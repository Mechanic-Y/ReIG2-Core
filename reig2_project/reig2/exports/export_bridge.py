import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

class ExportBridge:
    def __init__(self, font_path="reig2/assets/NotoSansJP-Regular.ttf"):
        self.font_prop = None
        if os.path.exists(font_path):
            self.font_prop = fm.FontProperties(fname=font_path)
            plt.rcParams['font.family'] = self.font_prop.get_name()

    def plot_history(self, alpha, beta, filename):
        plt.figure()
        plt.plot(alpha, label="Alpha")
        plt.plot(beta, label="Beta")
        title = "Resonance History"
        if self.font_prop:
            plt.title("共鳴履歴", fontproperties=self.font_prop)
        else:
            plt.title(title)
        plt.legend()
        plt.savefig(filename)
        plt.close()