class A:
    def process(self):
        print("A.process")
        super().process()

class B:
    def process(self):
        print("B.process")
        super().process()

class C:
    def process(self):
        print("C.process")

class D(A, B, C):
    def process(self):
        print("D.process")
        super().process()

d = D()
d.process()