import json

data = {} # empty dictionary called data
data['class'] = 'COE332'
data['title'] = 'Software Engineering and Design'
data['inperson'] = False

data['subjects'] = [] # subjects key that is an empty list
# lists have a method called .append()
data['subjects'].append( {'week': 1, 'topic': ['linux', 'python']} )
data['subjects'].append( {'week': 2, 'topic': ['json', 'unittest', 'git']} )

with open('class.json', 'w') as out:
    json.dump(data, out, indent=2) # indent formats by separating lines 
