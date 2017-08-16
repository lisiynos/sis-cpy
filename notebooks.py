import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def run_notebook(notebook_filename):
    with open(notebook_filename) as f:
        nb = nbformat.read(f, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': 'notebooks'}})


for file in ['day_01', 'day_02', 'day_02_sort', 'day_04_hashes']:
    run_notebook(file + '.ipynb')
