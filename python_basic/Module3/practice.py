# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」

max = 100
min = 1
ansre = 76

while 1:    
    if data == ansre:
        print("恭喜中獎")
        break
    elif (data > ansre) and (data < max):
        print("請輸入更小的數字")
        max = data
        data = int(input(f"猜數字！{min}~{data}:\n"))
    elif (data < ansre) and (data > min):
        print("請輸入更大的數字")
        min = data
        data = int(input(f"猜數字！{data}~{max}:\n"))
    else:
        print("請注意範圍！")
        data = int(input(f"猜數字！{min}~{max}:\n"))










