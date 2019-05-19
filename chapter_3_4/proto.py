# -*- coding: utf-8 -*-

import os, sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from unmo import Unmo

def prompt(unmo):
    return f"{unmo.name}:{unmo.responder.name} > "

print('Unmo System prototype : proto')
proto = Unmo('proto')

while True:
    print('> ', end='')
    input_text = input()
    input_text = input_text.rstrip()
    if input_text == '':
        break
    response = proto.dialogue(input_text)
    print(prompt(proto) + response)


print('shutdown')