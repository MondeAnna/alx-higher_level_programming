#!/usr/bin/python3

"""
prevent dynamic attributes
"""


class LockedClass:
    """
    prevent dynamic attributes
    """
    def __setattr__(self, attr, value):
        if attr == "first_name":
            return object.__setattr__(self, attr, value)
        message = f"`{attr}` is invalid, perhaps `first_name`"
        raise AttributeError(message)
