#!/usr/bin/env python

import itertools
import string

def map_reduce(i,mapper,reducer):
	intermediate = []
	for (key,value) in i.items():
		print "%s,%s" % (key,value)
		intermediate.extend(mapper(key,value))
	groups = {}
	for key, group in itertools.groupby(sorted(intermediate), lambda x: x[0]):
		groups[key] = list([y for x, y in group])
	return [reducer(intermediate_key,groups[intermediate_key]) for intermediate_key in groups]

def remove_punctuation(s):
	return s.translate(string.maketrans("",""),string.punctuation)

def mapper(input_key,input_value):
	return [(word,1) for word in remove_punctuation(input_value.lower()).split()]
    
def reducer(intermediate_key,intermediate_value_list):
	return (intermediate_key,sum(intermediate_value_list))

filenames = ["data"]
i = {}
for filename in filenames:
	f = open(filename)
	i[filename] = f.read()
	f.close()

print sorted(map_reduce(i,mapper,reducer),key= lambda x: x[0])
