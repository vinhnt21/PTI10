import sys
from datetime import datetime
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt


class Note:
    def __init__(self, title="", content=""):
        self.title = title
        self.content = content
        self.created_date = datetime.now()
        self.modified_date = datetime.now()

    def update(self, title, content):
        self.title = title
        self.content = content
        self.modified_date = datetime.now()

    def __str__(self):
        return f"{self.title} ({self.modified_date.strftime('%d/%m/%Y %H:%M')})"


class NoteList:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)
        return len(self.notes) - 1  # Return index of new note

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            self.notes.pop(index)

    def get_note(self, index):
        if 0 <= index < len(self.notes):
            return self.notes[index]
        return None

    def update_note(self, index, title, content):
        if 0 <= index < len(self.notes):
            self.notes[index].update(title, content)


class NoteApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file
        uic.loadUi("demo.ui", self)

        # Initialize note list
        self.note_list = NoteList()

        # Connect signals
        self.newButton.clicked.connect(self.new_note)
        self.saveButton.clicked.connect(self.save_note)
        self.deleteButton.clicked.connect(self.delete_note)
        self.noteListWidget.currentRowChanged.connect(self.note_selected)
        self.titleEdit.textChanged.connect(self.content_changed)
        self.contentEdit.textChanged.connect(self.content_changed)

        # Initialize status
        self.statusBar().showMessage("Sẵn sàng")
        self.current_note_index = -1
        self.is_modified = False

        # Create first note
        self.new_note()

    def new_note(self):
        note = Note("Ghi chú mới", "")
        index = self.note_list.add_note(note)
        self.noteListWidget.addItem(str(note))
        self.noteListWidget.setCurrentRow(index)
        self.show_note(index)
        self.statusBar().showMessage("Đã tạo ghi chú mới")

    def save_note(self):
        if self.current_note_index >= 0:
            title = self.titleEdit.text()
            content = self.contentEdit.toPlainText()
            self.note_list.update_note(self.current_note_index, title, content)
            self.noteListWidget.item(self.current_note_index).setText(
                str(self.note_list.get_note(self.current_note_index))
            )
            self.is_modified = False
            self.statusBar().showMessage("Đã lưu ghi chú")

    def delete_note(self):
        if self.current_note_index >= 0:
            self.note_list.delete_note(self.current_note_index)
            self.noteListWidget.takeItem(self.current_note_index)
            if self.noteListWidget.count() == 0:
                self.new_note()
            self.statusBar().showMessage("Đã xóa ghi chú")

    def note_selected(self, index):
        if index >= 0:
            self.show_note(index)

    def show_note(self, index):
        self.current_note_index = index
        note = self.note_list.get_note(index)
        if note:
            self.titleEdit.setText(note.title)
            self.contentEdit.setText(note.content)
            self.is_modified = False

    def content_changed(self):
        if self.current_note_index >= 0:
            self.is_modified = True
            self.statusBar().showMessage("Chưa lưu")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = NoteApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

# Created/Modified files during execution:
# - demo.ui
# - main.py
