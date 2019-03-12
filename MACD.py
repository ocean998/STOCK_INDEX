import baostock as bs 
import pandas as pd 
import talib as ta 
import stock_base
 
 
def computeMACD(code, startdate, enddate): 
 
    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)
 
    # 获取股票日 K 线数据     
    rs = bs.query_history_k_data_plus("sz.300582","date,code,close,tradeStatus",
        start_date=startdate, end_date=enddate,frequency="d", adjustflag="3") 
    result_list = [] 

    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        result_list.append(rs.get_row_data())
        df = pd.DataFrame(result_list, columns=rs.fields)     
        # 剔除停盘数据   df['tradeStatus'] == '1' 交易
        df2 = df[df['tradeStatus'] == '1']
        # 获取 dif,dea,hist，它们的数据类似是 tuple，且跟 df2 的 date 日期一一对应     
        # 记住了 dif,dea,hist 前 33 个为 Nan，所以推荐用于计算的数据量一般为你所求 日期之间数据量的 3 倍     
        # 这里计算的 hist 就是 dif-dea,而很多证券商计算的 MACD=hist*2=(difdea)*2    
        dif, dea, hist = ta.MACD(df2['close'].astype(float).values, fastperiod=12, slowperiod=26, signalperiod=9)

        # macd计算结果 ，日期date是索引列，'dif', 'dea', 'macd' 分别是三个结果
        df3 = pd.DataFrame({'dif': dif[33:], 'dea': dea[33:], 'hist': hist[33:]},
                index=df2['date'][33:], columns=['dif', 'dea', 'hist'])
    # df3.plot(title='MACD')
    # plt.show() 

    # 寻找 MACD 金叉和死叉     
        datenumber = int(df3.shape[0])    
        print(1,' ~~~ 分隔符' * 4,'~~~ ')
        print(datenumber)
        print(2,' ~~~ 分隔符' * 4,'~~~ ')
        
        for i in range(datenumber - 1):
            if ((df3.iloc[i, 0] <= df3.iloc[i, 1]) & (df3.iloc[i + 1, 0] >= df3.iloc[i + 1, 1])):
                print("MACD 金叉的日期： " + df3.index[i + 1])
            if ((df3.iloc[i, 0] >= df3.iloc[i, 1]) & (df3.iloc[i + 1, 0] <= df3.iloc[i + 1, 1])):
                print("MACD 死叉的日期： " + df3.index[i + 1]) 

    bs.logout()
    return(dif, dea, macd) 
 
if __name__ == '__main__':
    df = stock_base.get_stock_code( 'D:\\0_stock_macd\\_月K线金叉.xls' )
    print( df )