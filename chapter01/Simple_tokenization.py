# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-08-25 00:29:27
# @Last Modified time: 2016-08-28 23:29:31
# @FileName: Simple_tokenization.py

import nltk
import platform
import re
if (platform.system() == 'Windows'):
    nltk.data.path.append("D:\Work\Judge\Project\\nltk_data")
else:
    nltk.data.path.append("/home/vagrant/Project/nltk_data")

# open txt file and make every line to array

# [  ['The','company'   ]   ['This', 'company'    ]]
lines = [line.strip() for line in open("wsj-short.txt")]
line = []

num = 0
for l in lines:
    num += len(re.findall("[\w']+|[.,!?;]+", l))
print("Question 6: " + str(num))


# for problem 7
num = 0
for ll in lines:
    num = num + len(re.findall("(Jan\.)|(Feb\.)|(Mar\.)|(Apr\.)|(Jun\.)|(Jul\.)|(Aug\.)|(Sep\.)|(Oct\.)|(Nov\.)|(Dec\.)|([\w']+)|([.,!?;]+)", ll))
print("Question 7: " + str(num))
