import pickle

import nltk
from nltk.corpus import stopwords
from pymorphy2 import MorphAnalyzer
from sklearn.pipeline import Pipeline


def sign_delete(text):
    dataset_text = []
    if type(text) == list:
        for line in text:
            dataset_text.append(
                line.replace('"', '').replace('\n', '').replace('.', '').replace(':', '').replace(',', '').replace('?',
                                                                                                                   '').replace(
                    '!', ''))
    else:
        dataset_text = text.replace('"', '').replace('\n', '').replace('.', '').replace(':', '').replace(',',
                                                                                                         '').replace(
            '?',
            '').replace(
            '!', '')
    return dataset_text


def word_tokenize_pro(text, stop_words=None, morph=MorphAnalyzer()):
    if stop_words is None:
        stop_words = set(stopwords.words('russian'))
    from nltk.tokenize import word_tokenize
    pre_text = word_tokenize(text)
    fin_text = ''
    for word in pre_text:
        if word not in stop_words:
            fin_text += ' ' + (morph.parse(word)[0][2])
    return fin_text


def create_table(dataset_text, dataset_dict):
    dataset = ['', '', '', '', '', '', '', '']
    for line in dataset_text:
        if line in dataset_dict.keys():
            pos = dataset_dict[line]
        if line not in dataset_dict.keys() and line != '':
            dataset[pos] += (word_tokenize_pro(line))
    return dataset


def create_dataset(file_name, dataset_dict):
    pre_dataset = open(file_name, encoding='utf-8').readlines()
    pre_dataset = sign_delete(pre_dataset)
    return create_table(pre_dataset, dataset_dict)


def train_model(pipeline, train_data, y_train):
    pipeline.fit(train_data, y_train)
    return pipeline


def what_problem(model: Pipeline, text: str):
    pre_text = word_tokenize_pro(sign_delete(text))
    return model.predict([pre_text])[0]


def save_model(model: Pipeline, model_name: str):
    pickle.dump(model, open(model_name, 'wb'))


def load_model(model_name: str) -> Pipeline:
    return pickle.load(open(model_name, 'rb'))


def train_and_save_models():
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import SGDClassifier
    from sklearn.neighbors import KNeighborsClassifier

    nltk.download('stopwords')
    nltk.download('punkt')

    dataset_dict = {
        'Инцидент': 0,
        'Запрос на обслуживание': 1,
        'Выезд': 2,
        'Внутренняя помощь': 3,
        'Проект': 4,
        'Поставка': 5,
        'Проблема': 6,
        'Задача': 7
    }

    y_train = list(dataset_dict.keys())

    dataset_train = create_dataset('Nlp_dataset.txt', dataset_dict)

    pipelines = [
        Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('sgd_clf', SGDClassifier(random_state=42))
        ]),
        Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('knb_clf', KNeighborsClassifier(n_neighbors=1))
        ])
    ]

    for pipeline in pipelines:
        train_model(pipeline, dataset_train, y_train)
        save_model(pipeline, f'{pipeline.steps[1][0]}.pkl')


if __name__ == '__main__':
    train_and_save_models()
    print(what_problem(load_model('sgd_clf.pkl'), 'Прошу помочь с установкой программы'))
    print(what_problem(load_model('knb_clf.pkl'), 'Прошу помочь с установкой программы'))
