import pybryt
from textwrap import indent
import sys
import os

import nbformat


header = """---
title: Feedback
---
"""


def run_checks(nb_filename, ref_filename, report=None, prefix='', suffix=''):

    if __name__ != "__main__":
        pybryt.utils.save_notebook(nb_filename)

    ref = pybryt.ReferenceImplementation.load(ref_filename)
    nb = nbformat.read(nb_filename, nbformat.NO_CONVERT)

    ### can do surgery here, eg following

    for c in nb.cells:
        if hasattr(c.metadata, 'tags'):
            if 'pybryt_drop' in c.metadata.tags:
                nb.cells.remove(c)

    #nb.cells.insert(0,nbformat.v4.new_code_cell(source='_funcs = set([k for f, k in locals().items() if callable(k)])'))

    for p in prefix:
        nb.cells.insert(0, nbformat.v4.new_code_cell(source=p))
    for s in suffix:
        nb.cells.append(nbformat.v4.new_code_cell(source=s))

    subm = pybryt.StudentImplementation(nb)
    result = subm.check(ref)


    print(f"SUBMISSION: {nb_filename}")

    # res.messages is a list of messages returned by the reference during grading
    messages = "\n".join(result.messages)
    # res.correct is a boolean for whether the reference was satisfied
    message = f"ALL PASSING: {result.correct}\nMESSAGES:\n{indent(messages, '  - ')}"

    if report:
        with open('result.md', 'w') as myfile:
            myfile.write(header)
            myfile.write(message)
    else:
        print(message)


code = """
functions = [(k,v) for k, v in locals().items() if callable(v)]
for k,v in functions:
    _tmp='_function_'+k
"""

if __name__ == "__main__":
    run_checks(*sys.argv[1:], suffix=[code])