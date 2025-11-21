import os, json

class PhaseOperator:
    def __init__(self, rotation_depth=0.3, expansion_gain=0.6):
        self.rotation_depth = rotation_depth
        self.expansion_gain = expansion_gain

    def apply(self, text, use_R=True, use_E=True, use_P=True):
        if use_R: text = f"From another perspective: {text}"
        if use_E: text = text + " (Expanded context applied.)"
        if use_P: text = text + " [Phase Shift Detected]"
        return text

class PhaseMemory:
    def __init__(self, path="reig2/storage/phase_profile.json", limit=32):
        self.path = path
        self.limit = limit
        self.history = []

    def record(self, phase_index, delta, mode="Phase-Resonance"):
        self.history.append({"idx": phase_index, "delta": delta})
        if len(self.history) > self.limit: self.history.pop(0)

def detect_phase_transition(a_prev, b_prev, a, b, threshold=0.35):
    delta = abs(a - a_prev) + abs(b - b_prev)
    return (delta > threshold), round(delta, 3)