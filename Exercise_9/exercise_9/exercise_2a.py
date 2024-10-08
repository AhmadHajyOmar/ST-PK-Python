from fuzzingbook.ConcolicFuzzer import ConcolicTracer

from functions import *


def run(func: callable, args: tuple):
    
    # 1. TODO setup the ConcolicTracer ct and execute the function func on args.
    # You can execute a function f on a tuple t by calling f(*t).
    
    print(ct.path)
    
    sat, arg_map = None # 2. TODO evaluate the path constraints by calling the corresponding function.
    print((sat, arg_map))
    
    if sat == 'sat':
        args2 = []
        for k in arg_map:
            args2.append(int(arg_map[k][0]))
        
        # 3. TODO setup the ConcolicTracer ct2 and execute the function func on args2.
        # You can execute a function f on a list l by calling f(*l).
            
        print(ct2.path)
        

if __name__ == '__main__':
    run(sigma, (2, 4))
    print()
    run(totient, (20, ))