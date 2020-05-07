def total(initial=5, *num, **keywords):
    count = initial
    for number in num:
        count += number
    for key in keywords:
        count += keywords[key]


print('total',total(10, 1, 2, 3, veg=50, fruits=100))
