"""
a file containing the class VerboseList
"""


class VerboseList(list):
    """ a class VerboseList extending the class list"""
    def append(self, object, /) -> None:
        """ append version where the item appended gets printed """
        super().append(object)
        print("Added [{}] to the list.".format(object))

    def extend(self, iterable, /) -> None:
        """ extend version where the iterable gets printed"""
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, value, /) -> None:
        """ remove version where the value gets printed """
        super().remove(value)
        print("Removed [{}] from the list.".format(value))

    def pop(self, index=-1, /):
        """ pop version where the value gets printed """
        value = super().pop(index)
        print("Popped [{}] from the list.".format(value))
        return value
