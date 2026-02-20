n=input("Enter lsit elements separated by spaces : ")
str_list=n.split()
numbers=[int(num) for num in str_list]
print("List : ",numbers)
largest = max(numbers)

smallest = min(numbers)
print("Largest number:", largest)

print("Smallest number:", smallest)

