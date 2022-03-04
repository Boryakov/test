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
        
    if 2<= znak <= 16:  # Если система счислений 2-16 : 
        qwerty = znak16(number, znak)
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
    if znak>10:
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
    chislo = 0
    for i in range(len(arr)):
        chislo += arr[i]*znak**i
    return chislo

