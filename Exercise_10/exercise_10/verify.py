import os
import inspect

PRINT_FORMAT = '{:<40}{}'
CORRECT_STATE = 'PASS'
WRONG_STATE = 'FAIL'

files_to_verify = [
    os.path.join('exercise_1a.py'),
    os.path.join('exercise_1b.py'),
    os.path.join('exercise_1c.py'),
    os.path.join('exercise_1d.py'),
    os.path.join('test_1a.py'),
    os.path.join('test_1c.py'),
    os.path.join('test_1d.py'),
    os.path.join('example.py'),
    os.path.join('tree.py'),
    # path to file    
]

variables_to_verify = [
    ('exercise_1a', 'execution_tree'),
    ('exercise_1b', 'path_constraints'),
    ('exercise_1c', 'solutions'),
    ('exercise_1d', 'x'),
    ('exercise_1d', 'y'),
    ('exercise_1d', 'z'),
    ('tree', 'Condition'),
    ('tree', 'Var'),
    ('tree', 'Const'),
    ('tree', 'Op'),
    ('tree', 'Eq'),
    ('tree', 'Lt'),
    ('tree', 'Le'),
    ('tree', 'Gt'),
    ('tree', 'Ge'),
    ('tree', 'Not'),
    ('tree', 'And'),
    ('tree', 'Or'),
    ('tree', 'Node'),
] + [('exercise_1b', f'path_constraint_{i}') for i in range(1, 7)] + [('exercise_1c', f'solution_{i}') for i in range(1, 7)]

functions_to_verify = [
    ('example', 'foo', 3),
    ('test_1a', 'test_tree', 0),
    ('test_1c', 'test1', 1),
    ('test_1c', 'test_solutions', 0),
    ('test_1d', 'test_bug', 0),
]

def verify_files():
    missing_files = list()
    for path in files_to_verify:
        if os.path.exists(path):
            state = CORRECT_STATE
        else:
            missing_files.append(path)
            state = WRONG_STATE
        print(PRINT_FORMAT.format(path, state))
    print()
    return missing_files

def verify_variables():
    missing_variables = list()
    current_package = None
    for package, variable in variables_to_verify:
        if current_package is None or current_package.__name__ != package:
            current_package = __import__(package)
        varaible_repr = f'{package}.{variable}'
        if variable in dir(current_package):
            state = CORRECT_STATE
        else:
            missing_variables.append(varaible_repr)
            state = WRONG_STATE
        print(PRINT_FORMAT.format(varaible_repr, state))
    print()
    return missing_variables

def verify_functions():
    missing_functions = list()
    wrong_functions = list()
    current_package = None
    for package, function, args in functions_to_verify:
        if current_package is None or current_package.__name__ != package:
            current_package = __import__(package)
        function_repr = f'{package}.{function}'
        if function in dir(current_package):
            specs = inspect.getfullargspec(getattr(current_package, function))
            if len(specs[0]) == args:
                state = CORRECT_STATE
            else:
                wrong_functions.append(function_repr)
                state = WRONG_STATE
        else:
            missing_functions.append(function_repr)
            state = WRONG_STATE
        print(PRINT_FORMAT.format(function_repr, state))
    print()
    return missing_functions, wrong_functions

class VerificationError(ValueError):
    pass

if __name__ == '__main__':
    missing_files = verify_files()
    missing_variables = verify_variables()
    missing_functions, wrong_functions = verify_functions()
    for l, m in [(missing_files, 'Missing file'), (missing_variables, 'Missing variable'), 
                 (missing_functions, 'Missing functions'), (wrong_functions, 'Wrong function pattern')]:
        for v in l:
            print(f'{m}: {v}')
        if l:
            print()
    if missing_files or missing_variables:
        raise VerificationError()
