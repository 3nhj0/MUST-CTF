from Crypto.Util.Padding import pad
from secret import Tug
kii = '9769769769769769'.encode()  

def custom_encrypt(pt):
    pt = bytes.fromhex(pt)
    enum = pad(pt + Tug, 16)
    sub = bytearray()
    for i, byte in enumerate(enum):
        kii_byte = kii[i % len(kii)]
        sub.append(byte ^ kii_byte)
    swap = sub[::-1]
    ct = swap.hex()
    return {"ciphertext": ct}
#{'ciphertext': '3e31303e31303e4b035a0e0f0050560d08025601005558014c7f62746d65627408070608070608070608070608070608'}