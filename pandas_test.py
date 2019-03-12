import pandas as pd
import os  


def get_stock_code(market='sz'):
     
    d = os.path.dirname(__file__)  #返回当前文件所在的目录    
    sh = d+'\上海股票代码.txt'
    sz = d+'\深圳股市代码.txt'
    if market == 'sz':
        f = open(sz,'r',encoding="utf8")
    if market == 'sh':
        f = open(sh,'r',encoding="utf8")
 
    code = []
    name = []
    # open("filename",'w',encoding="utf8")
    for line in f.readlines():
        x = line.split('(')[1]
        y = line.split('(')[0]
        code.append(x.split(')')[0])
        name.append(y)

    data = {'stock_code':code, 'stock_name':name}
    return pd.DataFrame(data, columns=['stock_code', 'stock_name'])

if __name__ == "__main__":
    df = get_stock_code('sz')
    print(df)

    for x in range(1,9):
        print(-x)