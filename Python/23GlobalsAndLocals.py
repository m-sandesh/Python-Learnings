# Global vs Local Variable
# Defined by scopes

a = 10  # global


def useThis():
    a = 15  # local
    print("localFunc", a)


def changeGlobal():
    global a
    a = 11  # if 'global a' is not defined above, it will treat as local variable
    print('globalFunc', a)


def changeBoth():   # change global and local variable of same name within a scope
    globals()['a'] = 12
    a = 15
    print('GobalSameFunc', globals()['a'])
    print('LocalSameFunc', a)


print('Global Variable', a)
useThis()
changeGlobal()
changeBoth()
