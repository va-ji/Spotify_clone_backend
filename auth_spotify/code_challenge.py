import math
import random
import hashlib
import base64

class CodeChallenge:
    @staticmethod
    def _generate_code_verifier(self,length):
        text = ''
        possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

        for  i in range(length) :
          text += possible.charAt(math.floor(random.random() * possible.length))

        return text

    @staticmethod
    def generate_code_challenge(self):
        
        code_verifier = self.generate_code_verifier(60)

       # Encode the code verifier as bytes using UTF-8
        code_verifier_bytes = code_verifier.encode('utf-8')

        # Generate a SHA-256 digest of the code verifier
        digest = hashlib.sha256(code_verifier_bytes).digest()

        # Encode the digest as Base64url
        base64_bytes = base64.urlsafe_b64encode(digest).rstrip(b'=')
        base64_string = base64_bytes.decode('utf-8').replace('+', '-').replace('/', '_')

        return base64_string