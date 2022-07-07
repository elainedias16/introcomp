year = int(input('Type a year:\n'))

def is_leap_year(year):
    if( year % 400 == 0 or (year % 4 == 0 and  year % 100!= 0) ):
       return True
    else:
        return False


if is_leap_year(year) ==  True :
    print('{} é um ano bissexto!' .format(year))
else:
    print('{} não é um ano bissexto!' .format(year))

