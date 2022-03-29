from week2 import GCD

def lcm(a, b):
  gcd = GCD.gcdImp(a, b)
  return int((a*b)/gcd)

def lcm_tester():
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter a second number: "))
  print("LCM:", lcm(num1,num2))