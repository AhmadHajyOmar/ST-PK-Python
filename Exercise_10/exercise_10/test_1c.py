from exercise_1b import path_constraints
from exercise_1c import solutions

def test1(pc):
    return all([
        not pc.evaluate({'x': 3, 'y': 1, 'z': 1}),
        not pc.evaluate({'x': 3, 'y': 1, 'z': 0}),
        not pc.evaluate({'x': 3, 'y': 0, 'z': 1}),
        not pc.evaluate({'x': 3, 'y': 0, 'z': 0}),
        not pc.evaluate({'x': 2, 'y': 1, 'z': 1}),
        not pc.evaluate({'x': 2, 'y': 1, 'z': 0}),
        not pc.evaluate({'x': 2, 'y': 0, 'z': 1}),
        not pc.evaluate({'x': 2, 'y': 0, 'z': 0})
    ])


def test_solutions():
    c = 0
    for pc, s in zip(path_constraints, solutions):
        if test1(pc) if s is None else pc.evaluate(s):
            c += 1
        else:
            f'{s} is no solution for path constraint {pc}' 
    return c


if __name__ == '__main__':
    print(f'Passed {test_solutions()} of 6 tests')
