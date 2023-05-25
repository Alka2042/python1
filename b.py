class A:
    def __init__(self):
        self.a=10
        self.b=20

class B(A):
    def addition(self):
        print(self.a+self.b)


class C(B):
    def sub(self):
        print(self.a-self.b)

ob=C()
ob.sub()