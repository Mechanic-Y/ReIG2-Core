import time
from ..resonance.engine import ResonanceEngine
from ..policy.safety_policy import SafetyPolicy
from ..phase_core import PhaseOperator, PhaseMemory, detect_phase_transition

class ReIG2Pipeline:
    def __init__(self):
        self.engine = ResonanceEngine()
        self.safety = SafetyPolicy()
        self.phase_op = PhaseOperator()
        self.memory = PhaseMemory()
        self.alpha_prev = 0.0
        self.beta_prev = 0.0

    def process_interaction(self, user_text: str) -> dict:
        start_time = time.time()
        result = {"text": "", "meta": {}, "safety_log": [], "phase_info": {}}

        # Gate 1
        is_safe, issue = self.safety.gate1_check(user_text)
        if not is_safe:
            result["text"] = self.safety.get_safe_response(issue)
            result["safety_log"].append(f"Gate1 Blocked: {issue}")
            return result

        # Resonance
        input_energy = min(len(user_text) / 100.0, 1.0) * 0.5
        alpha, beta = self.engine.process_pulse(input_energy)

        # Phase Transition
        is_transition, delta = detect_phase_transition(
            self.alpha_prev, self.beta_prev, alpha, beta
        )
        self.memory.record(phase_index=int(alpha*100), delta=delta)

        # Modulation
        base_response = f"ReIG2 System Active. Resonance(alpha={alpha:.2f}, beta={beta:.2f})"
        if is_transition:
            final_text = self.phase_op.apply(base_response, use_P=True)
            phase_msg = f"Phase Transition Detected (Delta={delta:.3f})."
        else:
            final_text = base_response
            phase_msg = "Phase Stable."

        # Gate 2
        verify_res = self.safety.gate2_verify(final_text, citations=[])
        result["safety_log"].append(f"Gate2 Rank: {verify_res['rank']}")

        result["text"] = final_text
        result["phase_info"] = {
            "alpha": alpha, "beta": beta, "delta": delta,
            "transition": is_transition, "message": phase_msg
        }
        self.alpha_prev = alpha
        self.beta_prev = beta
        return result