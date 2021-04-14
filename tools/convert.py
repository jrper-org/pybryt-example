import pybryt
import sys

import nbformat


def do_pickle(nb_name, pkl_name="solution.pkl", stripped_name=None):

    ref = pybryt.ReferenceImplementation.compile(nb_name)
    ref.dump(pkl_name)

    if stripped_name:
        nb = nbformat.read(nb_name, nbformat.NO_CONVERT)

        for c in nb.cells:
            if hasattr(c.metadata, 'tags'):
                if 'answer_cell' in c.metadata.tags:
                    nb.cells.remove(c)

        nbformat.write(nb, stripped_name)

if __name__ == "__main__":
    do_pickle(*sys.argv[1:])
