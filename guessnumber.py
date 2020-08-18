import random
num = random.randint(1,20)
i = 0
while i<5:
        ans = input("請輸入數字:")
        ans = int(ans)
        if num == ans:
            print("答對")
            break
        else:
            print("答錯")
            if int(ans)>int(num):
                print("too big")
            else:
                print("too small")
        if num == ans:
            print("答對")
            break
        else:
            print("答錯")
            if int(ans) > int(num):
                print("too big")
            else:
                print("too small")
    
        if num == ans:
            print("答對")
            break
        else:
            print("答錯")
            if int(ans)>int(num):
                print("too big")
            else:
                print("too small")
        if num == ans:
            print("答對")
            break
        else:
            print("答錯")
            if int(ans)>int(num):
                print("too big")
            else:
                print("too small")
        i = i+1
    