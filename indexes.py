from document import Document

from typing import List


def build_inverted_index(documents: List[Document]):
    index = {}
    for document in documents:
        for word in document.words():
            index.setdefault(word, set()).add(document.reference)

    return index


def build_forward_index(documents: List[Document]):
    index = {}
    for document in documents:
        index.setdefault(document.reference, set(document.words()))
    return index
