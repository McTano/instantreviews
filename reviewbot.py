import spacy
import random
import re


""" run it with `$ python reviewbot.py` """

adj_list = ["love", "hate", "kinda like", "really like", "really don't like", "sorta like", "am indifferent to"]
en_nlp = spacy.load('en')


def diagnose(doc):
	""" Takes a document from spaCy and print out the tokens within it. """
	for t in doc:
		print t.dep_ + ", " + t.pos_ + "/" + t.tag_  + ": " + t.lower_

def invert_possessive(phrase):
	return re.sub(r"\b(my)\b", 'your', phrase)

def review(tweet):
	doc = en_nlp(tweet)
	# diagnose(doc)
	for chunk in doc.noun_chunks:
		print chunk.text
		t = chunk.root
		if (t.pos_ == "NOUN" or t.pos_ == "PROPN") and (t.dep_ == "pobj" or t.dep_ == "dobj") and (t.tag_ != "WP"):
			review_obj = chunk
			# now to make the review
			review = reviewer(review_obj)
			return review
			break

def reviewer(span):
	""" Takes a noun chunk span, then makes a random review around it. """
	review_obj_string = invert_possessive(span.text)
	adj = random.choice(adj_list)
	return "I %s %s." % (adj, review_obj_string)


def strip_punctuation(str):
	return re.sub(r'[\W]', '', str).lower()

def hardly_know_her(tweet):
	words = tweet.split(' ')
	words = map(strip_punctuation, words)
	for word in words:
		if word[-1] == 'r' and word[-2] in 'aeiou':
			return True

def damn_near_killed_him(tweet):
	words = tweet.split(' ')
	words = map(strip_punctuation, words)
	for word in words:
		if word[-1] == 'm' and word[-2] in 'aeiou':
			return True

def joke_response(tweet):
	if hardly_know_her(tweet):
		print "hardly know her."
	elif damn_near_killed_him(tweet):
		print "damn near killed him"

def main():
	tweet = unicode(raw_input("what's up yo?\n"))
	# print review(tweet)
	check_for_setups(tweet)
	main()

if __name__ == '__main__':
	main()