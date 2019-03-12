import macd_base as mb



if __name__ == "__main__":
    # 60 即将金叉
    macd_60 = mb.MACD_INDEX('60')
    macd_60.save_bing_golden('all', False)
