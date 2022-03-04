import Transfering as tr 
import Operations as op 

x1=67
x2=11
sys=16



y1=tr.full(x1,sys)
y2=tr.full(x2,sys)

z=op.addition(y1,y2,sys)
z1=op.multiply(y1,y2,sys)
print(z)
print(z1)

z11=tr.naoborot(z,sys)
z12=tr.naoborot(z1,sys)
print(z11)
print(z12)