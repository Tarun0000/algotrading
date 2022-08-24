def invertedhammer(open,close,high,low,time):
    if abs(open[1]-close[1])*2<high[1]-max(open[1],close[1]) and open[0]<close[0]and clos[0]-open[1]>abs(open[1]-close[1])*2 and open[2]>close[2]:
        return time[1]
6