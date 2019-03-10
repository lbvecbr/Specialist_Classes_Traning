def foo(**kwargs):
    print(kwargs)


dict = {'a':1, 'b':2}
foo(**dict)