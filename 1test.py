from numpy import multiply
import Transfering as tr 
import Operations as op 

x1=41444
y1=22311

sys=3
x=tr.full(x1,sys,'n')
y=tr.full(y1,sys,'n')

z=op.multiply(x,y,sys,'n')
print(tr.naoborot(z,sys)==x1*y1)

