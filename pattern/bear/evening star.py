def eveningstar(open,close):
    condition=open[0]>close[0] and open[0]-close[0]>2*open[1]-close[1] and min(open[0],close[0])<min(close[1],open[1]) and min(open[2],close[2])<min(close[1],open[1])
    if (open[0]<=close[1] and open[0]>close[0] and open[1]>close[1] and close[1]>=close[2] and close[2]>open[2])or(condition):
        m=max(open[2],close[2])
        l=0
        for i in range(3,len(open)):
            if max(open[i],close[i])<m:
                l=l+1
                m=max(open[i],close[i])
            elif l>1:
                print("morning star")
                return
            else:
                print("no morning star")
                return
        if l>1:
            print("moring star")