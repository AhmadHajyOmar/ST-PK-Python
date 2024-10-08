from fuzzingbook.Grammars import Grammar, crange, is_valid_grammar, opts
from fuzzingbook.GrammarFuzzer import GrammarFuzzer
from fuzzingbook.ProbabilisticGrammarFuzzer import ProbabilisticGrammarFuzzer
from fuzzingbook.GeneratorGrammarFuzzer import GeneratorGrammarFuzzer, ProbabilisticGeneratorGrammarCoverageFuzzer
from fuzzingbook.WebFuzzer import WebFormFuzzer, HTMLGrammarMiner, cgi_encode

REGISTRATION_GRAMMAR: Grammar = {
    "<start>": ["<registration>"],
    "<registration>": ["/register?name=<name>&lastname=<lastname>&email=<email>"
                       "&password=<password>&password2=<password2>&banking=<banking>"],
    "<name>": ["Leon", "Marius"],
    "<lastname>": ["Bettscheider", "Smytzek"],
    "<email>": [cgi_encode("leon.bettscheider@cispa.de"), 
                cgi_encode("marius.smytzek@cispa.de")],
    "<password>": ["password"],
    "<password2>": ["password"],
    "<banking>": ["<digit>" * 16],
    "<digit>": crange('0', '9')
}

assert is_valid_grammar(REGISTRATION_GRAMMAR)

def get_fuzzer(httpd_url):
    return GrammarFuzzer(REGISTRATION_GRAMMAR)