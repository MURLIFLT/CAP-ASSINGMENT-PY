#Write a Python program to print all positive numbers in a range.

list1 = [12, -7, 5, 64, -14] 
list2 = [12, 14, -95, 3] 

for num in list1:
    for num in list2: 
        if num >= 0:
            print(num, end = " ")
