import pickle

from self_trained_clf import sign_delete, word_tokenize_pro

from .AbstractClassifier import AbstractClassifier
from .types import HumanReadableResponse


class KNeighbours(AbstractClassifier):
    def __init__(self, model_file: str = 'models/knb_clf.pkl'):
        self.model = pickle.load(open(model_file, 'rb'))

    async def predict(self, text: str):
        pre_text = word_tokenize_pro(sign_delete(text))
        response = self.model.predict([pre_text])[0]
        return HumanReadableResponse(response)

    def __str__(self):
        return 'KNeighbours'
