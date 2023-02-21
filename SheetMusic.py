class Note:
    def __init__(self, note: str, duration: int):
        key_map = {
            '0': '0', '1': 'Z', '2': 'X', '3': 'C', '4': 'V', '5': 'B', '6': 'N', '7': 'M',
            '1#': 'S', '2b': 'S', '2#': 'D', '3b': 'D', '4#': 'G', '5b': 'G', '5#': 'H', '6b': 'H', '6#': 'J', '7b': 'J'
        }
        self.key = key_map[note]
        self.pitch = 0
        self.duration = duration


class SheetMusic:
    def __init__(self, duration: int):
        self.sheet = []
        self.duration = duration

    def __call__(self) -> list:
        return self.sheet

    def set_duration(self, duration: int) -> None:
        self.duration = duration

    def from_file(self, file) -> None:
        self.sheet = []
        for line in file:
            self.append(line[:-1] if line[-1] == '\n' else line)

    def append(self, notes: str) -> None:
        for note in notes.split():
            if note == '-':
                self.sheet[-1].duration += self.duration
            else:
                self.sheet.append(Note(note, self.duration))

    def clear(self) -> None:
        self.sheet.clear()

    def export(self) -> None:
        with open('file.ssm', 'w') as file:
            file.writelines(self.sheet)
