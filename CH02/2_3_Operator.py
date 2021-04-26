"""
날짜: 2021/04/26
이름: 김민우
내용: 파이썬 변수외 자료형 교제 p.38
"""

# 대입연산자
a=1
b=c=d=0
e, f, g = 7, True, 'Apple'

print('a:', a)
print('c:', c)
print('f:', f)
print('g:', g)


# 산술연산자
num1=1
num2=2
num3, num4= 3,4

r1= num1 + num2
r2= num1 - num2
r3= num2 * num3
r4= num4 / num2
r5= num4 // num2
r6= num4 % num3
r7= num4 ** num2    #거듭제곱



print('r1:',r1)
print('r2:',r2)
print('r3:',r3)
print('r4:',r4)
print('r5:',r5)
print('r6:',r6)
print('r7:',r7)



# 복합대입연산자
num5, num6, num7, num8 = 5, 6, 7, 8

num5 += 1        #num5 = num5 + 1
num6 -= 2        #num6 = num6 - 2
num7 *= 3        #num7 = num7 * 3
num8 /= 4        #num8 = num8 / 4

print('num5:', num5)
print('num6:', num6)
print('num7:', num7)
print('num8:', num8)


# 비교연산자
var1 = 1       #var1: 변수(variable),   1: 자료(data)   ->processing(연산) 하기 위해 변수에 자료를 담음.
var2 = 2

rs1 = var1 > var2   # var1이 var2보다 크다.
rs2 = var1 < var2   # var1이 var2보다 작다.
rs3 = var1 >= var2  # var1이 var2보다 크거나 같다.
rs4 = var1 <= var2  # var1이 var2보다 작거나 같다.
rs5 = var1 == var2  # var1과 var2는 서로 같다.
rs6 = var1 != var2  # var1과 var2는 서로 다르다.

print('rs1:', rs1)
print('rs2:', rs2)
print('rs3:', rs3)
print('rs4:', rs4)
print('rs5:', rs5)
print('rs6:', rs6)


# 논리연산자
var3 = 3
var4 = 4

res1 = (var3 > 2) and (var4 > 3)    # true  true, 둘 다 true이므로 res1은 true, 둘 중 하나라도 false면 res1은 false.
res2 = (var3 > 2) and (var4 > 4)    # true  false, 하나가 false이므로 res1은 false
res3 = (var3 > 2) or (var4 > 4)     # true  false, 둘 중 하나가 true이므로 res1은 true
res4 = not (var3 > var4)            # not: 부정, var3은 var4보다 크지 않다. -> var3은 var4보다 크지 않으므로 true

print('res1:', res1)
print('res2:', res2)
print('res3:', res3)
print('res4:', res4)