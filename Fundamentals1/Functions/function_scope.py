# Scope
# In Python we have function scope, which prohibits us from accessing
# variables created inside of a function from outside of that function
def func():
    x = 5
    return x

func() # 5
x # NameError
