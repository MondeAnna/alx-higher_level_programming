#!/usr/bin/python3


"""
Indent text

>>> text_indentation("Hello. World")
Hello.
<BLANKLINE>
World
>>>
"""


def text_indentation(text):
    """
    Indent text
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    full_stopped = text.replace(". ", ".").replace(".", ".\n\n")
    questioned = full_stopped.replace("? ", "?").replace("?", "?\n\n")
    final = questioned.replace(": ", ":").replace(":", ":\n\n")

    print(final)
