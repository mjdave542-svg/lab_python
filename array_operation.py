

# 1) len() - Number of elements
import array
arr = array.array('i', [10, 20, 30, 40, 50])
print(len(arr))

# Output: 5


# 2) append(x) - Add element at End
import array
arr = array.array('i', [10, 20, 30])
arr.append(40)
print(arr)

# Output: array('i', [10, 20, 30, 40])


# 3) insert(pos, x) - Insert at Position
import array
arr = array.array('i', [10, 20, 40])
arr.insert(2, 30)
print(arr)

# Output: array('i', [10, 20, 30, 40])


# 4) remove(x) - Remove first occurrence
import array
arr = array.array('i', [10, 20, 30, 20, 40])
arr.remove(20)
print(arr)

# Output: array('i', [10, 30, 20, 40])


# 5) pop() - Remove and Return last element
import array
arr = array.array('i', [10, 20, 30, 40])
x = arr.pop()
print("Removed:", x)
print(arr)

# Output:
# Removed: 40
# array('i', [10, 20, 30])


# 6) index(x) - Find index of element
import array
arr = array.array('i', [10, 20, 30, 40])
print(arr.index(30))

# Output: 2


# 7) count(x) - Count occurrences
import array
arr = array.array('i', [10, 20, 30, 20, 40])
print(arr.count(20))

# Output: 2


# 8) reverse() - Reverse array
import array
arr = array.array('i', [10, 20, 30, 40])
arr.reverse()
print(arr)

# Output: array('i', [40, 30, 20, 10])
