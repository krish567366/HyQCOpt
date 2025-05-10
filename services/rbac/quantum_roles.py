from hyqcopt import set_job_policy

class QuantumRBAC:
    roles = {
        "researcher": {
            "max_qubits": 50,
            "allowed_backends": ["simulator"]
        },
        "enterprise": {
            "max_qubits": 1000,
            "allowed_backends": ["qpu", "simulator"]
        }
    }

    def enforce_policy(self, user, job_config):
        policy = self.roles[user.role]
        
        if job_config['qubits'] > policy['max_qubits']:
            raise ValueError("Qubit limit exceeded")
            
        if job_config['backend'] not in policy['allowed_backends']:
            raise ValueError("Backend not allowed")
        
        set_job_policy(job_config['id'], policy)