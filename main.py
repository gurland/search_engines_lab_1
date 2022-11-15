from indexes import build_inverted_index, build_forward_index
from utils import load_dataset


if __name__ == '__main__':
    # Using dataset from https://www.kaggle.com/datasets/dorianlazar/medium-articles-dataset?resource=download
    medium_titles = load_dataset("medium_data.csv")

    inverted_index = build_inverted_index(medium_titles)
    forward_index = build_forward_index(medium_titles)

    print(f"Your inverted index is: {inverted_index}")
    print(f"Your forward index is: {forward_index}")
