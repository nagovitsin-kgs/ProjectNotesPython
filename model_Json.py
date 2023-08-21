import json

import view
from note import Note


class Model_Json(object):

    def __init__(self, file_Name):
        self.file_Name = file_Name
        self.notes = list()

    def create_note(self, note):
        self.notes = self.read_notes()
        max_id = 0
        for item in self.notes:
            if item.note_id > max_id:
                max_id = item.note_id
        note_id = max_id + 1
        note.note_id = note_id

        self.notes.append(note)
        self.write_json(self.notes)
