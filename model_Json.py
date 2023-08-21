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

    def read_note(self, search_id):
        self.notes = self.read_notes()
        for note in self.notes:
            if note.note_id == search_id:
                return note
        else:
            view.display_note_id_not_exist(search_id)
