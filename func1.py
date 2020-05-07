def get_max(a,b):
    if a > b:
        print('a is greater than b')
    elif a < b:
        print('b is greater than a')
    else:
        print('Both are same')
#Pass literal values
get_max(5,5)

x=8
y=7
#pass variables as args
get_max(x,y)