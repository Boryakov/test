def addition(arr1, arr2, znak):
    arr1=list(arr1)
    arr2=list(arr2)
    arr3 = []
    while len(arr1) < len(arr2):
        arr1.insert(0, 0)
    while len(arr2) < len(arr1):
        arr2.insert(0, 0)
    arr1.reverse()
    arr2.reverse()
    
    for i in range(len(arr1)):
        arr3.append((arr1[i] + arr2[i]))
        if (arr3[i]) >= znak:
            arr1[i+1] += 1
            arr3[i] %= znak
    arr3.reverse()
    for i in range(len(arr3)):
        if arr3[0]==0:
            arr3.pop(0)
        else:
            break
    arr3.insert(0,0)
    return arr3

def multiply(arr1, arr2, znak,rtrn):
    arr1=list(arr1)
    arr2=list(arr2)
    temp=[]
    for q in range(len(arr2)):
        test = []
        for i in range(arr2[q]):
            test=addition(test,arr1,znak)
        for r in range(len(arr2)-q-1):
            test.append(0)

        temp.append(test)
    temp.reverse()    
    array3=[]
    for i in range(len(temp)):
        array3=addition(array3,temp[i],znak)
    for i in range(len(array3)):
        if array3[0]==0:
            array3.pop(0)
        else:
            break
    array3.insert(0,0)
       
    if rtrn=='y':
        str_array3 = ''
        for i in range(len(array3)):
            str_array3 += ''.join(str(array3[i]))
        return str_array3
    else:
        return array3

def substraction(arr1, arr2, znak,rtrn):
    arr1 = list(arr1) #Type of variable that we waiting
    arr2 = list(arr2) 
    
    arr3= [] 
    z = 0
    while len(arr1) < len(arr2):  #Doing the same lenght of arrays(digits)
        arr1.insert(0, 0)   
    while len(arr2) < len(arr1):  
        arr2.insert(0, 0)
    for i in range(len(arr1)):
        if arr1[i] > arr2[i]:
            break
        if arr1[i] < arr2[i]:
            arr1, arr2 = arr2, arr1
            z += 1
            break
    arr1.reverse()
    arr2.reverse()
    for q in range(len(arr1)):
        temp = arr1[q] - arr2[q]
        if temp < 0:
            temp += znak
            arr1[q+1] -= 1 
        arr3.append(temp)
    arr3.reverse()
    for i in range(len(arr3)):
        if arr3[0]==0:
            arr3.pop(0)
        else:
            break
    arr3.insert(0,0)
    
    if rtrn=='y':
        str_array3 = ''
        for i in range(len(arr3)):
            str_array3 += ''.join(str(arr3[i]))
        return str_array3
    
    else:
        return arr3
    
