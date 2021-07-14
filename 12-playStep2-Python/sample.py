def turnintodigits(num):
    re=""
    if(num<=9):
        return num
    else:
        while(num!=0):
            rem = num%10
            re=re+str(rem)+","
            num=num//10
    return re

print(turnintodigits(154))