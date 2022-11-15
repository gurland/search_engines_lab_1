"""Task 0"""
import os
import tempfile
import unittest

from document import Document
from indexes import build_inverted_index, build_forward_index
from utils import load_dataset


class TestInvertedIndex(unittest.TestCase):
    test_documents = [
        Document("url_1", "some words appearing in the first document"),
        Document("url_2", "a few words got even into this document"),
        Document("url_3", "not first but third"),
        Document("url_4", ""),
        Document("url_5", "what in the name of Guido is this"),
    ]

    def setUp(self):
        # Create a temporary directory
        self.test_csv_file = tempfile.mktemp()
        with open(self.test_csv_file, "w") as f:
            pass

    def tearDown(self):
        # Remove the directory after the test
        os.remove(self.test_csv_file)

    def test_document_tokenization(self):
        self.assertEqual(
            Document("test_ref", "That   should  beCOMe normalized.tEXt.").words(),
            ["that", "should", "become", "normalized", "text"]
        )

    def test_inverted_index_build(self):
        inverted_index = build_inverted_index(self.test_documents)

        self.assertEqual(
            inverted_index,
            {
                'a': {'url_2'},
                'appearing': {'url_1'},
                'but': {'url_3'},
                'document': {'url_2', 'url_1'},
                'even': {'url_2'},
                'few': {'url_2'},
                'first': {'url_3', 'url_1'},
                'got': {'url_2'},
                'guido': {'url_5'},
                'in': {'url_5', 'url_1'},
                'into': {'url_2'},
                'is': {'url_5'},
                'name': {'url_5'},
                'not': {'url_3'},
                'of': {'url_5'},
                'some': {'url_1'},
                'the': {'url_5', 'url_1'},
                'third': {'url_3'},
                'this': {'url_2', 'url_5'},
                'what': {'url_5'},
                'words': {'url_2', 'url_1'}
            }
        )

    def test_forward_index_build(self):
        forward_index = build_forward_index(self.test_documents)

        self.assertEqual(
            forward_index,
            {
                'url_1': {'the', 'words', 'document', 'in', 'appearing', 'first', 'some'},
                'url_2': {'few', 'into', 'got', 'even', 'words', 'document', 'a', 'this'},
                'url_3': {'first', 'third', 'not', 'but'},
                'url_4': set(),
                'url_5': {'the', 'is', 'guido', 'in', 'this', 'of', 'name', 'what'}
            }
        )

    def test_csv_documents_creation(self):
        test_csv = "id,url,title,subtitle,f1,f2,f3\n" \
                   "1,url_1,Title 1 is good,subtitle also is ok,fff,fff,fff\n" \
                   "2,url_1,Title 2, subtitle 2 also is ok,fff,fff,fff\n"

        with open(self.test_csv_file, "w") as f:
            f.write(test_csv)

        self.assertEqual(
            load_dataset(self.test_csv_file),
            [
                Document(reference='url_1', content='title 1 is goodsubtitle also is ok'),
                Document(reference='url_1', content='title 2 subtitle 2 also is ok')
            ]
        )


if __name__ == '__main__':
    unittest.main()
