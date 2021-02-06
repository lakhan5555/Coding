class Box:
    def __init__(self,h,w,d):
        self.h = h
        self.w = w
        self.d = d

    def __lt__(self,other):
        return self.w * self.d < other.w * other.d

def maxStackHeight(a,n):
    rot = [Box(0,0,0) for i in range(3*n)]

    index = 0

    for i in range(n):
        rot[index].h = a[i].h
        rot[index].w = min(a[i].w,a[i].d)
        rot[index].d = max(a[i].w,a[i].d)
        index += 1

        rot[index].h = a[i].w
        rot[index].w = min(a[i].h,a[i].d)
        rot[index].d = max(a[i].h,a[i].d)
        index += 1

        rot[index].h = a[i].d
        rot[index].w = min(a[i].w,a[i].h)
        rot[index].d = max(a[i].w,a[i].h)
        index += 1

    n *= 3

    rot.sort(reverse = True)

    dp = [0]*n
    for i in range(n):
        dp[i] = rot[i].h

    for i in range(1,n):
        for j in range(i):
            if (rot[i].w < rot[j].w) and (rot[i].d < rot[j].d):
                if dp[i] < dp[j] + rot[i].h:
                    dp[i] = dp[j] + rot[i].h

    return max(dp)

if __name__=="__main__":
    arr = [Box(4, 6, 7), Box(1, 2, 3),
           Box(4, 5, 6), Box(10, 12, 32)]
    n = len(arr)
    print("The maximum possible height of stack is",
           maxStackHeight(arr, n))
