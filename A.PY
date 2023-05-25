class D:
    def method_a(self):
        self.a=10


class E:
    def method_b(self):
        self.b=12


class C(D,E):
    def addition(self):
        print(self.a+self.b)


ob=C()
ob.method_a()
ob.method_b()
ob.addition()