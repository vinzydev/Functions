x = 50

def func():
    global x
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func()
print('x is still', x)

def say(message,time=1):
    print(message*time)
say('Vinay')
say('pyappa\t',4)