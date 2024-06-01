import nltk
import string
import re
import inflect
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import simplemma


def main():
    file_name = "input.txt"  
    data = read_file(file_name)
    # lowercase
    data = text_lowercase(data)
    # convert number
    data = convert_number(data)
    # remove whitespace from text
    data = remove_whitespace(data)
    # remove punctuation
    data = remove_punctuation(data)
    # remove stopwords function
    data = remove_stopwords(data)
    # Lemmatization of the text
    data = lemma_words(data)
    # join list to string
    data = join_strings(data)
    write_file(data, "output.txt")


# Read input.txt file
def read_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return "Error: The file was not found."
    except IOError:
        return "Error: Issues with reading the file."


# Write to input.txt file
def write_file(text, file_name):
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(text)
        return True
    except IOError:
        print("Error: Unable to write to the file.")
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
    # initialise empty list
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
    return  result


if __name__ == "__main__":
    main()
