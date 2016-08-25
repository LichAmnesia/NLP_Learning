# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-08-24 23:53:57
# @Last Modified time: 2016-08-24 23:58:48
# @FileName: test.py

import nltk
nltk.data.path.append("/home/vagrant/Project/nltk_data")

# define a sentence
sentence = """At eight o'clock on Thuesday evening,
    Lich didn't feel good."""

# get tokens of this sentence
tokens = nltk.word_tokenize(sentence)
print(tokens)

# get tags
tag = nltk.pos_tag(tokens)
print(tag)

entities = nltk.chunk.ne_chunk(tag)
print(entities)
