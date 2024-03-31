from PyQt6.QtCore import QThread, pyqtSignal

class InferenceThread(QThread):
    finished = pyqtSignal(str, list)  # Define a signal to emit the result

    def __init__(self, vc, audio_path, transpose, f0_choice, index_file, index_rate, vol_ratio, protect, min_freq, max_freq):
        super().__init__()
        self.vc = vc
        self.audio_path = audio_path
        self.transpose = transpose
        self.f0_choice = f0_choice
        self.index_file = index_file
        self.index_rate = index_rate
        self.vol_ratio = vol_ratio
        self.protect = protect
        self.min_freq = min_freq
        self.max_freq = max_freq

    def run(self):
        info, audio = self.vc.vc_single(
            0,
            self.audio_path,
            self.transpose,
            None,
            self.f0_choice,
            self.index_file,
            None,
            self.index_rate,
            4,
            40000,
            self.vol_ratio,
            self.protect,
            self.min_freq,
            self.max_freq
        )
        self.finished.emit(info, audio)