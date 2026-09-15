para="hello world theat vfbr, fdfd, world, hello ,dvf,fd,og og"
words=para.lower().split()
freq={}
for i in words:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

para="hellowor ldtheat vfbrfdfdworl dhellodvfdogog"
letter=para.lower().split()
freq={}
for i in letter:
    for w in i:
        if w in freq:
            freq[w]+=1
        else:
            freq[w]=1
print(freq)

para="h ellowor ldtheat vfbrfdf dworl dhellodvfdogog"
letter=para.lower().strip()
freq={}
for i in letter:
  if i!= " ":
    if i in freq:
        freq[i]+=1   
    else:                                                     
        freq[i]=1                       
print(freq)    






                                                                               