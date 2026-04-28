n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print("\nEnter details for Student", i + 1)

    name = input("Enter name: ")

    m1 = float(input("Enter marks for Subject 1: "))
    m2 = float(input("Enter marks for Subject 2: "))
    m3 = float(input("Enter marks for Subject 3: "))

    total = m1 + m2 + m3
    average = total / 3

    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"

    student = {
        "name": name,
        "marks": [m1, m2, m3],
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)

print("\n--- All Student Results ---")
for s in students:
    print("\nName:", s["name"])
    print("Marks:", s["marks"])
    print("Total:", s["total"])
    print("Average:", round(s["average"], 2))
    print("Grade:", s["grade"])

search_name = input("\nEnter student name to search: ")

found = False

for s in students:
    if s["name"].lower() == search_name.lower():
        print("\nStudent Found!")
        print("Name:", s["name"])
        print("Marks:", s["marks"])
        print("Total:", s["total"])
        print("Average:", round(s["average"], 2))
        print("Grade:", s["grade"])
        found = True
        break

if not found:
    print("Student not found!")