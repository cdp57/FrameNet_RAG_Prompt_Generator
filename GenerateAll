#prompt generator for RAG FrameNet project


#import framenet_v17 data
import nltk
nltk.download('framenet_v17')
from nltk.corpus import framenet as fn
import re
import xml.dom.minidom


#loops through all the frame IDs, adding a description for each frame
array = ['a'] * 5000
head = 1600
while head < 5000:


   #only adds frame with valid ID numbers
   try:
       f = fn.frame(head)
       head += 1
       current = f.name
       current += '.xml'
       ID = ''


       #parse the XML files for the desired frame
       xml_doc = xml.dom.minidom.parse(current)


       #obtain the frame ID from the XML file in order to pull information from FrameNet database
       f = ''
       frames = xml_doc.getElementsByTagName("frame")
       for frame in frames:
           ID = frame.getAttribute('ID')
           f = fn.frame(int(ID))


       #extract key information about frame from the FrameNet database via NLTK(name, defintion, core FEs, lexical units)
       name = f.name
       definition = f.definition
       lex_list = f.lexUnit
       verb_list = []
       adj_list = []
       other_list = []


       #sort lexical units by part of speech
       for element in lex_list:
        if element[len(element) - 1] == 'v' and element[len(element) - 2] == '.':
            element = element[0:len(element) - 2]
            verb_list.append(element)
        elif element[len(element) - 1] == 'a' and element[len(element) - 2] == '.':
            element = element[0:len(element) - 2]
            adj_list.append(element)
        elif element[len(element) - 1] == 'n' and element[len(element) - 2] == '.':
            element = element[0:len(element) - 2]
            other_list.append(element)
        elif element[len(element) - 1] == 'v' and element[len(element) - 4] == '.':
                element = element[0:len(element) - 4]
                other_list.append(element)
        elif element[len(element) - 1] == 'p' and element[len(element) - 5] == '.':
            element = element[0:len(element) - 5]
            other_list.append(element)
        elif element[len(element) - 1] == 'n' and element[len(element) - 5] == '.':
            element = element[0:len(element) - 5]
            other_list.append(element)
        elif element[len(element) - 1] == 'j' and element[len(element) - 5] == '.':
            element = element[0:len(element) - 5]
            other_list.append(element)


       #information extracted by parsing the XML for the desired frame (core FE definitions, number of core frames, frame relations)
       FE_list = []
       FE_def_list = []
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


       #extract core FEs and their defintions; remove annotated examples from definitions
       FEs = xml_doc.getElementsByTagName("FE")
       for FE in FEs:
          type = FE.getAttribute('coreType')
          if type == 'Core' or type == 'Core-Unexpressed':
              description = FE.getElementsByTagName('definition')[0].childNodes[0].data
              FE_name = FE.getAttribute('name')
              FE_list.append(FE_name)
              matches = re.findall(r'<ex>.+?</ex>',description)
              for match in matches:
                  description = description.replace(match, '')
              matches2 = re.findall(r'<.+?>',description)
              for match in matches2:
                  description = description.replace(match, '')
              matches3 = re.findall(r'\n', description)
              for match in matches3:
                  description = description.replace(match, '')
              FE_def_list.append(description)


       #extract frame relations
       relations = xml_doc.getElementsByTagName("frameRelation")
       for relation in relations:
          type = relation.getAttribute('type')
          if type == 'Is Inherited by':
              count = len(relation.getElementsByTagName('relatedFrame'))
              index = 0
              while index < count:
                  inherited_by_list.append(relation.getElementsByTagName('relatedFrame')[index].childNodes[0].data)
                  index += 1


          if type == 'Inherits from':
              count = len(relation.getElementsByTagName('relatedFrame'))
              index = 0
              while index < count:
                  inherits_from_list.append(relation.getElementsByTagName('relatedFrame')[index].childNodes[0].data)
                  index += 1


          if type == 'Perspective on':
              count = len(relation.getElementsByTagName('relatedFrame'))
              index = 0
              while index < count:
                  perspective_on_list.append(relation.getElementsByTagName('relatedFrame')[index].childNodes[0].data)
                  index += 1


          if type == 'Is Perspectivized in':
              count = len(relation.getElementsByTagName('relatedFrame'))
              index = 0
              while index < count:
                  is_perspectivized_in_list.append(relation.getElementsByTagName('relatedFrame')[index].childNodes[0].data)
                  index += 1


          if type == 'Uses':
              count = len(relation.getElementsByTagName('relatedFrame'))
              index = 0
              while index < count:
                  uses_list.append(relation.getElementsByTagName('relatedFrame')[index].childNodes[0].data)
                  index += 1


          if type == 'Is Used by':
              count = len(relation.getElementsByTagName('relatedFrame'))
              index = 0
              while index < count:
                  is_used_by_list.append(relation.getElementsByTagName('relatedFrame')[index].childNodes[0].data)
                  index += 1


          if type == 'Subframe of':
              count = len(relation.getElementsByTagName('relatedFrame'))
              index = 0
              while index < count:
                  subframe_of_list.append(relation.getElementsByTagName('relatedFrame')[index].childNodes[0].data)
                  index += 1


          if type == 'Has Subframe(s)':
              count = len(relation.getElementsByTagName('relatedFrame'))
              index = 0
              while index < count:
                  has_subframe_list.append(relation.getElementsByTagName('relatedFrame')[index].childNodes[0].data)
                  index += 1


          if type == 'Precedes':
              count = len(relation.getElementsByTagName('relatedFrame'))
              index = 0
              while index < count:
                  precedes_list.append(relation.getElementsByTagName('relatedFrame')[index].childNodes[0].data)
                  index += 1


          if type == 'Is Preceded by':
              count = len(relation.getElementsByTagName('relatedFrame'))
              index = 0
              while index < count:
                  is_preceded_by_list.append(relation.getElementsByTagName('relatedFrame')[index].childNodes[0].data)
                  index += 1


          if type == 'Is Inchoative of':
              count = len(relation.getElementsByTagName('relatedFrame'))
              index = 0
              while index < count:
                  is_inchoative_of_list.append(relation.getElementsByTagName('relatedFrame')[index].childNodes[0].data)
                  index += 1


          if type == 'Is Causative of':
              count = len(relation.getElementsByTagName('relatedFrame'))
              index = 0
              while index < count:
                  is_causative_of_list.append(relation.getElementsByTagName('relatedFrame')[index].childNodes[0].data)
                  index += 1


       #generates prompt based off of extracted information; omits parts of prompt where no relevant input is present
       prompt = name
       prompt += '\n'
       prompt += ID
       prompt += '\n'
       prompt += 'The semantic frame for “'
       prompt += name
       prompt += '” is defined as follows: “'
       prompt += definition
       prompt += '" '
       prompt += '\n'
       if len(FE_list) != 0:
           prompt += 'Core frame elements in this frame are '
           def_count = 0
           for element in FE_list:
            prompt += '"'
            prompt += element
            prompt += '" : '
            prompt += FE_def_list[def_count]
            prompt = prompt.rstrip('.')
            prompt += ', '
            def_count += 1
           prompt = prompt.rstrip(', ')
           prompt += '. '
           prompt += '\n'
       if len(verb_list) != 0 or len(adj_list) != 0 or len(other_list) != 0:
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
            if len(adj_list) != 0 or len (verb_list) != 0:
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


       prompt += "BREAK"
       prompt += '\n'
       prompt += '\n'


       #adds the prompt to the context array
       array[head] = prompt


   #catches an exception if the frame ID is invalid
   except:
       head += 1


#outputs the context for all frames
for prompt in array:
   if prompt != 'a':
       print(prompt)

