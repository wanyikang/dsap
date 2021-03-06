# -*- coding: utf-8 -*-
# this is exercise p5.34
class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""
    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        encoder, decoder = self._make_coder_dicts(shift)
        self._encoder = encoder
        self._decoder = decoder

    def _make_alphabet_char_list(self):
        hblist = []
        for i in range(0x41, 0x5a):
            hblist.append(unichr(i))
        for i in range(0x61, 0x7b):
            hblist.append(unichr(i))
        return hblist

    def _make_coder_dicts(self, shift):
        encoder = {}
        decoder = {}
        hb = self._make_alphabet_char_list()
        hlen = len(hb)
        for i in range(hlen):
            encoder[hb[i]] = hb[(i + shift) % hlen]
        for i in range(hlen):
            decoder[hb[i]] = hb[(i - shift) % hlen]
        return (encoder, decoder)

    def encrypt(self, message):
        """Return string representing encripted message."""
        return  self._transform(message, self._encoder)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return  self._transform(secret, self._decoder)

    def _transform(self, original, coder):
        """Utility to perform transformation based on given code string."""
        msg = list(original)
        for k in range(len(msg)):
            if 0x40 < ord(msg[k]) < 0x5a or 0x60 < ord(msg[k]) < 0x7b:
                msg[k] = coder[msg[k]]
        return u"".join(msg)

if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "This is MacBook Pro!"
    message = message.decode('utf-8')
    coded = cipher.encrypt(message)
    print 'Secret: ', coded
    answer = cipher.decrypt(coded)
    print 'Message:', answer

