from example import foo
from exercise_1d import x, y, z


def test_bug():
    try:
        foo(x, y, z)
    except AssertionError:
        return True
    else:
        return False
    

if __name__ == '__main__':
    if test_bug():
        print('Error found')
    else:
        print('Error not found')
