import math

def solution(n):
    lcm = (n * 6) // math.gcd(n, 6) 
    answer = lcm // 6
    return answer
