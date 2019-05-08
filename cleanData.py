#print('hello')

import spacy
from spacy.tokens import Span
import collections

def print_line():
	print("\n-----------------------------------------------------")

def get_entities():
	doc = nlp(text)

	print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
	print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

	for entity in doc.ents:
    print(entity.text, entity.label_)

def get_lpd():
	doc = nlp(text)

	for token in doc:
		print("Text: {} | Lemmatization: {} | Part of Speech: {} | Dependency Parsing: {}".format(token.text, token.lemma_, token.pos_, token.dep_))

	print_line()

def most_frequent():
	doc = nlp(text)
	words = [token.text for token in doc if token.pos_ != "PUNCT"]
	print(collections.Counter(words).most_common(10))
	print_line()

nlp = spacy.load("en_core_web_sm")

text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

get_entities()
update_entities()
most_frequent()


