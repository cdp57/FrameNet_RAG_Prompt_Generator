#prompt generator for RAG FrameNet project

#import framenet_v17 data
import nltk
nltk.download('framenet_v17')
from nltk.corpus import framenet as fn

#extract frame based on id number (must input)
f = fn.frame(000)

#print frame name
print(f.name)

#extract key information about frame (name, defintion, core FEs, lexical units)
name = f.name
definition = f.definition
FE_list = f.FE
lex_list = f.lexUnit
verb_list = []
adj_list = []
other_list = []

#sort lexical units by part of speech
for element in lex_list:
    if element[len(element) - 1] == 'v':
        element = element.rstrip('.v')
        verb_list.append(element)
    if element[len(element) - 1] == 'a':
        element = element.rstrip('.a')
        adj_list.append(element)
    if element[len(element) - 1] == 'n' and element[len(element) - 2] == '.':
        element = element.rstrip('.n')
        other_list.append(element)

#information that cannot be extracted automatically, requires manual input (core FE definitions, number of core frames, frame relations)
FE_def_list = [""]
core_count = 0
inherits_from_list = []
inherited_by_list = []
perspective_on_list = []
is_perspectivized_in_list = []
uses_list = []
is_used_by_list = []
subframe_of_list = []
has_subframe_list = []
precedes_list = []
is_preceded_by_list = []
is_inchoative_of_list = []
is_causative_of_list = []

#generates prompt based off of extracted information; omits parts of prompt where no relevant input is present
prompt = 'The semantic frame for “'
prompt += name
prompt += '” is defined as follows: “'
prompt += definition
prompt += '" '
prompt += '\n'
prompt += 'Core frame elements in this frame are "'
count = 0
for element in FE_list:
    prompt += element
    prompt += ', '
    count += 1
    if count == core_count:
        break
prompt = prompt.rstrip(', ')
prompt += '." '
for element in FE_def_list:
    prompt += element
    prompt += ' '
prompt += '\n'
prompt += 'Words evoking this frame are '
if len(verb_list) > 0:
    prompt += 'the verbs '
    for element in verb_list:
        prompt += element
        prompt += ', '
if len(adj_list) > 0:
    prompt += 'the adjectives '
    for element in adj_list:
        prompt += element
        prompt += ', '
if len(other_list) > 0:
    prompt += 'and other lexical units including '
    for element in other_list:
        prompt += element
        prompt += ', '
prompt = prompt.rstrip(', ')
prompt += '. '
prompt += '\n'

#the following twelve blocks of code add frame relations if they are present
if len(inherits_from_list) > 0:
    prompt += 'This frame inherits from the frame(s) '
    for element in inherits_from_list:
        prompt += '"'
        prompt += element
        prompt += '", '
    prompt = prompt.rstrip(', ')
    prompt += '. '
    prompt += '\n'

if len(inherited_by_list) > 0:
    prompt += 'This frame is inherited by the frame(s) '
    for element in inherited_by_list:
        prompt += '"'
        prompt += element
        prompt += '", '
    prompt = prompt.rstrip(', ')
    prompt += '. '
    prompt += '\n'

if len(perspective_on_list) > 0:
    prompt += 'This frame has a perspective on the frame(s) '
    for element in perspective_on_list:
        prompt += '"'
        prompt += element
        prompt += '", '
    prompt = prompt.rstrip(', ')
    prompt += '. '
    prompt += '\n'

if len(is_perspectivized_in_list) > 0:
    prompt += 'This frame is perspectivized by the frame(s) '
    for element in is_perspectivized_in_list:
        prompt += '"'
        prompt += element
        prompt += '", '
    prompt = prompt.rstrip(', ')
    prompt += '. '
    prompt += '\n'

if len(uses_list) > 0:
    prompt += 'This frame uses the frame(s) '
    for element in uses_list:
        prompt += '"'
        prompt += element
        prompt += '", '
    prompt = prompt.rstrip(', ')
    prompt += '. '
    prompt += '\n'

if len(is_used_by_list) > 0:
    prompt += 'This frame is used by the frame(s) '
    for element in is_used_by_list:
        prompt += '"'
        prompt += element
        prompt += '", '
    prompt = prompt.rstrip(', ')
    prompt += '. '
    prompt += '\n'

if len(subframe_of_list) > 0:
    prompt += 'This frame is a subframe of the frame(s) '
    for element in subframe_of_list:
        prompt += '"'
        prompt += element
        prompt += '", '
    prompt = prompt.rstrip(', ')
    prompt += '. '
    prompt += '\n'

if len(has_subframe_list) > 0:
    prompt += 'This frame has the subframe(s) '
    for element in has_subframe_list:
        prompt += '"'
        prompt += element
        prompt += '", '
    prompt = prompt.rstrip(', ')
    prompt += '. '
    prompt += '\n'

if len(precedes_list) > 0:
    prompt += 'This frame precedes the frame(s) '
    for element in precedes_list:
        prompt += '"'
        prompt += element
        prompt += '", '
    prompt = prompt.rstrip(', ')
    prompt += '. '
    prompt += '\n'

if len(is_preceded_by_list) > 0:
    prompt += 'This frame is preceded by the frame(s) '
    for element in is_preceded_by_list:
        prompt += '"'
        prompt += element
        prompt += '", '
    prompt = prompt.rstrip(', ')
    prompt += '. '
    prompt += '\n'

if len(is_inchoative_of_list) > 0:
    prompt += 'This frame is inchoative of the frame(s) '
    for element in is_inchoative_of_list:
        prompt += '"'
        prompt += element
        prompt += '", '
    prompt = prompt.rstrip(', ')
    prompt += '. '
    prompt += '\n'

if len(is_causative_of_list) > 0:
    prompt += 'This frame is causative of the frame(s) '
    for element in is_causative_of_list:
        prompt += '"'
        prompt += element
        prompt += '", '
    prompt = prompt.rstrip(', ')
    prompt += '. '
    prompt += '\n'

prompt += 'Please propose 10 additional words that evoke the “'
prompt += name
prompt += '” semantic frame. '
prompt += '\n'
prompt += 'Present them as a JSON array. '

#outputs final prompt
print(prompt)
