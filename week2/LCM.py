from GCD import gcdIMP

def lcm(a, b):
  gcd = gcdIMP(a, b)
  return (a*b)/gcd

def lcm_tester():
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter a second number: "))
  print("LCM: ", lcm(num1,num2))