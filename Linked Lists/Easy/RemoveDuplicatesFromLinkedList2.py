# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def helper(linkedList):
    if linkedList is None or linkedList.next is None:
        return linkedList

    if linkedList.value == linkedList.next.value:
        linkedList.next = linkedList.next.next
    else:
        linkedList = linkedList.next
    removeDuplicatesFromLinkedList(linkedList)
    return linkedList

def removeDuplicatesFromLinkedList(linkedList):
    
    head = linkedList
    helper(linkedList)
    return head
