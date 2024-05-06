# 5-39

import math
goal = 30000000
salary = 5000000
res = 0

if ((goal - salary) * (100/112)) >= 10000001:
    res = ((goal - salary) * (100/112))
elif ((goal - salary) * (100/110)) >= 5000001:
    res = ((goal - salary) * (100/110))
else:
    res = ((goal - salary) * (100/108))
print(math.ceil(res))
