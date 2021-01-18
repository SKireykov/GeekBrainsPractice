from itertools import count

for i in count(10):
    if i > 30:
        break
    else:
        print(i)

from itertools import cycle

count = 0
for item in cycle("ONI"):
    if count > 11:
        break
    print(item)
    count +=1

