import nltk

print("NLTK : version 1\n")
sentence = "Monica Chase paid 300 dollars yesterday at 5 o'clock at the Generator in New York."
sentence2 = "Monique Dupond a payé hier à 17 heures 300 euros à Generator, situé à New York."

tokens = nltk.word_tokenize(sentence)
tokens2 = nltk.word_tokenize(sentence2, language="french")
#print(tokens)
tagged = nltk.pos_tag(tokens)
tagged2 = nltk.pos_tag(tokens2) # lang="french" doesn't exist
#ERROR for FR : NotImplementedError: Currently, NLTK pos_tag only supports English and Russian (i.e. lang='eng' or lang='rus')
#print(tagged)

entities = nltk.chunk.ne_chunk(tagged)
entities2 = nltk.chunk.ne_chunk(tagged2)
print(entities)
print("\n", entities2)


import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
nlp_fr = spacy.load("fr_core_news_md")
doc = nlp(sentence)
doc2 = nlp(sentence2)

print("\nSpacy : version 1\n")
print('ENG\n')
for ent in doc.ents:
    #print(ent.text, ent.start_char, ent.end_char, ent.label_)
    print(ent.text, ent.label_)

print('\nFR\n')
for ent in doc2.ents:
    #print(ent.text, ent.start_char, ent.end_char, ent.label_)
    print(ent.text, ent.label_)

print("\nSpacy : version 2\n")
print('ENG\n')
for token in doc:
    print(token.text, token.ent_iob_, token.ent_type_)

print('\nFR\n')
for token in doc2:
    print(token.text, token.ent_iob_, token.ent_type_)

#displacy.serve(doc, style="ent")
displacy.serve(doc2, style="ent")