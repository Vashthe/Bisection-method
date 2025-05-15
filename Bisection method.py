import numexpr
import math

func = input("请输入函数：")
a = float(input("请输入a："))
b = float(input("请输入b："))
epsilon = float(input("请输入ε："))
count = 0

k = math.ceil((math.log10(b-a) - math.log10(epsilon))/math.log10(2))

fa = numexpr.evaluate(func.replace("x", str(a)))
fb = numexpr.evaluate(func.replace("x", str(b)))
if fa * fb >= 0:
    print("错误：f(a)和f(b)必须异号")
    exit()

while True:
    count += 1
    x = (a+b)/2
    fx = numexpr.evaluate(func.replace("x",str(x)))
    fa = numexpr.evaluate(func.replace("x",str(a)))
    if fx * fa < 0:
        b = x
    else:
        a = x
    if abs(b-a) < epsilon:
        break
print(f"预估迭代次数为：{k}")
print(f"方程的解的近似值为{x},迭代了{count}次")

