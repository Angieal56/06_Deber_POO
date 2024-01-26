class A:
    def hablar(self):
        print("Hola desde A")
        
class H(A):
    def hablar(self):
        print("Hola desde H")


class B(A): 
    pass
        
class C(H):
    pass
        
class D(B,C): 
        pass
       
d = D()
d.hablar()

print(D.mro())

H.hablar(d)