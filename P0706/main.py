'''
# 输入m和n，计算组合数C(m,n)的值
m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

fm = 1
fn = 1
fn_m = 1

for i in range(1, m+1):
    fm*=i
for i in range(1, n+1):
    fn*=i
for i in range(1,m-n+1):
    fn_m*=i

C = fm//fn//fn_m
print("The value of C(m,n) is:", C)
'''


'''
# 输入m和n，计算组合数C(m,n)的值
m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

fm = factorial(m)
fn = factorial(n)
fn_m = factorial(m-n)

print("The value of C(m,n) is:",fm//fn//fn_m)
'''


'''
# 设计一个生成随机验证码的函数，验证码由数字和英文大小写字母构成，长度可以通过参数设置。
import random

def generate_code(n = 4):
    # 小写字母
    lalp = [chr(i) for i in range(ord('a'), ord('z')+1)]
    # 大写字母
    salp = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    # 合并为所有字母
    alp = lalp + salp
    # 数字
    num = [str(i) for i in range(10)]
    
    # 随机生成n个字母
    anum = random.randint(0,n)
    # 剩余的数字个数
    nnum = n - anum

    # 随机生成验证码
    code = random.sample(alp,anum)
    code += random.sample(num,nnum)

    # 利用集合的无序性来打乱验证码
    set_code = set(code)
    # 输出打乱后的验证码
    for i in set_code:
        print(i, end='')


for i in range(5):
    generate_code(5)
    print()
'''