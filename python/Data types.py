num = [10, 20, 30, 20, 40] 
num.count(20) 
num.remove(20)
num.append(50)
print(num)

data = [5, 10, 15, 20, 25] 
max(data)
data = [5, 10, 15, 20, 25] 
min(data)
data = [5, 10, 15, 20, 25] 
sum(data)


items = [1, 2, 3] 
items.extend([4, 5]) 
items.pop() 
items.reverse()

student = {"A": 50, "B": 60}
student["C"] = 70
student["A"] = 80
student.values()

nums = [1,2,2,3,3,3,4] 
freq = {} 

for n in nums: 
    freq[n] = nums.count(n) 

print(freq)

list1 = [1,2,3] 
list2 = [3,4,5]
combined = list1 + list2
unique = list(set(combined))
unique.sort()
print(unique)