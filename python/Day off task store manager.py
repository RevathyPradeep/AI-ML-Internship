items = ["pen", "book", "bag", "bottle", "notebook"] 
prices = { 
    "pen": 10, 
    "book": 50, 
    "bag": 300, 
    "bottle": 150, 
    "notebook": 80 
  }
total = sum(prices[item] for item in items)
print(total) 

items = ["pen", "book", "bag"]
prices = {"pen": 10, "book": 50, "bag": 300}
print(prices)

print("items and prices:")
for item in items:
  print(item,":",prices[item])

prices["book"]=60
print("\nUpdated price of book:",prices["book"])

items.remove("pen")
prices.pop("pen")

print("\nAfter removing 'pen':")
for item in items:
    print(item,":",prices[item])

expensive_item=max(prices,key=prices.get)
print("\nMost expensive item:",expensive_item,"-",prices[expensive_item])

total_price=sum(prices.values())
print("\nTotal price of all items:",total_price)

#Challenge:Items with price>100
print("\nItems with price greater than 100:") 
for item in prices: 
    if prices[item] > 100: 
      
        print(item, ":", prices[item])

#Bonus :search for item
search=input("\nEnter item to search:")
if search in prices:
    print(search,"price is:",prices[search])
else:
    print("item not found")      