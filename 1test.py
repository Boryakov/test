

from Tasks import naoborot
import Transfering as tr 
import Operations as op 

x1=67

sys=2
x=tr.full(x1,sys,1)
f=tr.f2to16(x)
print(x)
print(f)
print(tr.naoborot(f,16))

