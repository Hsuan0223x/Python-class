import math

# 讀取使用者輸入的四個數字
x1, y1 = map(float, input("請輸入點1的座標 (x1 y1): ").split())
x2, y2 = map(float, input("請輸入點2的座標 (x2 y2): ").split())

# 計算兩點的歐式距離
distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# 輸出結果並格式化到小數點後四位
print(f"兩點之間的歐式距離為: {distance:.4f}")
