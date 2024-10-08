class Condition(object):
        
    def __str__(self):
        return self.__repr__()
    
    def evaluate(self, values: dict):
        raise NotImplementedError()
    

class Var(Condition):
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return self.name
    
    def evaluate(self, values: dict):
        if self.name in values:
            return values[self.name]
        else:
            raise ValueError(f'Variable {self.name} not found in value dict.')
    

class Const(Condition):
    
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return str(self.value)
    
    def evaluate(self, values: dict):
        return self.value
    

class Op(Condition):
    
    def _op(self):
        return ''
    
    def __repr__(self):
        return '(' + self.left.__repr__() + ') ' + self._op() + ' (' + self.right.__repr__() + ')'
    
    def __init__(self, left: Condition, right: Condition):
        self.left = left
        self.right = right
    

class Eq(Op):
    
    def _op(self):
        return '=='
        
    def evaluate(self, values: dict):
        return self.left.evaluate(values) == self.right.evaluate(values)
    

class Gt(Op):
    
    def _op(self):
        return '>'
        
    def evaluate(self, values: dict):
        return self.left.evaluate(values) > self.right.evaluate(values)
    

class Lt(Op):
    
    def _op(self):
        return '<'
        
    def evaluate(self, values: dict):
        return self.left.evaluate(values) < self.right.evaluate(values)
    

class Ge(Op):
    
    def _op(self):
        return '>='
        
    def evaluate(self, values: dict):
        return self.left.evaluate(values) >= self.right.evaluate(values)
    

class Le(Op):
    
    def _op(self):
        return '<='
        
    def evaluate(self, values: dict):
        return self.left.evaluate(values) <= self.right.evaluate(values)
    

class Not(Condition):
    
    def __init__(self, f: Condition):
        self.f = f
        
    def __repr__(self):
        return 'not (' + self.f.__repr__() + ')'
        
    def evaluate(self, values: dict):
        return not self.f.evaluate(values)
    

class And(Op):
    
    def _op(self):
        return 'and'
        
    def evaluate(self, values: dict):
        return self.left.evaluate(values) and self.right.evaluate(values)
    

class Or(Op):
    
    def _op(self):
        return 'or'
        
    def evaluate(self, values: dict):
        return self.left.evaluate(values) or self.right.evaluate(values)
        

class Node(object):
    pass


class Node(Node):
    
    def __init__(self, condition: Condition, true_action: dict = None, false_action: dict = None, true_child: Node = None, false_child: Node = None):
        self.condition = condition
        self.true_action = true_action if true_action else {}
        self.false_action = false_action if false_action else {}
        self.true_child = true_child
        self.false_child = false_child
        
    def evaluate(self, values: dict) -> dict:
        if self.condition.evaluate(values):
            values.update(self.true_action)
            if self.true_child:
                return self.true_child.evaluate(values)
            else:
                return values
        else:
            values.update(self.false_action)
            if self.false_child:
                return self.false_child.evaluate(values)
            else:
                return values
