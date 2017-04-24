def measure():
    import time
    t0 = time.time()
    t1 = t0
    while t1 == t0:
        t1 = time.time()
    return (t0, t1, t1-t0)

def measure_clock():
    import time
    t0 = time.clock()
    t1 = t0
    while t1 == t0:
        t1 = time.clock()
    return (t0, t1, t1-t0)

samples = [measure() for i in range(10)]

for s in samples:
    print(s)

from functools import reduce


print(reduce(lambda a,b : a+b, [measure()[2] for i in range(1000)], 0.0) / 1000.0)

print(reduce(lambda a,b : a+b, [measure_clock()[2] for i in range(1000)], 0.0) / 1000.0)
