from LinkedList import _LinkedList

lk = _LinkedList()

lk.insertItem(9, 0)
lk.insertItem(5, 0)
lk.insertItem(2, 0)
print(list(lk))

lk.insertItem(3, 1)
print(list(lk))

lk.removeItem(3)
lk.removeItem(1)
lk.removeItem(0)
print(list(lk))