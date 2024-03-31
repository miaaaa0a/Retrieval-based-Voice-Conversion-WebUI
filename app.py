# pyqt stuff
import sys
from PyQt6.QtWidgets import (
    QApplication, QFileDialog, QMainWindow, QLineEdit
)
from PyQt6.QtCore import Qt
from ui.main import Ui_MainWindow
from ui.inferClass import InferenceThread

# rvc stuff
from infer.modules.vc.modules import VC
from configs.config import Config
from dotenv import load_dotenv
import soundfile as sf

# misc stuff
from itertools import chain
import os
import time

# some setup
config = Config()
vc = VC(config)
load_dotenv()

weight_root = os.getenv("weight_root")
weight_uvr5_root = os.getenv("weight_uvr5_root")
index_root = os.getenv("index_root")
outside_index_root = os.getenv("outside_index_root")
f0_min = 50
f0_max = 1100
protect = 33
volRatio = 25
indexRate = 20

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.thread = None
        
        # button triggers
        self.inferBtn.clicked.connect(self.inference)
        self.inferAudioBtn.clicked.connect(self.openAudioFile)

        # sliders
        # condition for sub 1 values
        self.protectSlider.valueChanged.connect(
            lambda: self.divide(
                self.protectVal, self.protectSlider.value()
            )
        )
        self.volRatioSlider.valueChanged.connect(
            lambda: self.divide(
                self.volRatioVal, self.volRatioSlider.value()
            )
        )
        self.indexRateSlider.valueChanged.connect(
            lambda: self.divide(
                self.indexRateVal, self.indexRateSlider.value()
            )
        )

        # set min/max freq
        self.minFreqSlider.setValue(f0_min)
        self.maxFreqSlider.setValue(f0_max)
        self.minFreqSpinBox.setValue(f0_min)
        self.maxFreqSpinBox.setValue(f0_max)

        # set protect
        self.protectSlider.setValue(protect)

        # set vol ratio
        self.volRatioSlider.setValue(volRatio)

        # set index
        self.indexRateSlider.setValue(indexRate)

        # combo menus
        # populate f0 choices
        f0s = [
            "rmvpe",
            "mangio-crepe",
            "harvest",
            "fcpe",
            "hybrid"
        ]
        self.f0Choice.addItems(f0s)
        self.hybridF0Choices.addItems(f0s[:-1])

        # hybrid f0 condition
        self.f0Choice.activated.connect(self.toggleHybrid)
        self.toggleHybrid() # trigger this once since f0 choice doesnt change on startup

        # models for inference
        for name in os.listdir(weight_root):
            if name.endswith(".pth"):
                self.modelInfer.addItem(name)
        
        # index files
        for root, _, files in chain(
            os.walk(index_root),
            os.walk(outside_index_root)
        ):
            for name in files:
                if name.endswith(".index") and "trained" not in name:
                    self.indexInfer.addItem("%s\\%s" % (root, name))
        
        # get current model name
        self.setSid()
        self.loadModel()

        # model change condition
        self.modelInfer.activated.connect(self.setSid)
        self.modelInfer.activated.connect(self.loadModel)
    
    def setSid(self):
        self.sid = self.modelInfer.currentText()
    
    def divide(self, item: QLineEdit, val):
        item.setText(str(val / 100))
    
    def toggleHybrid(self):
        isHybrid = self.f0Choice.currentText() == "hybrid"
        self.hybridF0Choices.setEnabled(isHybrid)
        self.hybridF0Label.setEnabled(isHybrid)
    
    def loadModel(self):
        _, _, _, _, indexFile = vc.get_vc(self.sid, False, False)
        index = self.indexInfer.findText(indexFile['value'], Qt.MatchFlag.MatchFixedString)
        if index >= 0:
            self.indexInfer.setCurrentIndex(index)
    
    def openAudioFile(self):
        audioDlg = QFileDialog.getOpenFileName(
            self,
            'Open file',
            '.',
            'Audio files (*.mp3 *.ogg *.flac *.wav)'
        )
        self.inferAudio.setText(audioDlg[0])
    
    def handle_inference_finished(self, info, audio):
        filename = f"audios/audio-{self.sid.split('.')[0]}-{int(time.time())}.wav"
        sf.write(filename, audio[1], audio[0])
        print(info)
        self.inferBtn.setEnabled(True)

    def inference(self):
        self.inferBtn.setEnabled(False)  # Disable the button while the inference is running

        # Create a new thread and connect the finished signal
        self.thread = InferenceThread(
            vc,
            self.inferAudio.text(),
            self.transposeVal.text(),
            self.f0Choice.currentText(),
            self.indexInfer.currentText(),
            float(self.indexRateVal.text()),
            float(self.volRatioVal.text()),
            float(self.protectVal.text()),
            self.minFreqSpinBox.value(),
            self.maxFreqSpinBox.value()
        )
        self.thread.finished.connect(self.handle_inference_finished)
        self.thread.start()

    def closeEvent(self, event):
        if self.thread and self.thread.isRunning():
            # Wait for the thread to finish before closing the application
            self.thread.quit()
            self.thread.wait()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())