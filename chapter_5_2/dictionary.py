# -*- coding: utf-8 -*-

import codecs


def messages(path):
    results = []
    content = codecs.open(path, "r", "utf-8")
    for row in content:
        if row.rstrip() != '':
            results.append(row.rstrip())            
    content.close()
    return results    

def divided_by(rows, word):
    results = {}
    for row in rows:
        divided = row.split(word)
        results[divided[0]] = divided[1]
    return results


class Dictionary:
    def __init__(self):
        directory = './dics/'
        self.random = messages(directory + 'random.txt')
        self.patterns = divided_by(messages(directory + 'pattern.txt'), '\t')