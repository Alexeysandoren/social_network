# x = [[]]*3

# x[0].append('a')
# x[1].append('b')
# x[2].append('c')
# x[0]=['d']
# print(x)


# a = [1, 3, 7, 8, 11]
# thr = 0
# a = filter(lambda a: (thr, a)[a < thr], a)
# print(max(a))

# s = '\nAlice\n'
# print(s.lstrip())
def h():
    try:
        1/0
    except ZeroDivisionError:
        print('error')
        raise
    finally:
        print('ff')

print(h())