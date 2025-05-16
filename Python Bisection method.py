import math
import sympy


# 用户输入部分
func = input("请输入函数：")  # 例如输入 "x**2 - 2"
a = float(input("请输入a："))
b = float(input("请输入b："))
epsilon = float(input("请输入截断误差ε："))  # 例如输入 1e-6
N = int(input("请输入迭代次数N："))  # 例如输入 100

x_value = a
k_estimate = math.ceil((math.log10(b-a) - math.log10(epsilon))/math.log10(2))
k = 0

x = sympy.symbols("x")
expr_1 = sympy.sympify(func)

fa = expr_1.subs(x, a).evalf()
fb = expr_1.subs(x, b).evalf()
if fa * fb >= 0:
    print("错误：f(a)和f(b)必须异号")
    exit()

while k < N:
    k += 1
    x_value = (a+b)/2
    fx = expr_1.subs(x, x_value).evalf()
    fa = expr_1.subs(x, a).evalf()
    if fx * fa < 0:
        b = x_value
    else:
        a = x_value
    if abs(b-a) < epsilon:
        break
print(f"预估迭代次数为：{k_estimate}")
print(f"方程的解的近似值为{x_value},迭代了{k}次")

