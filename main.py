from indexes import build_inverted_index, build_forward_index
from utils import load_dataset, chunks


if __name__ == '__main__':
    # Using dataset from https://www.kaggle.com/datasets/dorianlazar/medium-articles-dataset?resource=download
    medium_titles = load_dataset("medium_data.csv")

    inverted_index = build_inverted_index(medium_titles)
    forward_index = build_forward_index(medium_titles)

    print(f"Your inverted index is: {inverted_index}")
    print(f"Your forward index is: {forward_index}")

    # Task 4
    word_to_search = input("Enter any word you want to find in an inverted index: ")
    found_references = inverted_index.get(word_to_search)
    if found_references:
        print(f"Found this word in the following documents: {found_references}")
    else:
        print("Nothing found!")

    print("Your forward index:")

    for i, (reference, words) in enumerate(forward_index.items()):
        print(f"{i}. {reference}\n\tWords: {words}")
        input("Press Enter to view next article's words...")
