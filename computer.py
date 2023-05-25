class computers:
    def specs(self,r,m):
        self.RAM=r
        self.models=m

ob=computers()
comp1=computers()
ob.specs("8GB","dell inspiron")
comp1.specs("4GB","hp pavillion")
print(ob.RAM)
print(comp1.RAM)