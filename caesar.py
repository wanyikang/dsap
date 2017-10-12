# -*- coding: utf-8 -*-
# caesar cipher for Hebrew. There are 2 steps to modify the cipher algorithm:
# 1, modify the encoder and decoder table, actually you can user dict
# 2, modify corresponding _transform method

class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""
    unallocated_codepoint = [
            0x590, 0x5c8, 0x5c9, 0x5ca, 0x5cb, 0x5cc, 0x5cd, 0x5ce, 0x5cf, 0x5eb,
            0x5ec, 0x5ed, 0x5ee, 0x5ef, 0x5f5, 0x5f6, 0x5f7, 0x5f8, 0x5f9, 0x5fa,
            0x5fb, 0x5fc, 0x5fd, 0x5fe, 0x5ff, 0xfb37, 0xfb3d, 0xfb3f, 0xfb42, 0xfb45]

    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        encoder, decoder = self._make_coder_dicts(shift)
        self._encoder = encoder
        self._decoder = decoder

    def _make_hebrew_char_list(self):
        hblist = []
        for i in range(0x0590, 0x0600):
            if i not in self.unallocated_codepoint:
                hblist.append(unichr(i))
        for i in range(0xfb1d, 0xfb50):
            if i not in self.unallocated_codepoint:
                hblist.append(unichr(i))
        return hblist

    def _make_coder_dicts(self, shift):
        encoder = {}
        decoder = {}
        hb = self._make_hebrew_char_list()
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
            if 0x590 < ord(msg[k]) < 0xfb50:
                msg[k] = coder[msg[k]]
        return u"".join(msg)

if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "נתראה יותר מאוחר"
    message = message.decode('utf-8')
    coded = cipher.encrypt(message)
    print 'Secret: ', coded
    answer = cipher.decrypt(coded)
    print 'Message:', answer

