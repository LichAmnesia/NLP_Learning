# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-08-25 00:29:27
# @Last Modified time: 2016-08-25 09:11:01
# @FileName: Simple_tokenization.py

import nltk
import platform
import re
if (platform.system() == 'Windows'):
    nltk.data.path.append("D:\Work\Judge\Project\\nltk_data")
else:
    nltk.data.path.append("/home/vagrant/Project/nltk_data")

# open txt file and make every line to array
lines = [line.strip('\n') for line in open("wsj-short.txt")]
print lines[0]

l = lines[0]
print(re.split('[,. ]+', l))

print(re.findall("[\w]+|[.,;!]+", l))
