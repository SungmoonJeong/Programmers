import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    분자 = (denom1 * numer2) + (denom2 * numer1)
    분모 = (denom1 * denom2)
    최대공약수 = math.gcd(분모, 분자)
    answer = [분자 // 최대공약수, 분모 // 최대공약수]
    return answer