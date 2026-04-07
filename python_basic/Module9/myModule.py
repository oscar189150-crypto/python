# 計算幾次方
def pow(x, y):
    return x ** y

def disc(orgin):
    if orgin >= 2000:
        orgin = orgin-(200*(orgin//2000))
    return(orgin)



# 簡單斷句




print("myMoudule 的 __name__:")
print(__name__)
# 測試模組
if __name__ == "__main__":# 在函式庫寫測試必備
    print(f"myModule.py - funtion pow的結果： {pow(2, 3)}")
    print(f"myModule.py - funtion disc的結果： {disc(6000)}")

