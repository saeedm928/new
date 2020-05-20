class gen:
    def get(self,a,b):
        self.a=a
        self.b=b
    def fin(self):
        self.lis=[]
        for i in range(self.a,self.b+1):
            if i%7==0:
                self.lis.append(i)
        return self.lis
