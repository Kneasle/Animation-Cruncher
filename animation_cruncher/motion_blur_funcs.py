# File for motion blur functions
import math

def MBConstant (x, n):
    return 1 / n

def MBLinear (x, n):
    x += 1
    
    if x > n / 2:
        x = n - x + 1

    if n % 2 == 0:
        total = n // 2 * (n // 2 + 1)
    else:
        mid = (n + 1) // 2
        
        total = mid + mid * (mid - 1)

    return x / total

def MBGaussian (x, n):
    n -= 1
    
    return math.factorial (n) / (math.factorial (x) * math.factorial (n - x) * 2 ** n)

def GetArray (func, n):
    return [func (i, n) for i in range (n)]


if __name__ == "__main__":
    print (GetArray (MBLinear, 4))
    print (GetArray (MBLinear, 5))
    print (GetArray (MBLinear, 6))
    print (GetArray (MBLinear, 7))
