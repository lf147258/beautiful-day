import random
a=random.randint(0,9)
print("请输入一个0到9的数字：\n")
b=int(input())
print(b)
x=2
if x > 0:
    while a != b:
        
        if a > b:
            print("小了\n","还有{0}次机会".format(x))
            b = int(input('请再次输入数字:'))
        elif a <b:
            print("大了\n","还有{}次机会".format(x))
            b = int(input('请再次输入数字:'))
        x=x-1
    else:
        print("恭喜你答对了")
