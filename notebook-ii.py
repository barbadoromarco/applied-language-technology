# Notebook 2

# My solutions to the final exam

# Import the pathlib module and use the module to read the content of each text file into string objects.

from pathlib import Path

corpus_dir = Path('data/sotu')

files = list(corpus_dir.glob(pattern='*.txt'))

speeches = list(map(lambda file: file.read_text(encoding='utf-8'), files))
