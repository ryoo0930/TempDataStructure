from ArrayBasedList import _ArrayBasedList

arr = _ArrayBasedList(10)

arr.insertItem(9, 0)
arr.insertItem(5, 0)
arr.insertItem(2, 0)
print(list(arr))

arr.insertItem(3, 1)
print(list(arr))

arr.removeItem(3)
arr.removeItem(1)
print(list(arr))