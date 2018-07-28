# File for motion blur functions
import math

def MBLinear (x, n):
    return 1 / n

def MBGaussian (x, n):
    return math.factorial (n) / (math.factorial (x) * math.factorial (y) * 2 ** n)

def GetArray (func, n):
    return [func (i) for i in range (n)]
