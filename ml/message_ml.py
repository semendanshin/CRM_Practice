from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pymorphy2 import MorphAnalyzer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier

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
stop_words = set(stopwords.words('russian'))
morph = MorphAnalyzer()
y_train = list(dataset_dict.keys())


def sign_delete(text):
    dataset_text = []
    if type(text) == list:
        for line in text:
            dataset_text.append(
                line.replace('"', '').replace('\n', '').replace('.', '').replace(':', '').replace(',', '').replace('?',
                                                                                                                   '').replace(
                    '!', ''))
    else:
        dataset_text = text.replace('"', '').replace('\n', '').replace('.', '').replace(':', '').replace(',', '').replace('?',
                                                                                                                   '').replace(
                    '!', '')
    return dataset_text


def word_tokenize_pro(text):
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


dataset_train = create_dataset('Nlp_dataset.txt', dataset_dict)

sgd_ppl_clf = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('sgd_clf', SGDClassifier(random_state=42))])
knb_ppl_clf = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('knb_clf', KNeighborsClassifier(n_neighbors=1))])
sgd_ppl_clf.fit(dataset_train, y_train)
knb_ppl_clf.fit(dataset_train, y_train)

def what_problem(text):
    pre_text = word_tokenize_pro(sign_delete(text))
    return sgd_ppl_clf.predict([pre_text])[0],knb_ppl_clf.predict([pre_text])[0]
