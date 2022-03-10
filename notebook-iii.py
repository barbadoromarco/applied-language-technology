# Final exam - part 3: this is my solution.
import spacy

small_nlp = spacy.load('en_core_web_sm')
medium_nlp = spacy.load('en_core_web_md')

# To load the spacy file from disk, I have to use this method.
# I need to initialize an empty DocBin object .
small_docbin_loaded = DocBin().from_disk(path='docbin/small.spacy')
medium_docbin_loaded = DocBin().from_disk(path='docbin/medium.spacy')

# To access the docs in the docbin, I have to use this method and cast them into a list.
# I need the original vocab to reconstruct the information.
small_docs = list(small_docbin_loaded.get_docs(small_nlp.vocab)) 
medium_docs = list(medium_docbin_loaded.get_docs(medium_nlp.vocab))

# Now I have all the the docs neatly stored in lists and i can access infprmation.
# I collect the part-of-speech tags from both collections.
small_tokens = []
for doc in small_docs: 
    for token in doc:
        small_tokens.append(token.tag_)

medium_tokens = []
for doc in small_docs:
    for token in doc:
        medium_tokens.append(token.tag_)

# I measure the precision between the two language models using this library.
from sklearn import metrics

precision = metrics.precision_score(small_tokens, medium_tokens, average='micro', zero_division=0) # precision = 1.0

# Time for pandas!
import pandas as pd

#I read this DatFrame that has 2 colums: tokens and pos tags.
data = pd.read_csv('corp/pos.csv')

# I get the 5 most common pos using this function that counts unique values in a pandas Series.
top_pos = data['pos'].value_counts()[:5] # We limit the output to the top 5.

# I get the DataFrame's rows where pos is a noun.
top_nouns = data.loc[data['pos'] == 'NOUN']['token'].value_counts()[:5] # Then, I select the 5 top nouns in the token column.
