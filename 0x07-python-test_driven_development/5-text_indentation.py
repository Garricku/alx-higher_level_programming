#!/usr/bin/python3
"""Defines a fucntion that prints a text with 2 lines after each ., ? and :."""
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    # Check that text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text into sentences
    sentences = text.split(".")
    for i in range(len(sentences)):
        sentences[i] = sentences[i].strip()
        if sentences[i]:
            sentences[i] += ".\n\n"

    # Split each sentence into sub-sentences
    sub_sentences = []
    for sentence in sentences:
        sub_sentences += sentence.split("?")
    for i in range(len(sub_sentences)):
        sub_sentences[i] = sub_sentences[i].strip()
        if sub_sentences[i]:
            sub_sentences[i] += "?\n\n"

    # Print the sub-sentences
    for sub_sentence in sub_sentences:
        print(sub_sentence.strip())
