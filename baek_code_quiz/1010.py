import sys
import math

T = int(sys.stdin.readline())
for i in range(T):
    n, m = map(int, sys.stdin.readline().split())
    result = math.ceil( (math.factorial(m) // math.factorial(m-n)) // math.factorial(n))
    print(result)

# math library의 factorial() method는 특정 숫자의 factorial 값을 return합니다.
# math.factorial(x) x는 숫자입니다.
#
# 전달받은 x의 팩토리얼 값을 return합니다.
#
# 팩토리얼 값을 계산하기 때문에 x는 양의 정수만을 받습니다.
#
# (실수, 음수 등을 전달하면 error가 발생합니다.)
#
# - math.factorial(5)
#
# 5!의 값을 계산하여 return합니다.
#
# 5! = 5 * 4 * 3 * 2 * 1 = 120 이므로 120이 return됩니다.