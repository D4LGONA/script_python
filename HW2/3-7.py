# 3-7
import time
import random

random.seed(time.time())
random_char = chr(random.randint(65, 90))
print("생성된 문자:", random_char)
