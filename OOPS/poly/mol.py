class calc:

    def add(self, a, b=0, c=0):
        print(a + b + c)


obj = calc()

obj.add(10)
obj.add(10, 40)
obj.add(10, 20, 40)