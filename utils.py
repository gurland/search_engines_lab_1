from document import Document

from typing import List
from csv import reader


def load_dataset(file_path: str) -> List[Document]:
    with open(file_path, "r") as csv_file:
        medium_csv = reader(csv_file)
        next(medium_csv)  # Skip CSV heading

        return [
            Document.from_medium_csv_line(url, title, subtitle)
            for _, url, title, subtitle, *_ in medium_csv
        ]
