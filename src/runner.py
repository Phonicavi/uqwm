# -*- coding: utf-8 -*-
import traceback
from dataapiclient import Client
from privacy import token


if __name__ == "__main__":

    try:
        client = Client()
        client.init(token)

        # url1='/api/macro/getChinaDataGDP.csv?field=&indicID=M010000002&indicName=&beginDate=&endDate='
        # code, result = client.getData(url1)
        # if code==200:
        #     print result
        # else:
        #     print code
        #     print result
        #
        # url2='/api/subject/getThemesContent.csv?field=&themeID=&themeName=&isMain=1&themeSource='
        # code, result = client.getData(url2)
        # if(code==200):
        #     file_object = open('themes.csv', 'w')
        #     file_object.write(result)
        #     file_object.close()
        # else:
        #     print code
        #     print result
        #
        # url3='/api/market/getMktEqud.csv?field=&beginDate=&endDate=&secID=&ticker=&tradeDate=20160328'
        # code, result = client.getData(url3)
        # if code==200:
        #     file_object = open('mktequd20160328.csv', 'w')
        #     file_object.write(result)
        #     file_object.close()
        # else:
        #     print code
        #     print result

        url4='/api/market/getBarRTIntraDay.json?securityID=600050.XSHG&startTime=&endTime=&unit=1'
        # url4='/api/market/getBarRTIntraDayOneMinute.csv?time=11:20&exchangeCD=&unit=1'
        code, result = client.getData(url4)
        if code==200:
            file_object = open('oneminute20160330.csv', 'w')
            file_object.write(result)
            file_object.close()
        else:
            print code
            print result

    except Exception, e:
        traceback.print_exc()
        raise e