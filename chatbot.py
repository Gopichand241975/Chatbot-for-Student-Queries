"""
Student Query Chatbot
A simple rule-based chatbot that answers common student questions
by matching user input against keywords stored in qa_dataset.csv.
"""

import csv
import string
import os

#dataset was created 
DATASET_FILE = "qa_dataset.csv"
EXIT_WORDS = ("bye", "exit", "quit", "goodbye", "see you")
DEFAULT_RESPONSE = (
    "Sorry, I didn't understand that. Try asking about courses, timings, "
    "fees, admissions, hostel, library, placements, exams, or scholarships."
)


#load dataset
def load_dataset(filepath):
    #Read the CSV dataset and build a list of (keywords_list, answer) pairs.
    qa_pairs = []
    filepath = os.path.join(os.path.dirname(__file__), filepath)

    with open(filepath, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            keywords = row["keywords"].split(";")
            keywords = [k.strip().lower() for k in keywords]
            answer = row["answer"].strip()
            qa_pairs.append((keywords, answer))

    return qa_pairs


def clean_input(text):
    """Lowercase the text and remove punctuation."""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.strip()


def is_exit(cleaned_text):
    #Check if the cleaned input matches any exit word.
    return any(word in cleaned_text for word in EXIT_WORDS)


def get_response(cleaned_text, qa_pairs):
    """Match cleaned input against dataset keywords and return best answer."""
    for keywords, answer in qa_pairs:
        if any(keyword in cleaned_text for keyword in keywords):
            return answer
    return DEFAULT_RESPONSE


def run_chatbot():
    qa_pairs = load_dataset(DATASET_FILE)

    print("=" * 55)
    print(" Student Query Chatbot")
    print("=" * 55)
    print("Ask me about courses, timings, fees, admissions,")
    print("hostel, library, placements, exams, or scholarships.")
    print("Type 'bye' or 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ")
        cleaned = clean_input(user_input)

        if is_exit(cleaned):
            print("Bot: Goodbye! Feel free to come back if you have more questions.")
            break

        response = get_response(cleaned, qa_pairs)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    run_chatbot()
