#      Date and Time 
#  Finding difference in time 

# difference in Hour :
import numpy as n 
a=n.datetime64("2026-09-27 00:01","h")
b=n.datetime64("2026-09-28 16:00","h")
print(b-a)

# difference in Minute:
import numpy as n 
a=n.datetime64("2026-09-27 00:01","h")
b=n.datetime64("2026-09-28 16:00","h")
print(b-a)

# difference in Second :
import numpy as n 
a=n.datetime64("2026-09-27 00:01","h")
b=n.datetime64("2026-09-28 16:00","h")
print(b-a)

#Timedelta64
# use to add or subtract time 


import numpy as n 
a=n.datetime64("2026-09-27 00:01","h")
b=n.timedelta64("10","h")
print(a+b)

