import sys
import threading
import time

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtWidgets import QFileDialog, QGraphicsOpacityEffect

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
        self.t_keys = ['Q', 'W', 'E', 'R', 'T', 'Y']
        self.tools = [True, False, True, False, True, False]
        self.effects = [QGraphicsOpacityEffect() for _ in range(6)]
        self.update_tools()

    def keyPressEvent(self, event):
        if QKeyEvent.isAutoRepeat(event):
            return
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
            case Qt.Key.Key_Q.value:
                if self.tools[0]:
                    threading.Thread(target=self.tool_on, args=('file',)).start()
                    filename, filetype = QFileDialog.getOpenFileName(self, '選擇樂譜', './', '文字文件 (*.txt)')
                    self.ui.lb_path.setText(f'File: {filename}')
                    self.tools[3] = self.tools[5] = True
                    self.update_tools()
            case Qt.Key.Key_W.value:
                if self.tools[1]:
                    threading.Thread(target=self.tool_on, args=('save',)).start()
            case Qt.Key.Key_E.value:
                if self.tools[2]:
                    threading.Thread(target=self.tool_on, args=('stop',)).start()
                    for player in self.players.values():
                        player.stop()
                    self.ui.img_play.setStyleSheet(f'border-image: url("assets/image/play.png");')
            case Qt.Key.Key_R.value:
                if self.tools[3]:
                    threading.Thread(target=self.tool_on, args=('play',)).start()
                    img = 'pause' if self.ui.img_play.styleSheet() == 'border-image: url("assets/image/play.png");' else 'play'
                    self.ui.img_play.setStyleSheet(f'border-image: url("assets/image/{img}.png");')
                    self.update_tools()
            case Qt.Key.Key_T.value:
                for player in self.players.values():
                    player.stop()
                if self.tools[4]:
                    threading.Thread(target=self.tool_on, args=('record',)).start()
            case Qt.Key.Key_Y.value:
                if self.tools[5]:
                    threading.Thread(target=self.tool_on, args=('edit',)).start()

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
        time.sleep(0.2)
        getattr(self.ui, f'img_{direction}').setStyleSheet(f'border-image: url("assets/image/{direction}.png");')

    def tool_on(self, tool: str):
        x, y = self.ui.img_file.x(), self.ui.img_file.y()
        getattr(self.ui, f'img_{tool}').setGeometry(x - 5, y - 5, 60, 60)
        time.sleep(0.1)
        getattr(self.ui, f'img_{tool}').setGeometry(x, y, 50, 50)

    def update_tools(self):
        for key, tool, effect in zip(self.t_keys, self.tools, self.effects):
            effect.setOpacity(1 if tool else 0.3)
            getattr(self.ui, f'tool_{key}').setGraphicsEffect(effect)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    QtGui.QFontDatabase.addApplicationFont('assets\\font\\SpaceJaeger-BW2pn.otf')
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
