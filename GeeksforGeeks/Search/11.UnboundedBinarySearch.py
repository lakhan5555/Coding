# Find the point where a monotonically increasing
# function becomes positive first time

def f(x):
    return x*x - 10*x - 20

def FirstPositiveNumber():
    if f(0) > 0:
        return 0

    i = 1
    while f(i) <= 0:
        i = i*2

    return BinarySearch(i/2, i)

def BinarySearch(l,r):
    if l<=r:
        m = int(l + (r-l)/2)
        if f(m) > 0 and (m == l or f(m-1) <= 0):
            return m
        if f(m) <= 0:
            return BinarySearch(mid+1,r)
        else:
            return BinarySearch(l,m-1)
    return -1

print("The value n where f() becomes positive first is: ",FirstPositiveNumber())
