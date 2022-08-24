import datetime
def morningstar(open,close):
    #starting ka first wala  second  wale se check kare ka
    condition=open[0]<close[0] and max(open[1],close[1])<max(open[0],close[0]) and max(open[1],close[1])<max(open[2],close[2]) and open[2]>close[2] and 2*(close[1]-open[1])<=open[0]-close[0]
    if (open[0]>close[1] and close[1]>open[1] and open[2]>close[2] and close[2]>close[1]) or (condition):
        c=max(open[1],close[1])
        l=0
        # yahan par hum index 1 se slop nikaenge
        for i in range(2,len(open)):
            if c<=max(open[i],close[i]):
                l=l+1
            elif l>1:
                return "MorningStar"
            else:
                return 0
    return "morning star"

minu=datetime.datetime.today().minute
print(minu)


