import nltk
import string
import re
import inflect
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import simplemma
import logging

# Tool Description
"""
This script processes a text file 'input.txt', performs a series of preprocessing
operations on the text, and saves the result in the file 'output.txt'.
Make sure to insert the text into the 'input.txt' file before running the script.
"""

# Configure the logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)


def main():
    logger.info("Starting the text processing.")
    file_name = "input.txt"
    data = read_file(file_name)

    if "Error" in data:
        logger.error("Process interrupted due to an error in reading the file.")
        return

    # lowercase
    logger.info("Converting text to lowercase.")
    data = text_lowercase(data)

    # convert number
    logger.info("Converting numbers to words.")
    data = convert_number(data)

    # remove whitespace from text
    logger.info("Removing extra whitespace.")
    data = remove_whitespace(data)

    # remove punctuation
    logger.info("Removing punctuation.")
    data = remove_punctuation(data)

    # remove stopwords function
    logger.info("Removing stopwords.")
    data = remove_stopwords(data)

    # Lemmatization of the text
    logger.info("Lemmatizing the text.")
    data = lemma_words(data)

    # join list to string
    logger.info("Joining words into a single string.")
    data = join_strings(data)

    write_file(data, "output.txt")
    logger.info("Processing completed. The result has been saved in 'output.txt'.")


# Read input.txt file
def read_file(file_name):
    logger.info("Reading the file '{}', operation in progress...".format(file_name))
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        logger.error("Error: File not found.")
        return "Error: The file was not found."
    except IOError:
        logger.error("Error: Issues with reading the file.")
        return "Error: Issues with reading the file."


# Write to input.txt file
def write_file(text, file_name):
    logger.info("Writing to the file '{}', operation in progress...".format(file_name))
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(text)
        return True
    except IOError:
        logger.error("Error: Unable to write to the file.")
        return False


# join list to string
def join_strings(list):
    return " ".join(list)


# text lowercase
def text_lowercase(text):
    return text.lower()


def convert_number(text):
    p = inflect.engine()
    # split string into list of words
    temp_str = text.split()
    # initialize empty list
    new_string = []

    for word in temp_str:
        # if word is a digit, convert the digit
        # to numbers and append into the new_string list
        if word.isdigit():
            temp = p.number_to_words(word)
            new_string.append(temp)

        # append the word as it is
        else:
            new_string.append(word)

    # join the words of new_string to form a string
    temp_str = " ".join(new_string)
    return temp_str


# remove punctuation
def remove_punctuation(text):
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)


# remove whitespace from text
def remove_whitespace(text):
    return " ".join(text.split())


# remove stopwords function
def remove_stopwords(text):
    nltk.download("stopwords")
    stop_words = set(stopwords.words("italian"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return filtered_text


# Lemmatization of the text
def lemma_words(text):
    result = []
    for word in text:
        result.append(simplemma.lemmatize(word, lang="it"))
    return result


if __name__ == "__main__":
    main()
