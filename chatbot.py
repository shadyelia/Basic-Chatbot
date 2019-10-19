import pandas as pd
import numpy as np
import tensorflow as tf
import re
import time


def splitingDataSet():
    """Reading dataset and spliting it"""
    # Load the data
    lines = open('movie_lines.txt', encoding='utf-8',
                 errors='ignore').read().split('\n')
    conv_lines = open('movie_conversations.txt', encoding='utf-8',
                      errors='ignore').read().split('\n')

    # The sentences that we will be using to train our model.
    lines[:10]

    # The sentences' ids, which will be processed to become our input and target data.
    conv_lines[:10]

    # Create a dictionary to map each line's id with its text
    id2line = {}
    for line in lines:
        _line = line.split(' +++$+++ ')
        if len(_line) == 5:
            id2line[_line[0]] = _line[4]

    # Create a list of all of the conversations' lines' ids.
    convs = []
    for line in conv_lines[:-1]:
        _line = line.split(
            ' +++$+++ ')[-1][1:-1].replace("'", "").replace(" ", "")
        convs.append(_line.split(','))

    convs[:10]

    questions = []
    answers = []

    for conv in convs:
        for i in range(len(conv)-1):
            questions.append(id2line[conv[i]])
            answers.append(id2line[conv[i+1]])

    # Check if we have loaded the data correctly
    limit = 0
    for i in range(limit, limit+5):
        print(questions[i])
        print(answers[i])
        print()

    # Compare lengths of questions and answers
    print(len(questions))
    print(len(answers))
    return questions, answers


def main():
    questions, answers = splitingDataSet()


if __name__ == '__main__':
    main()
