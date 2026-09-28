#multiple datatype assign
n_list=[2.9,3000,'Hello',"Welcome to python list ", True]
print(n_list)
 
# Nested List Example1
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][3])
print(n_list[1][2])
 
# Nested indexing
print(my_list[1][1])
print(my_list[2][2])

# Negative indexing in lists
my_list = ['p','r','o','b','e']
print(my_list[-1])
print(my_list[-5])

# Appending and Extending lists in Python

odd = [1, 3, 5]
odd.append(7)
print(odd)

odd.extend([9, 11, 13])
print(odd)


# Concatenating and repeating lists
odd = [1, 3, 5]

print(odd + [9, 7, 5])

print(["re"] * 3)






#USIN A WHILE LOOP
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#PYTHON SORTS LIST
  thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
Output:['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#sort decending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#python copy lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#python insert
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

#remove specified index
thislist = ["apple","banana","cherry"]
thislist.pop(1)
print(thislist)

#clear the results
Clear the list content:
thislist = ["apple","banana","cherry"]
thislist.clear()
print(thislist)

#python list count
fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = fruits.count(9)
print(x)

# Program to demonstrate

lst = [10, 20, 30, 40]

# Create a copy of the list
new_lst = lst.copy()

print("Original List :", lst)
print("Copied List   :", new_lst)

#list index() method
lst = [10, 20, 30, 40, 50]

value = 30

position = lst.index(value)

print("List     :", lst)
print("Value    :", value)
print("Index    :", position)

#python pop
 t = ['a', 'b', 'c']
 x = t.pop(1)
 print (t)
['a', 'c']
 print (x)
b

#python remove
 t = ['a', 'b', 'c']
t.remove('b')
print (t)
['a', 'c']

#python list built in functions
 nums = [3, 41, 12, 9, 74, 15]
 print len(nums)

 #python spilit
 s = 'pining for the fjords'
 t = s.split()
 print (t)
['pining', 'for', 'the', 'fjords']
 print t[2]










            

