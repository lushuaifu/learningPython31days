try:
    print('try1......')
    try:
        print('try2......')
        num = 1 / 0
    except FileNotFoundError:
        print('except2......')
except:
    print('except1......')