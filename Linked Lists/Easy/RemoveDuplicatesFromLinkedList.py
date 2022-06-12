# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    if linkedList is None:
        return linkedList

    head = linkedList
    while linkedList.next is not None:
        if linkedList.value == linkedList.next.value:
            linkedList.next = linkedList.next.next
        else:
            linkedList = linkedList.next

    return head