    intervals = [[4,7],[1,4],[1,3],[2,6],[8,10],[15,18]]
    res = []
    i = 0
    print(len(intervals))
    for i in range(len(intervals)):
        res.append(intervals[i])
        if i-1 >= 0 and intervals[i][0] >= intervals[i-1][0] and intervals[i][0] <= intervals[i-1][1] and intervals[i][1] >= intervals[i-1][1]:
            intervals[i][0] = intervals[i-1][0]
            if res: 
                res.pop()
                res.pop()
            res.append(intervals[i])
        elif i+1 != len(intervals) and intervals[i][0] >= intervals[i+1][0] and intervals[i][0] >= intervals[i+1][1] and intervals[i][1] >= intervals[i+1][1]:
            intervals[i][0] = intervals[i+1][0]
            print("helo")
            if res:
                res.pop()
    print(res)