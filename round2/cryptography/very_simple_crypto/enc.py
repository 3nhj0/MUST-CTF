from flag import tug
def encr(msg, x, y):
    msg2 = int.from_bytes(msg, byteorder='big')
    ct = pow(msg2, y, x)
    return ct

chosen = 65537
seat_token = 882564595536224140639625987659416029426239230804614613279163
encd = hex(encr(tug, seat_token, chosen))[2:]
with open('ct.txt','w') as f:
	f.write(encd)
print("your_ticket",encd)

#your_ticket='0x8081d27d43aa21d16a5ecb683977c03df9f823fb737efd965f'
