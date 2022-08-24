from NorenRestApiPy.NorenApi import  NorenApi



class ShoonyaApiPy(NorenApi):
    def __init__(self):
        NorenApi.__init__(self, host='https://shoonyatrade.finvasia.com/NorenWClientTP/', websocket='wss://shoonyatrade.finvasia.com/NorenWSTP/', eodhost='https://shoonya.finvasia.com/chartApi/getdata/')
        global api
        api = self




# enable dbug to see request and responses
#logging.basicConfig(level=logging.DEBUG)

# start of our program
api = ShoonyaApiPy()
uid="FA64119"
pwd="Tarun@3684"
vc="FA64119_U"
imei="abc1234"
app_key="58685a7b53cd6b8753fffaf18c79d526"
factor2="MXLPS1309G"

ret = api.login(userid=uid, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)
print("login Done")