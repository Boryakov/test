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

def full(number, znak):
        # number- число которое будем переводить в другой разряд
        # znak- разряд, в который мы будем переводить
        # rtrn- если 'y' - возвращаем тип str, если что то другое - тип list
        
    if 2<= znak <= 16:  # Если система счислений 2-16 : 
        qwerty = znak16(number, znak)
        qwerty.insert(0, 0) 
        return qwerty           
    else :   # если система счислений не 2-16
        print('идите нахуй =(')

def naoborot(arr, znak):
    """ переводим из 2-10 значной в 10 значный """
    # arr - код , который будем переводить в число
    # znak - система счислений,в которую будем переводить
    arr = list(arr) # ожидаем от переменной тип 'list'
    arr.reverse()
    if znak>10:
        fromto(arr)

    chislo = 0
    for i in range(len(arr)):
        chislo += arr[i]*znak**i
    return chislo

def f2to8(arr):
    arr = list(arr)
    if len(arr) >= 4:
        while len(arr)%3 != 1 :
            arr.insert(0, 0)
    else :
        while(len(arr)) != 4:
            arr.insert(0, 0)
    arr.reverse()
    arr2 = []
    arr3 = []
    arr_r = []
    for i in range(len(arr) // 3):
        for q in range(3):
            arr2.insert(0, arr[q+i*3])
        arr3.insert(0, arr2)
        arr2 = []
    for i in range(len(arr3)):
        if arr3[i]==[0, 0, 0]:
            arr_r.insert(0, 0)
        elif arr3[i]==[0, 0, 1]:
            arr_r.insert(0, 1)    
        elif arr3[i]==[0, 1, 0]:
            arr_r.insert(0, 2)    
        elif arr3[i]==[0, 1, 1]:
            arr_r.insert(0, 3)    
        elif arr3[i]==[1, 0, 0]:
            arr_r.insert(0, 4)    
        elif arr3[i]==[1, 0, 1]:
            arr_r.insert(0, 5)    
        elif arr3[i]==[1, 1, 0]:
            arr_r.insert(0, 6)    
        elif arr3[i]==[1, 1, 1]:
            arr_r.insert(0, 7)
    arr_r.reverse()
    arr_r.insert(0, 0)
    
    return arr_r   

def f2to16(arr):
    arr = list(arr)
    if len(arr) >= 5:
        while len(arr)%4 != 1 :
            arr.insert(0, 0)
    else :
        while(len(arr)) != 4:
            arr.insert(0, 0)
    arr.reverse()
    arr2 = []
    arr3 = []
    arr_r = []
    for i in range(len(arr) // 4):
        for q in range(4):
            arr2.insert(0, arr[q+i*4])
        arr3.insert(0, arr2)
        arr2 = []
    for i in range(len(arr3)):
        if arr3[i]==[0, 0, 0, 0]:
            arr_r.insert(0, 0)
        elif arr3[i]==[0, 0, 0, 1]:
            arr_r.insert(0, 1)    
        elif arr3[i]==[0, 0, 1, 0]:
            arr_r.insert(0, 2)    
        elif arr3[i]==[0, 0, 1, 1]:
            arr_r.insert(0, 3)    
        elif arr3[i]==[0, 1, 0, 0]:
            arr_r.insert(0, 4)    
        elif arr3[i]==[0, 1 ,0, 1]:
            arr_r.insert(0, 5)    
        elif arr3[i]==[0, 1, 1, 0]:
            arr_r.insert(0, 6)    
        elif arr3[i]==[0, 1, 1, 1]:
            arr_r.insert(0, 7)
        if arr3[i]==[1, 0, 0, 0]:
            arr_r.insert(0, 8)
        elif arr3[i]==[1, 0, 0, 1]:
            arr_r.insert(0, 9)    
        elif arr3[i]==[1, 0, 1, 0]:
            arr_r.insert(0, 'A')    
        elif arr3[i]==[1, 0, 1, 1]:
            arr_r.insert(0, 'B')    
        elif arr3[i]==[1, 1, 0, 0]:
            arr_r.insert(0, 'C')    
        elif arr3[i]==[1, 1, 0, 1]:
            arr_r.insert(0, 'D')    
        elif arr3[i]==[1, 1, 1, 0]:
            arr_r.insert(0, 'E')    
        elif arr3[i]==[1, 1, 1, 1]:
            arr_r.insert(0, 'F')
    arr_r.reverse()
    arr_r.insert(0, 0)
    
    return arr_r   

def ListToStr(arr):
    str_array = ''
    for i in range(len(arr)):
        str_array += ''.join(str(arr[i]))
    return str_array

def fromto(arr):
    for i in range(len(arr)):
        if type(arr[i])==str:
            if arr[i]=='A':
                arr[i]=10
            elif arr[i]=='B':
                arr[i]=11
            elif arr[i]=='C':
                arr[i]=12
            elif arr[i]=='D':
                arr[i]=13
            elif arr[i]=='E':
                arr[i]=14
            elif arr[i]=='F':
                arr[i]=15