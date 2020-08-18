import random
num = random.randint(1,2)
ans = input("請輸入數字:")
if ans == "1" or ans == "2" or ans == "3" or ans == "4" or ans == "5" :
    int(ans)
    if num == ans:
        print("答對")
    else:
        print("答錯")
elif ans == "6" or ans == "7" or ans == "8" or ans == "9" or ans == "10":
    int(ans)
    if num == ans:
        print("答對")
    else:
        print("答錯")
else:
    print("要輸1~10的數字")
