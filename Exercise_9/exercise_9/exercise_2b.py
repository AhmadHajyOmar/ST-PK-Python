from fuzzingbook.ConcolicFuzzer import SimpleConcolicFuzzer, ConcolicTracer, ExpectError

from functions import totient


scf = SimpleConcolicFuzzer()
with ConcolicTracer() as ct:
    with ExpectError(print_traceback=False):
        # z3.StringVal(urllib.parse.unquote('%80')) <-- bug in z3
        ct[totient](10)

# 1. TODO add the trace to scf by calling the correct function with ct and '10' as arguments.

for i in range(10):
    v = None # 2. TODO Fuzz a new string
    print(repr(v))
    if v is None:
        continue
    with ConcolicTracer() as ct:
        with ExpectError(print_traceback=False):
            pass # 3. TODO call totient on v with the tracer ct. Keep in mind that v is a string but totient requires an integer
    # 4. TODO add the trace to scf by calling the correct function with ct and v as arguments.