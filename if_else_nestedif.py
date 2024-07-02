x = 12
r = x % 2

if r == 0:
    print('even')
    if r > 5:
        print('great') #nested if
    else:
        print('not great')
else:
    print('odd')

x=5
if x==1:
    print("one")
elif x==2:
    print("two")
elif x==3:
    print('three')
else:
    print('not in range')