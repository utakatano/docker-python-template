# 入力を得てインチをセンチメートルに変換
# 変換の元になる値
per_inch = 2.54

# ユーザーから入力を得る
user = input("inch? ")

# 浮動小数点型に変換
inch = float(user)

# 計算
cm = inch * per_inch

# 結果を表示
desc = "{0}inch = {1}cm".format(inch , cm)

print(desc)