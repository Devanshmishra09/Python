employee= [
    {"name": "Alice", "salary": 17000},
    {"name": "Bob", "salary": 19000},
    {"name": "Charlie", "salary": 18000},
    {"name": "David", "salary": 16000}
]
increase=list(map(lambda x:x["salary"]*1.2,employee))
print(increase)