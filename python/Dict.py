#1.Create and access
student = {"name": "Abhay", "age": 20, "grade": "A+"}

print(student["grade"])
print(student.get("grade"))

print(student.get("marks", "Key not found"))

#2.Update
car ={"brand": "Honda", "model": "city"}

car["year"] = 2020
car["model"] = "Amaze"

print(car)

#3.pop()
fruits = {"apple": 100,"banana": 60,"orange": 80}

removed = fruits.pop("banana")
print(removed)
print(fruits)

#4.Popitem()
data = {"a": 1, "b": 2, "c":3}

print(data.popitem())
print(data.popitem())

#5.del statement
person = {"name": "Abhay", "age": 20, "city":"Mavelikara"}

del person["age"]
print(person)

#6.clear()
d= {"a": 1, "b": 2, "c": 3}

d. clear()
print(d)

#7.key()
country = {"India": "Delhi", "Japan": "Tokyo", "France": "Paris"}

print(country.keys())

for key in country.keys():
    print(key)

#8.Values()
print(country.values())

values_list = list(country.values())
print(values_list)

#9.items()
student = {"name": "Abhay", "Age": 20, "grade": "A+"}

print(student.items())

for k, v in student.items():
    print(f"key: {k}, value: {v}")

#10.copy()
original = {"x": 10, "y": 20}

copy_dict = original.copy()
copy_dict["x"] = 100

print(original)
print(copy_dict)

#11.fromkeys()
subjects = ["math", "science", "english"]

d = dict.fromkeys(subjects, 0)
print(d)

#12.setdefault()
person = {"name": "abhi", "age": 22}

person.setdefault("city", "kochi")
person.setdefault("age", 21)

print(person)

#13.update()
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)

#14.Nested dictionary
students = {
    "Ravi": {"math": 80, "science": 85},
    "Meena": {"math": 90, "science": 95}
}

print(students["Ravi"]["science"])

students["Meena"]["english"] = 88
print(students)

#15.Dictionary comprehension
squares = {x: x*x for x in range(1, 11)}
print(squares)

letters = {'a': 'apple', 'b': 'ball'}
upper = {k.upper(): v.upper() for k, v in letters.items()}
print(upper)

#16.Combining multiple methods

inventory = {}

inventory["rice"] = 10
inventory["milk"] = 5
inventory["egg"] = 12

inventory["milk"] = 8

inventory.pop("egg")

inventory.clear()

print(inventory)