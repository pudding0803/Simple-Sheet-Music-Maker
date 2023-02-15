import sys
import threading
import time

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput

from ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pitch = 4
        self.w_keys = ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        self.b_keys = ['S', 'D', 'G', 'H', 'J']
        self.players = {key: QMediaPlayer() for key in self.w_keys + self.b_keys}
        self.audios = {key: QAudioOutput() for key in self.w_keys + self.b_keys}
        for player, audio in zip(self.players.values(), self.audios.values()):
            player.setAudioOutput(audio)
        # filename, filetype = QFileDialog.getOpenFileName(self, '選擇資料集', './',
        #                                                  '文字文件 (*.txt)')
        # print(filename, filetype)

    def keyPressEvent(self, event):
        match event.key():
            case Qt.Key.Key_Z.value | Qt.Key.Key_X.value | Qt.Key.Key_C.value | Qt.Key.Key_V.value | \
                 Qt.Key.Key_B.value | Qt.Key.Key_N.value | Qt.Key.Key_M.value | Qt.Key.Key_S.value | \
                 Qt.Key.Key_D.value | Qt.Key.Key_G.value | Qt.Key.Key_H.value | Qt.Key.Key_J.value:
                key = chr(event.key())
                self.players[key].setSource(QUrl.fromLocalFile(f'assets\\audio\\piano\\{self.pitch}\\{key}.mp3'))
                self.players[key].play()
                threading.Thread(target=self.key_on, args=(key,)).start()
            case Qt.Key.Key_Down.value | Qt.Key.Key_Left.value:
                self.pitch = max(1, self.pitch - 1)
                self.ui.pitch.setText(str(self.pitch))
                threading.Thread(target=self.pitch_on, args=('left',)).start()
            case Qt.Key.Key_Up.value | Qt.Key.Key_Right.value:
                self.pitch = min(7, self.pitch + 1)
                self.ui.pitch.setText(str(self.pitch))
                threading.Thread(target=self.pitch_on, args=('right',)).start()

    def key_on(self, key: str):
        getattr(self.ui, f'key_{key}').setStyleSheet(
            f'background-color: {"#FF3860" if key in self.w_keys else "#3273DC"};'
        )
        time.sleep(0.3)
        getattr(self.ui, f'key_{key}').setStyleSheet(
            f'background-color: {"#FFFCF3" if key in self.w_keys else "#0A0D18"};'
        )

    def pitch_on(self, direction: str):
        getattr(self.ui, f'img_{direction}').setStyleSheet(f'border-image: url("assets/image/{direction}_on.png");')
        time.sleep(0.3)
        getattr(self.ui, f'img_{direction}').setStyleSheet(f'border-image: url("assets/image/{direction}.png");')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    QtGui.QFontDatabase.addApplicationFont('assets\\font\\SpaceJaeger-BW2pn.otf')
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
