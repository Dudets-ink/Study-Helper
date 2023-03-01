import re


def parse_cookie(cookie):
    notes = []
    notes.extend(re.findall(r"(note-\d+:\w+;)", cookie)) 
    
    print(notes[0][:-1])
    notes = [note[:-1].split(':') for note in notes]
    print(notes, '\n\n\n\nsuka')
    
    return notes