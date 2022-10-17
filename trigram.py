#!/usr/bin/env python3

import argparse
import collections
import fileinput
import re
import string
from nltk import ngrams

parser = argparse.ArgumentParser(
    description="Given one or more text files, display the top 100 most common trigrams."
)
parser.add_argument(
    "file",
    nargs="*",
    default="False",
    help="Provide one or more files you'd like to parse.",
)

args = parser.parse_args()

def trigram_parser(text):
    """
    This function takes a file or text as input, extracts each word in each line,
    tokenizes those words, and then calculates ngrams and their frequency in each
    individual file. It prints this information to stdout.
    """
    # ignore punctuation in the file- even within words.
    ignorePunctuation = "[" + string.punctuation + "]"
    sanitizedText = re.sub(ignorePunctuation, "", text)
    # split the file's text into individual words to evaluate.
    # we want to ignore the case as well.
    words = sanitizedText.split()
    a = [word.lower() for word in words]
    # the ngrams function takes two arguments- the data, and the length of the ngram.
    trigrams = ngrams(a, 3)
    # Counting the frequency of those trigrams.
    trigramFreq = collections.Counter(trigrams)
    # Sort by the most common trigrams.
    results = trigramFreq.most_common(100)
    # Concatenate the strings, which is our trigram.
    # Include the number of times that trigram has appeared.
    for i in results:
        print(f"{' '.join(i[0])} - {i[1]}")


# Input from stdin.
stdinLines = []

def main():
    if args.file != "False":
        for file in args.file:
            try:
                filename = open(file)
                text = filename.read()
            except (FileNotFoundError, IOError):
                print(
                    "File not found. It either doesn't exist, or it exists outside of the current working directory."
                )
                exit(1)
            # when you're passing more than one file as an argument, assume they want
            # the results  for each file individually. Otherwise, they should pipe
            # files to the script.
            print(
                f"--------------------------------\nTrigram results for the file: {file}\n--------------------------------"
            )
            trigram_parser(text)
    else:
        try:
            for line in fileinput.input():
                # Add those lines to our list
                stdinLines.append(line)
                text = "".join(stdinLines)
            trigram_parser(text)
        except KeyboardInterrupt:
            print(
                "\nUse a utility like cat to pipe a file to trigram.py. Type ./trigram.py -h for usage instructions."
            )
            exit(0)


if __name__ == "__main__":
    main()
