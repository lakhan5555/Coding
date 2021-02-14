def maximumActivities(n,start,end):
    '''
    :param n: number of activities
    :param start: start time of activities
    :param end: corresponding end time of activities
    :return: Integer, maximum number of activities
    '''
    for i in range(n):
        start[i] = [start[i],end[i]]
    start.sort(key = lambda x: x[1])
    count = 1
    i = 0
    for j in range(1,n):
        if start[j][0] >= start[i][1]:
            count += 1
            i = j
    return count  
