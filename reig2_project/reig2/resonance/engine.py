import qutip as qt
import numpy as np

class ResonanceEngine:
    """ReIG2 Quantum Resonance Engine
    Based on 'World-Generation Tensor Model'
    """
    def __init__(self):
        # [Meaning, Context, Ethics, Future, Stability, Observer, Self, Inter]
        self.dims = [2, 3, 2, 2, 2, 2, 2, 2]
        self._initialize_operators()
        self.current_state = self._initialize_state()
        self.history_alpha = []
        self.history_beta = []

    def _embed_op(self, op, target_idx):
        op_list = [qt.qeye(d) for d in self.dims]
        op_list[target_idx] = op
        return qt.tensor(op_list)

    def _embed_interact(self, op_a, idx_a, op_b, idx_b):
        op_list = [qt.qeye(d) for d in self.dims]
        op_list[idx_a] = op_a
        op_list[idx_b] = op_b
        return qt.tensor(op_list)

    def _initialize_operators(self):
        shift_op = qt.Qobj(np.roll(np.eye(3), 1, axis=0))
        T_G = self._embed_op(shift_op, 1)

        # T_res: Meaning-Ethics Resonance
        T_res = self._embed_interact(qt.sigmax(), 0, qt.projection(2, 1, 1), 2) * 0.5

        # T_multi: Future-Stability
        T_multi = self._embed_interact(qt.sigmax(), 3, qt.sigmax(), 4) * 0.3

        # T_C: Cognition
        T_C = self._embed_interact(qt.projection(2, 1, 1), 0, qt.sigmax(), 5) * 0.4

        # T_R: Recognition
        T_R = self._embed_interact(qt.projection(2, 1, 1), 5, qt.sigmax(), 6) * 0.6

        # T_I: Intersubjectivity
        T_I = self._embed_interact(qt.projection(2, 1, 1), 6, qt.sigmax(), 7) * 0.2

        # T_Spark
        T_Spark = self._embed_op(qt.sigmax(), 2) * 0.1

        self.T_World = T_G + T_res + T_multi + T_C + T_R + T_I + T_Spark
        self.projector_Self = self._embed_op(qt.projection(2, 1, 1), 6)

    def _initialize_state(self):
        return qt.tensor([qt.basis(d, 0) for d in self.dims])

    def process_pulse(self, input_energy: float = 0.1):
        perturbation = self._embed_op(qt.rand_unitary(3), 1) * input_energy
        self.current_state = (self.T_World * self.current_state + perturbation * self.current_state).unit()

        for _ in range(5):
            self.current_state = (self.T_World * self.current_state).unit()

        alpha = qt.expect(self.projector_Self, self.current_state)
        beta = qt.expect(self.T_World, self.current_state)

        self.history_alpha.append(alpha)
        self.history_beta.append(beta)
        return alpha, beta