Question2

List comprehensions are used for creating new lists from other iterables. As list comprehensions return lists, they consist of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element.


1st-[1,2,3,4,5,6,7,8,9,10]

print(1st)

list1=[i for i in range(11,19)] print(list1)

#list.append(x)

list1.append(20)

print(list1)

#list.insert(i, x)

list1.insert(8,19)

print (list1)

#list.extend(iterable) 1st.extend(1ist1)

print(1st)

#list.remove(x)

1st.remove(20)

print(1st)

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

[11, 12, 13, 14, 15, 16, 17, 18] [11, 12, 13, 14, 15, 16, 17, 18, 20] [11, 12, 13, 14, 15, 16, 17, 18, 19,

20]

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
