weight = int(input("请输入你的体重:"))
height = int(input("请输入身高:"))
bmi = weight/(height*height)

print("你的bmi指数: %.2f%%" % (bmi*100))

if bmi >= 32:
    print("严重肥胖")
elif bmi >= 28:
    print("肥胖")
elif bmi >= 25:
    print("过重")
elif bmi >= 18.5:
    print("正常")
else:
    print("太轻啦!")