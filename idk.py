
def znak16(namber, znaak):
    # перевод в 11 -  16-ную систему счислений 
    # namber- число которое будем переводить в другой разряд
    # znaak - ввести систему счислений
    qwerty = []  
    
    while namber != 0 : 
        if namber%znaak <= 9:
            qwerty.append(namber%znaak)
            namber //= znaak
        elif namber % znaak == 10:
            qwerty.append('A')
            namber //= znaak
        elif namber % znaak == 11:
            qwerty.append('B')
            namber //= znaak
        elif namber % znaak == 12:
            qwerty.append('C')
            namber //= znaak
        elif namber % znaak == 13:
            qwerty.append('D')
            namber //= znaak  
        elif namber % znaak == 14:
            qwerty.append('E')
            namber //= znaak
        elif namber % znaak == 15:
            qwerty.append('F')
            namber //= znaak
    qwerty.reverse()
    return qwerty

    
def full(number, znak, rtrn):
        # number- число которое будем переводить в другой разряд
        # znak- разряд, в который мы будем переводить
        # rtrn- если 'y' - возвращаем тип str, если что то другое - тип list
        
    if 2<= znak <= 16:  
        qwerty = znak16(number, znak)
        qwerty.insert(0, 0)
        if rtrn != 'y':
            while len(qwerty) <= 9:
                qwerty.insert(0, 0)
        if rtrn == 'y':
            str_qwerty = ''
            for i in range(len(qwerty)):
                str_qwerty += ''.join(str(qwerty[i]))
            return str_qwerty
        else:
            return qwerty
            
                     
    else :   # если система счислений не 2-16
        print('идите нахуй =(')


def naoborot(arr, znak):
    """ переводим из 2-10 значной в 10 значный """
    # arr - код , который будем переводить в число
    # znak - система счислений,в которую будем переводить
    arr = list(arr) # ожидаем от переменной тип 'list'
    arr.reverse()
    chislo = 0
    for i in range(len(arr)):
        chislo += int(arr[i])*znak**i
    return chislo


def frsttask():
   # 1 задание
   x = [451,111,764,245]
   N = 3
   while N < 6:
        print (N,'-чная система счислений:' )       
        for i in range(len(x)):
            print(full(x[i], N,'y'))
        print ('Перевод обратно:')    
        for i in range(len(x)):
            print(naoborot(full(x[i], N, 'y') , N) )
        N += 1     


def plus(arr1, arr2, znak):
    arr1=list(arr1)
    arr2=list(arr2)
    arr3 = []
    while len(arr1) <= len(arr2):
        arr1.insert(0, 0)
    while len(arr2) <= len(arr1):
        arr2.insert(0, 0)
    arr1.reverse()
    arr2.reverse()
    
    for i in range(len(arr1)):
        arr3.append((arr1[i] + arr2[i]))
        if (arr3[i]) >= znak:
            arr1[i+1] += 1
            arr3[i] %= znak
    arr3.reverse()
    return arr3


def umnoj(arr1, arr2, znak,rtrn):
    arr1=list(arr1)
    arr2=list(arr2)
    temp=[]
    for q in range(len(arr2)):
        test = []
        for i in range(arr2[q]):
            test=plus(test,arr1,znak)
        for r in range(len(arr2)-q-1):
            test.append(0)

        temp.append(test)
    temp.reverse()    
    array3=[]
    for i in range(len(temp)):
        array3=plus(array3,temp[i],znak)
    
        str_array3 = ''
        for i in range(len(array3)):
            str_array3 += ''.join(str(array3[i]))
       
    if rtrn=='y':
        return str_array3
    else:
        return array3
        
   


#frsttask()
sys=6
first_number=3022
second_number=3

array1=full(first_number,sys,'n')
array2=full(second_number,sys,'n')

array3=umnoj(array1,array2,sys,'n')
str_array3=umnoj(array1,array2,sys,'y')
print(str_array3)    
print(naoborot(array3,sys))
if first_number*second_number==naoborot(array3,sys):
    print('Подсчёт правильный')
else:
    print('Подсчёт неправильный')