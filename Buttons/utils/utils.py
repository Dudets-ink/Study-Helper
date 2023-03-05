import re


def parse_cookie(cookie):
    notes = []
    notes.extend(re.findall(r"(note-\d+:\w+;)", cookie)) 
    
    notes = [note[:-1].split(':') for note in notes]
    
    return notes

def del_cookie(cookie, note_id):
    cookie = cookie.replace(re.findall(rf"({note_id}:\w+;)", cookie)[0], '') 
    
    return cookie