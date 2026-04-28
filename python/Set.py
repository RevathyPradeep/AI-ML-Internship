set = set()

set.add(10)
set.add(20)
set.add(30)
set.add(40)
set.add(50)

print(set)

set = {1, 2, 3, 4}

set.remove(2)
print(set)

set.discard(10)
print(set)

set1 = {10, 20, 30}

set2 = set1.copy()

set1.add(40)

print("Original:", set1)
print("Copy:", set2)

set = {5, 10, 15}

set.clear()

print(set)

set = {1, 2, 3, 4}

print(2 in set)
print(10 in set)

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))

a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))

a = {1, 2, 3}
b = {2, 4}

print(a.difference(b))

a = {1, 2, 3}
b = {2, 3, 4}

print(a.symmetric_difference(b))

a = {1, 2}
b = {3, 4}

a.update(b)

print(a)