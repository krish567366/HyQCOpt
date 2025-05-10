from jose import JWTError, jwt
from cryptography.hazmat.primitives.asymmetric import kyber

class QuantumAuth:
    def __init__(self):
        self.private_key, self.public_key = kyber.generate_keypair()
        
    def create_token(self, tenant_id: str) -> str:
        """Generate quantum-safe JWT"""
        return jwt.encode(
            {'tenant': tenant_id},
            self.private_key,
            algorithm='KYBER'
        )

    def validate_token(self, token: str) -> dict:
        """Verify quantum-safe JWT"""
        try:
            return jwt.decode(
                token,
                self.public_key,
                algorithms=['KYBER']
            )
        except JWTError:
            raise AuthError("Invalid token")