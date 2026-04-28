#1.Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

#2.Print even num between 1 and 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

#3.Sum of first 10 natural numbers
total = 0

for i in range (1, 11):
    total += i

print(total)

#4.Print num from 10 to 1(reverse)
for i in range(10, 0, -1):
    print(i)

#5.Multiplication table
n = 5

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
