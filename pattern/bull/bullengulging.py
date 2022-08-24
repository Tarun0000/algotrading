def bullengulfing(open,close,high,low,time):
    if len(open)<2:
        pass
    elif len(open)>5:
        if close[1]<open[1] and open[1]<close[0] and open[0]<=close[1]:
            temp=(open[1]+close[1])/2
            l=0
            for i in range(2,len(open)):
                if temp <= (open[i]+close[i])/2:
                    l=l+1
                    temp=(open[i]+close[i])/2
                else:
                    break
            if l>0:
                return time[0]
            else:
                return 0
    elif close[1]<open[1] and open[1]<close[0] and open[0]<=close[1]:
        return time[0]
    else:
        return


