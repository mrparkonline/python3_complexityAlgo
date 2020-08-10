#!/usr/bin/python3

# Converted Jupyter markdowns
from os import listdir

files = listdir().copy()
notes = list(filter(lambda x : x.endswith('.md'), files))

frontMatter = '''
---
title: ""
date:
draft: false
order:
lesson: true
descriptor: ""
---

'''

for file in notes:
    print('Currently reading:', file)
    title = file.split(' ')[0].lower() + '.md'
    data = None

    with open(file, 'r') as current_file:
        data = current_file.read()

    path = './lessons/' + title
    print('Writing to:', path)
    with open(path, 'w') as new_file:
        new_file.write(frontMatter)
        new_file.write(data)

#f1 = notes[0]

"""
with open(f1, 'r') as current:
    data = current.read()
    print(data)

f2 = './lessons/new.md'

with open(f2, 'w') as new_file:
    new_file.write(frontMatter)
    new_file.write(data)
"""
