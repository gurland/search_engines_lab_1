from dataclasses import dataclass


@dataclass
class Document:
    reference: str
    content: str

    @classmethod
    def from_medium_csv_line(cls, url, title, subtitle):
        return cls(url, title + subtitle)

    @staticmethod
    def normalize_text(text: str) -> str:
        replace_chars = {
            ".": " ",
            "…": " ",
            ",": " ",
            "?": " ",
            ":": " ",
            "\n": " "
        }

        for source, dest in replace_chars.items():
            text = text.replace(source, dest)

        return text.lower()

    def __post_init__(self):
        self.content = self.normalize_text(self.content)

    def words(self):
        return [word.strip() for word in self.content.split()]
