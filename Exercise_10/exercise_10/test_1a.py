from example import foo
from exercise_1a import execution_tree

def test_tree():
    c = 0
    t = 0
    for x in range(-2, 4):
        for y in range(-2, 4):
            for z in range(-2, 4):
                try:
                    a, b = foo(x, y, z)
                    t += 1
                    values = execution_tree.evaluate({'x': x, 'y': y, 'z': z})
                    if a == values['a'] and b == values['b']:
                        c += 1
                except:
                    pass
    return c, t

if __name__ == '__main__':
    c, t = test_tree()
    print(f'PASSED {c} of {t} tests')