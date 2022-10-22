def EX1_1(a):
    return a+1

def EX1_2(base,height):
    return (base*height)/2

def EX1_3 (side1,side2):
    return (side1+side2)

def EX1_4 (day):
    if day==1:
        return 'Monday'
    if day==2:
        return 'Tuesday'
    if day==3:
        return 'Wednesday'
    if day==4:
        return 'Thursday'
    if day==5:
        return 'Friday'
    if day==6:
        return 'Saterday'
    if day==7:
        return 'Sunday'

    return 'Error'

def EX1_5 (a):
    if a <= 1:
        return 'infant'
    if a < 13:
        return 'child'
    if a <20 :
        return 'teenager'
    if a >=20:
        return 'adult'

    
def EX1_6 (a):
    if a==1:
        return 'I'
    if a==2:
        return 'II'
    if a==3:
        return 'III'
    if a==4:
        return 'IV'
    if a==5:
        return 'V'
    if a==6:
        return 'VI'
    if a==7:
        return 'VII'
    if a==8:
        return 'VIII'
    if a==9:
        return 'IX'
    if a==10:
        return 'X'
    return 'Error'

#example

print(EX1_1(2))
print(EX1_2(2,4))
print(EX1_3(2,4))
print(EX1_4(5))
print(EX1_5(17))
print(EX1_6(9))
    
