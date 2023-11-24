from secret import tug
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

#your_ticket='0x5dc3e1d09a42233cc160a1c5bba4100f2556b5ef933d20c5ca'
