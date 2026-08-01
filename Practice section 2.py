# Q 1Create a set and print all elements
a={1,2,3,4,5,6,7,8,9,10}
print(a)

# Q 2 Find the union of two sets.
a={1,2,3,4,5,6,7,8,9,10}
b={11,12,13,14,15,16,17,18,19
,20}
print(a.union(b))   

# Q 3 find the intersection of two sets.
a={1,2,3,4,5,6,7,8,9
,10}
b={11,12,13,14,15,16,17,18,19
,20}
print(a.intersection(b))


# Q 4 Find the difference between two sets
a={1,2,3,4,5,6,7,8,9,10}
b={11,12,13,14,15,16,17,18,19,20}
print(a.difference(b))

# Q 5 Remove duplicate values from a list using a set.
a=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]
print(list(set(a))) 


# Q 6 Create a dictionary of student names and marks.
a={"John":85,"Alice":90,"Bob":78,"Eve":92}
print(a)

# Q 7 Print all keys of a dictionary. 
a={"John":85,"Alice":90,"Bob":78,"Eve":92}
print(a.keys())

# Q 8 Print all values of a dictionary.
a={"John":85,"Alice":90,"Bob":78,"Eve":92}
print(a.values())

# Q 9 Find the student with the highest marks
a={"John":85,"Alice":90,"Bob":78,"Eve":92}
highest_student = max(a, key=a.get)
print(highest_student, a[highest_student])

# Q 10 Find the student with the lowest marks
a={"John":85,"Alice":90,"Bob":78,"Eve":92}
lowest_student = min(a, key=a.get)
print(lowest_student, a[lowest_student])

# Q 11 Check whether a key exists in a dictionary
a={"John":85,"Alice":90,"Bob":78,"Eve":92}
print("John" in a)


# Q 12 Merge two dictionaries.
a={"John":85,"Alice":90}
b={"Bob":78,"Eve":92}
merged_dict = {**a, **b}
print(merged_dict)


# Q 13 Count the frequency of each character in a string using a dictionary.
a="hello world"
frequency = {}
for char in a:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)

# Q 14 Count the frequency of each word in a sentence 
a="hello world hello everyone"
frequency = {}
for word in a.split():
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print(frequency)


# Q 15 Swap keys and values in a dictionary
a={"John":85,"Alice":90,"Bob":78,"Eve":92}
swapped_dict = {value: key for key, value in a.items()}
print(swapped_dict)


