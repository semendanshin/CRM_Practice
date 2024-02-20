from pymorphy2 import MorphAnalyzer
from typing import Optional, Set

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def sign_delete(text: str | list[str]) -> str:
    signs = ['"', '\n', '.', ':', ',', '?', '!', "'", '(', ')', '-', '—', '–']
    if isinstance(text, list):
        text = ' '.join(text)
    for sign in signs:
        text = text.replace(sign, '')
    return text


def word_tokenize_pro(text: str, stop_words: Optional[Set[str]] = None, morph: Optional[MorphAnalyzer] = None) -> str:
    if stop_words is None:
        stop_words = set(stopwords.words('russian'))
    if morph is None:
        morph = MorphAnalyzer()

    pre_text = word_tokenize(text)
    fin_text = ''
    for word in pre_text:
        if word not in stop_words:
            fin_text += ' ' + (morph.parse(word)[0][2])
    return fin_text
