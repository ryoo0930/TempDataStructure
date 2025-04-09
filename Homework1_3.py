from DoublyLinkedList import _DoublyLinkedList

dl = _DoublyLinkedList()
dl.insertItem(9, 0)
dl.insertItem(5, 0)
dl.insertItem(2, 0)
print(list(dl))

dl.insertItem(3, 1)
print(list(dl))

dl.removeItem(3)
dl.removeItem(1)
dl.removeItem(0)
print(list(dl))