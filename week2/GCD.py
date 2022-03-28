def gcdImp(a,b):
    # return 0 for the GCD if one of the inputs is 0
    if a==0:
        return 0
    # return 0 for the GCD if one of the inputs is 0
    if b==0:
        return 0
    #  checking if the two inputs evenly divide
    if a % b ==0:
        return b
    if b % a ==0:
        return a
    # subtract smaller input from larger input. Replace larger value with difference and recursively call
    if a > b:
        return gcdImp(a-b,b)
    if b > a:
        return gcdImp(b-a,a)


def GCDImp_tester():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    print("GCD: ", gcdImp(num1,num2))

class GCD:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __call__(self):
        # return 0 for the GCD if one of the inputs is 0
        if self.a==0:
            return 0
        # return 0 for the GCD if one of the inputs is 0
        if self.b==0:
            return 0
        #  checking if the two inputs evenly divide
        if self.a % self.b ==0:
            return self.b
        if self.b % self.a ==0:
            return self.a
        # subtract smaller input from larger input. Replace larger value with difference and recursively call
        if self.a > self.b:
            self.a = self.a -self.b
            return self()
        if self.b > self.a:
            self.b = self.b - self.a
            return self()


def GCD_OOP_tester():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    GCD_instance = GCD(num1,num2)
    print("GCD: ", GCD_instance())

if __name__ == "__main__":
    GCD_OOP_tester()