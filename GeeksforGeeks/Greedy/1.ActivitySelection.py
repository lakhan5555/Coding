def ActivitySelection(a,n):

    # sortef according to finish time
    a.sort(key = lambda x: x[1])
    s = []
    i = 0
    s.append(a[i])
    for j in range(1,n):
        if a[j][0] >= a[i][1]:
            s.append(a[j])
            i = j
    return s

a = [[5,9],[1,2],[3,4],[0,6],[5,7],[8,9]]
n = len(a)
s = ActivitySelection(a,n)
print("Following Activites are selected: ")
print(s)
