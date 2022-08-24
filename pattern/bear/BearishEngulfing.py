def bearishengulfing(open,close,high,low):
    temp=max(open[0],close[0])
    o=open[0]
    c=close[0]
    flow=0
    eng=0
    for i in range(len(open)):
        if (o<=close[i] and c<open[i]) or (o<close[i] and c>=open[i]):
            print(i)
            return
        elif temp>=max(open[i],close[i]):
            temp=max(open[i],close[i])
        o=open[i]
        c=close[i]
    return 0
bearishengulfing(open,close,high,low)