#check_amstrong_number
def armstrong_number(number):
    number=153
    k=len(str(number))

    counter=0

    while number>0:
        tempx=number%10
        number=int(number/10)
        counter+=tempx**k
    return counter

    

