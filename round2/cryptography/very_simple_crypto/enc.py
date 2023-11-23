from flag import tug
def encr(msg, x, y):
    msg2 = int.from_bytes(msg.encode(), byteorder='big') #ene from_bytes zasah
    ct = pow(msg2, y, x)
    return ct

til = 882564595536224140639625987659416029426239230804614613279163
f4 = 65537 #chnge
ctext = hex(encr(tug, til, f4))[2:]
with open('ct.txt','w') as f:
	f.write(ctext)

