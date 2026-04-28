list = []

list.append(10)
list.append(20)
list.append(30)
list.append(40)
list.append(50)

print(list)

list.insert(2, 99)
print(list)

list.extend([60, 70])
print(list)

list.append([80, 90])
print(list)

list.remove(99)
print(list)

x = list.pop()
print(x)
print(list)

list.pop(3)
print(list)

list.clear()
print(list)

list = [1, 2, 2, 3, 2]
print(list.count(2))

print(list.index(3))

list = [5, 2, 8, 1]
list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

new_list = list.copy()
new_list.append(100)

print(list)
print(new_list)

list = [1, 2, 2, 3, 4, 4]
new = []

for i in list:
    if i not in new:
        new.append(i)

print(new)

a = [1, 2]
b = [3, 4]

a.extend(b)
print(a)

list = [10, 20, 30, 40]
list.insert(2, 99)
list.pop(3)

print(list)

list = [1, 5, 5, 3, 5]

largest = max(list)
print(list.count(largest))

words = ["banana", "apple", "cherry"]
words.sort()

print(words)