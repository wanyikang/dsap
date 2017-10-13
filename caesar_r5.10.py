# -*- coding: utf-8 -*-
# this is exercise r5.10

class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""

    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        self._forward = [chr((k + shift) % 26 + ord('A')) for k in range(26)]
        self._backward = [chr((k - shift) % 26 + ord('A')) for k in range(26)]

    def encrypt(self, message):
        """Return string representing encripted message."""
        return  self._transform(message, self._forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return  self._transform(secret, self._backward)

    def _transform(self, original, code):
        """Utility to perform transformation based on given code string."""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')                  # index from 0 to 25
                msg[k] = code[j]                            # replace this character
        return ''.join(msg)

if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)
