import baostock as bs
import pandas as pd
import numpy as np
import macd_base as mb


if __name__ == '__main__':
    macd_d = mb.MACD_INDEX('60', '2019-03-06')

    df = macd_d.get_index('sz.000416')
    df.drop(df.index[[70,71]], inplace=True)
    print(df)
    print('\n k线 获取完成，如上\n')
    df2 = macd_d.get_MACD(df)
    print(df2)
    print('\n MACD 打印完成，如上\n')

    dead_macd = macd_d.analyze_dead(df2, True)
    print(dead_macd)
    print('\n死叉结果打印完成，如上')
    print('\n\t 执行 macd_d.analyze_bing_golden\n')
    df3 = macd_d.analyze_bing_golden( df2, True )

    print(df3)

    #### 登陆系统 ####
    # lg = bs.login()
    # # 显示登陆返回信息
    # print('login respond error_code:' + lg.error_code)
    # print('login respond  error_msg:' + lg.error_msg)
    #
    # #### 获取沪深A股历史K线数据 ####
    # # 详细指标参数，参见“历史行情指标参数”章节
    # rs = bs.query_history_k_data_plus("sz.000416",
    #                                   "time,code,open,high,low,close,volume,amount",
    #                                   start_date='2018-12-01', end_date='2019-03-12',
    #                                   frequency="60" )
    # print('query_history_k_data_plus respond error_code:' + rs.error_code)
    # print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)
    #
    # #### 打印结果集 ####
    # data_list = []
    # while (rs.error_code == '0') & rs.next():
    #     # 获取一条记录，将记录合并在一起
    #     data_list.append(rs.get_row_data())
    # result = pd.DataFrame(data_list, columns=rs.fields)
    #
    # #### 结果集输出到csv文件 ####
    # # result.to_csv("D:\\history_A_stock_k_data.csv", index=False)
    #
    # print(result)
    # result.drop(result.index[[250]], inplace=True)
    # result.drop(result.index[[250]], inplace=True)
    # # result.drop(result.index[[250]], inplace=True)
    # print(result)
    # #### 登出系统 ####
    # bs.logout()