from cryptography.hazmat.primitives.asymmetric import kyber

class PQCAuthentication:
    def __init__(self):
        self.private_key, self.public_key = kyber.generate_keypair()
    
    def generate_token(self, tenant_id):
        ciphertext = kyber.enc(self.public_key, tenant_id.encode())
        return base64.b64encode(ciphertext)

    def validate_token(self, token):
        plaintext = kyber.dec(self.private_key, base64.b64decode(token))
        return plaintext.decode()