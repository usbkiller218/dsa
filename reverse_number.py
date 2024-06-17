#first method
def reverse(x):
        tempx=abs(x)

        reverse_number=0 
        counter=0
        while tempx>0:
            temp=tempx%10
            tempx=tempx/10
            reverse_number=temp+(reverse_number*10)
            counter+=1
        if x>0:
            pass
        else:
            reverse_number=0-reverse_number
        
        maximium=(2**31)-1
        mimimumm=-(2**31)
        if maximium>reverse_number>mimimumm:
            return reverse_number


        return 0
#second method
def reverse_number2(number):
    if number>0:
        sign=1
    else:
        number=-number
        sign=-1

    reverse_number=int(str(number)[::-1])
    maximium=(2**31)-1
    mimimumm=-(2**31)
    if maximium>reverse_number>mimimumm:
        return sign*(int(reverse_number))
    
    return 0
number=-2342524

x=reverse_number2(number)
print(x)







