import baostock as bs
import pandas as pd
import numpy as np
import talib as ta
import stock_base


def get_index(code, jb, begin, end):
    '''
            根据周期初始化 开始时间，结束时间，获取远程指标数据
        '''
    # 要获取的指标数据列表
    # d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据
    if jb in ['d','w','m']:
        index_name = "date,close,volume,amount,turn"
    else:
        index_name = "date,time,close,volume,amount"
    rs = bs.query_history_k_data_plus(
        code,index_name,start_date=begin,end_date=end,
        frequency=jb,
        adjustflag="3")  
    # 复权状态(1：后复权， 2：前复权，3：不复权） 
    print('query_history_k_data_plus respond error_code:' + rs.error_code)
    print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)
    
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())

    result = pd.DataFrame(
        data_list, columns=rs.fields).sort_values(
            by='date', ascending=True)

    return result

if __name__ == "__main__":

    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' , lg.error_code)
    print('login respond  error_msg:' , lg.error_msg)
    date = stock_base.get_start_time('60')
    print(date)
    index = get_index('sz.000725', '60', date[0], date[1])
    lg = bs.logout()
    print('login respond error_code:' , lg.error_code)
    print('login respond  error_msg:' , lg.error_msg)
    print(index)
    # for x in range(0,len(index))
    #     print(index)