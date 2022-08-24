from main import api
import datetime
import timeit
import logging
import pandas as pd
import json
import talib as t
import json
import  matplotlib.pyplot as plt
from datetime import timedelta
from datacheck import datacheck
#end = datetime.datetime.today()-
#end = end.replace(hour=0, minute=0, second=0, microsecond=0)
lastBusDay = datetime.datetime.today()
lastBusDay = lastBusDay.replace(hour=0, minute=0, second=0, microsecond=0)
eq_name={'ADANI PORT & SEZ LTD': '15083', 'APOLLO HOSPITALS ENTER. L': '157', 'ASIAN PAINTS LIMITED': '236', 'AXIS BANK LIMITED': '5900', 'BAJAJ AUTO LIMITED': '16669', 'BAJAJ FINANCE LIMITED': '317', 'BAJAJ FINSERV LTD.': '16675', 'BHARAT PETROLEUM CORP  LT': '526', 'BHARTI AIRTEL LIMITED': '10604', 'BRITANNIA INDUSTRIES LTD': '547', 'UNSEC RED NCD 5.50%': '5066', 'CIPLA LTD': '694', 'COAL INDIA LTD': '20374', 'DIVI S LABORATORIES LTD': '10940', 'DR. REDDY S LABORATORIES': '881', 'EICHER MOTORS LTD': '910', 'GRASIM INDUSTRIES LTD': '1232', 'HCL TECHNOLOGIES LTD': '7229', 'HDFC BANK LTD': '1333', 'HDFC LIFE INS CO LTD': '467', 'HERO MOTOCORP LIMITED': '1348', 'HINDALCO  INDUSTRIES  LTD': '1363', 'HINDUSTAN UNILEVER LTD.': '1394', 'HDFCAMC - HDFCSENETF': '11593', 'HDFCAMC - HDFCNIFETF': '11591', 'HDFCAMC - HDFCNIF100': '10633', 'HDFCAMC - HDFCNEXT50': '10619', 'HDFC GOLD ETF': '19543', 'HDFC AMC LIMITED': '4244', 'HDFC LTD': '1330', 'HOUSING DVPT FIN CORP LTD': '22326', 'ICICIPRAMC - ICICIBANKP': '11386', 'ICICIPRAMC - IPRU5008': '11037', 'ICICI BANK LTD.': '4963', 'ITC LTD': '1660', 'INDUSIND BANK LIMITED': '5258', 'INFOSYS LIMITED': '1594', 'JSW STEEL LIMITED': '11723', 'KOTAK MAHINDRA BANK LTD': '1922', 'L&T TECHNOLOGY SER. LTD.': '18564', 'L&T INFOTECH LIMITED': '17818', 'NIP IND ETF LONGTERM GILT': '17700', 'LARSEN & TOUBRO LTD.': '11483', 'M&M FIN. SERVICES LTD': '13285', 'MAHINDRA & MAHINDRA LTD': '2031', 'UNSECURED NCD': '20050', '9.00% UNSECURED NCD': '20048', '8.72% UNSECURED NCD': '20046', 'MARUTI SUZUKI INDIA LTD.': '10999', 'NTPC LTD': '11630', 'TFB 7.62% 2035 SR. 3B': '10751', 'TFB 7.53% 2030 SR. 2B': '10749', 'TFB 7.36% 2025 SR. 1B': '10746', 'TFB 7.37% 2035 SR. 3A': '10744', 'TFB 7.28% 2030 SR. 2A': '10741', 'TFB 7.11% 2025 SR. 1A': '10737', '8.49% SEC NON-CUM RED NCD': '7377', '8.91%S-R-NCD SERIES 3B': '31768', '8.73%S-R-NCD SERIES 2B': '31766', '8.66%S-R-NCD SERIES 1B': '31764', '8.66%S-R-NCD SERIES 3A': '31762', '8.48%S-R-NCD SERIES 2A': '31760', '8.41%S-R-NCD SERIES 1A': '31758', 'NESTLE INDIA LIMITED': '17963', 'OIL AND NATURAL GAS CORP.': '2475', 'POWER GRID CORP. LTD.': '14977', 'RELIANCE INDUSTRIES LTD': '2885', 'SBI LIFE INSURANCE CO LTD': '21808', 'SHREE CEMENT LIMITED': '3103', 'TATA CONSULTANCY SERV LT': '11536', 'TATA CONSUMER PRODUCT LTD': '3432', 'TATA MOTORS LIMITED': '3456', 'TATA STEEL LIMITED': '3499', 'TECH MAHINDRA LIMITED': '13538', 'TITAN COMPANY LIMITED': '3506', 'UPL LIMITED': '11287', 'ULTRATECH CEMENT LIMITED': '11532', 'WIPRO LTD': '3787'}
#eq_name={'cipla':'694'}
#print(datetime.datetime.today())
while(True):
    minu = datetime.datetime.today().minute
    if int(minu)%5==0:
        complete_list=[]
        for eq in eq_name:
            ret1 = api.get_time_price_series(exchange='NSE', token=eq_name[eq], starttime=lastBusDay.timestamp(),interval=5)
            data=pd.DataFrame(ret1)
            data.drop(['intoi','intvwap','v','oi','intv','stat'],axis=1,inplace=True)
            datacheck(eq,data)
            l=datacheck(eq,data)
            complete_list.append(l)

        file_name=str(datetime.datetime.today().hour)+str(datetime.datetime.today().minute)
        file_name=file_name+"-"+str(datetime.time().hour)
        file_data=json.dumps(complete_list,indent=4)
        w=open(file_name+'.json','w')
        w.write(file_data)
