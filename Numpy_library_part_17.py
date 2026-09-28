# Date and time : 
# find date and time accouding to use 

import numpy as n 
a=n.datetime64("2026-09-28","Y")
print(a)

# for Month
import numpy as n 
a=n.datetime64("2026-09-28","M")
print(a)

# for date 
import numpy as n 
a=n.datetime64("2026-09-28","D")
print(a)

#  Find difference between date 
import numpy as n 
a=n.datetime64("2026-09-28")
b=n.datetime64("2026-06-28")
print(a-b)

#  Find difference between Hour 
import numpy as n 
a=n.datetime64("2026-09-28","h")
b=n.datetime64("2026-06-28","h")
print(a-b)

#  Find difference between minute 
import numpy as n 
a=n.datetime64("2026-09-28","m")
b=n.datetime64("2026-06-28","m")
print(a-b)

#  Find difference between months 
import numpy as n 
a=n.datetime64("2026-09-28","M")
b=n.datetime64("2026-06-28","M")
print(a-b)