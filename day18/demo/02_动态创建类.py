def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo  # 返回的是类，不是类的实例
    else:
        class Bar(object):
            pass
    return Bar

obj = choose_class('foo')
print(obj)

obj = choose_class('xx')
print(obj)