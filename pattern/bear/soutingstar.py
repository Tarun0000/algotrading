def soutingstar(open,high,low,close,time):
    if len(open)=2:
        if max(open[0],close[0])-high[0] > 2*abs(open[0]-close[0]) and min(open[0],close[0])>max(open[1],close[1]) and open[1]<close[1]:
            return time[0]
        else:
            return
    elif len(open)>2:
        f