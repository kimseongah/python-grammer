#내장함수
result = sum([1,2,3,4,5])
min_result = min(7,4,3,2)
max_result = max(7,3,4,2)
result = eval("(3+5)*7")

result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4], reverse=True)

array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key = lambda x: x[1], reverse=True)
#순열과 조합
from itertools import permutations
data = ['A','B','C']
result = list(permutations(data, 3)) #3개 나열하는 모든 순열

from itertools import combinations
result = list(combinations(data, 2)) #2개 뽑는 모든 조합

#중복 순열
from itertools import product
result = list(product(data, repeat=2))

#중복 조합
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2))


#Counter
from collections import Counter
counter = Counter(['red', 'blue', 'red','green','blue','blue'])
print(counter['blue'])
print(dict(counter))


#최대공약수와 최소공배수
import math
#최소공배수
def lcm(a, b):
    return a*b // math.gcd(a,b)
print(lcm(21, 14))
#최대공약수
print(math.gcd(21, 14))