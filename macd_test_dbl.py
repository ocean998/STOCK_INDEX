import baostock as bs
import pandas as pd
import numpy as np
import macd_base as mb


if __name__ == '__main__':
    df_rst = pd.DataFrame( columns=('指标类别', '股票代码', '即将金叉日期', '快线强弱', '首次金叉时间', '大陆代码') )
    macd_60 = mb.MACD_INDEX( '60' )
    if macd_60.jb == 'm':
        pre = '月K线 即将底背离'
    if macd_60.jb == 'd':
        pre = '日K线 即将底背离'
    if macd_60.jb == 'w':
        pre = '周K线 即将底背离'
    if macd_60.jb == '60':
        pre = '60分钟K线 即将底背离'
    if macd_60.jb == '15':
        pre = '15分钟K线 即将底背离'

    macd_60.save_name = 'D:\\0_stock_macd\\'+'_'+pre+'.xls'

    code = macd_60.get_index( 'sz.000005' )
    df2 = macd_60.get_MACD( code )
    rst = macd_60.analyze_bottom( df2, True )
    if len( rst ) > 3:
        df_rst.loc[ 1 ] = rst

    print( '\n \t\t', '完成！\n' )
    df_rst.to_excel( macd_60.save_name, sheet_name='将要底背离' )