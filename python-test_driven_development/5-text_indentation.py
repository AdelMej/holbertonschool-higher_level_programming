#!/usr/bin/python3
"""Function to indent text.

uses separators like `?` `:` `.`
get rid leading whitespaces and ending whitespaces
should be type safe
"""


def text_indentation(text):
    """print text with indentation

    Args:
        text(str): a string to print and indent

    Returns:
        None

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    is_word = False
    for c in text:
        if c == " " and not is_word:
            continue
        else:
            is_word = True

        if c in "?:.":
            is_word = False
            print(c, end="\n\n")
        else:
            print(c, end="")

