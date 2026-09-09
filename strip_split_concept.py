# Q 1

para="hello bhai hello  "
words=para.lower().split()
freq={}
for i in words:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

# Q 2

para="hello bhai hello"
word=para.lower().strip()
freq={}
for i in word:
    if i in freq:
        freq[i]+=1 
    else:
        freq[i]=1 
print(freq)

# Q 3


para=" hello bhai hello"
word=para.lower().split()
freq={}
for i in word:
    for w in i:
        if i in freq:
            freq[w]+=1 
        else:
            freq[w]=1 
print(freq)

# Q 4

para="hello bhai hello"
word=para.lower().strip()
freq={}
for i in word:
    for w in i:
        if w in freq:
            freq[w]+=1 
        else:
            freq[w]=1 
print(freq)

# Q 5

para=" hello word hello"
word=para.lower().strip()
freq={}
for i in word:
    if i!=" ":
        if i in freq:
            freq[i]+=1 
        else:
            freq[i]=1 
print(freq)
