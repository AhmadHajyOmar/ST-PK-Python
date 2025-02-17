"""
Use this file to implement your solution for exercise 4-1 b.
"""

from examples import examples

RE_GRAMMAR = {
    '<start>': ['<re>'],
    '<re>': ['<alternative>', '^<alternative>', '<alternative>$', '^<alternative>$'],
    '<alternative>': ['<concat>', '<concat>|<alternative>'],
    '<concat>': ['', '<concat><regex>'],
    '<regex>': ['<symbol>', '<symbol>*', '<symbol>+', '<symbol>?', '<symbol>{<range>}'],
    '<symbol>': ['.', '<char>', '(<alternative>)'],
    '<char>': ['a', 'b', 'c'],
    '<range>': ['<num>', ',<num>', '<num>,'],
    '<num>': ['1', '2'],
}

def learn_probabilities():
    return None