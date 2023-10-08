import os
import json

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NotesManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def create_note(self, title, content):
        note = Note(title, content)
        notes = self._load_notes()
        notes.append(vars(note))
        self._save_notes(notes)

    def read_notes(self):
        notes = self._load_notes()
        for note in notes:
            print("Title:", note['title'])
            print("Content:", note['content'])
            print("--------------------------")

    def update_note(self, title, new_content):
        notes = self._load_notes()
        for note in notes:
            if note['title'] == title:
                note['content'] = new_content
                self._save_notes(notes)
                return
        print("Note with title '{}' not found.".format(title))

    def delete_note(self, title):
        notes = self._load_notes()
        for note in notes:
            if note['title'] == title:
                notes.remove(note)
                self._save_notes(notes)
                return
        print("Note with title '{}' not found.".format(title))

    def _load_notes(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r') as file:
            try:
                notes = json.load(file)
                return notes
            except json.JSONDecodeError:
                return []

    def _save_notes(self, notes):
        with open(self.file_path, 'w') as file:
            json.dump(notes, file)

# if __name__ == '__main__':
#      Пример использования

#      Создание менеджера заметок
#     notes_manager = NotesManager("notes.json")

#      Создание заметки
#     notes_manager.create_note("Заметка 1", "Это содержимое заметки 1")

#      Чтение списка заметок
#     notes_manager.read_notes()

#      Редактирование заметки
#     notes_manager.update_note("Заметка 1", "Новое содержимое заметки 1")

#      Удаление заметки
#     notes_manager.delete_note("Заметка 1")