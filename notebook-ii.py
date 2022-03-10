# Notebook 2
# My solutions to the final exam
# I import the pathlib module and use the module to read the content of each text file into string objects.
from pathlib import Path

corpus_dir = Path('sotu')

files = list(corpus_dir.glob(pattern='*.txt')) 

texts = list(map(lambda file: file.read_text(encoding='utf-8'), files)) # I feed the speech files to the iterator's read function and cast the resulting strings into a python list.

# Then, I import the spacy library and load a small language model for English. I assign the model under the variable nlp.
import spacy

nlp = spacy.load('en_core_web_sm')

processed_speeches = list(map(lambda text: nlp(text), texts)) # I feed the speech strings to the nlp model and cast everything into a list of spacy Doc objects.

# I retrieve named entities from each Doc object in the list speeches and store the named entities into a list named
entities = []

for speech in speeches:
    entities.extend(speech.ents)
    
# I retrieve all Tokens that have the coarse part-of-speech tag VERB from the Doc object under speeches and store the lemma of each verb into a list named verbs.
verbs = []

for speech in speeches:
    for token in speech: 
        if token.pos_ == 'VERB':
            verbs.append(token.lemma_) # I lemmatize in the nested loop.
