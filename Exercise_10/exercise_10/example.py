def foo(x: int, y: int, z: int) -> tuple[int, int]:
    
    if x > 2:
        a: int = 2
        b: int = 3
        if y <= 0 and z == 1:
            b: int = 2
    else:
        a: int = 0
        b: int = 5
    
    if y > 0:
        b: int = 7
    else:
        a: int = 3
        
    assert a + b != 5
    
    return a, b
