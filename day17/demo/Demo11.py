
def fun(*args):
    print(args)

fun(1)
fun(1,2)


def fun(**kwargs):
    print(kwargs)

fun(a=1,b='a')
fun()
