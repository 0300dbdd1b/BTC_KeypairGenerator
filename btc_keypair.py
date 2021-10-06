


### This file contain all the functions to interact from a mnemonic seed to the BTC Protocol
import hmac
import binascii
import ecdsa
import base58
import sys
from hashlib import sha512, sha256, new
from secrets import randbits

def get_bip32masterkey(seed):
	master_key = hmac.new(("Bitcoin seed").encode(), binascii.a2b_hex(seed) , sha512).hexdigest()
	return (master_key)


def get_xpub(xpriv, compressed=False):
	xpriv = bytes.fromhex(xpriv)
	signing_key = ecdsa.SigningKey.from_string(xpriv, curve = ecdsa.SECP256k1)
	verifying_key = signing_key.get_verifying_key()
	uncompressed_k = (bytes.fromhex("04") + verifying_key.to_string()).hex()
	compressed_k =  i2o_ECPublicKey(verifying_key.pubkey, True)
	if (compressed == True):
		return (compressed_k)
	else:
		return (uncompressed_k)


def get_addr(xpub, prefix):
	xpub_hash = get_xpub_hash(xpub)
	checksum_token = checksum((prefix + xpub_hash))
	addr = prefix + xpub_hash + checksum_token
	addr = base58.b58encode(bytes.fromhex(addr))
	addr = addr.decode()
	return (str(addr))


def get_xpub_hash(xpub):
	xpub_hash = sha256(binascii.a2b_hex(xpub)).hexdigest()
	xpub_hash = new('ripemd160', binascii.a2b_hex(xpub_hash)).hexdigest()
	return (xpub_hash)


def get_child_key(master_key, index):
	print(hmac.new(master_key.encode(), index).hexdigest())

# pywallet openssl private key implementation
def i2o_ECPublicKey(pubkey, compressed=False):
	# public keys are 65 bytes long (520 bits)
	# 0x04 + 32-byte X-coordinate + 32-byte Y-coordinate
	# 0x00 = point at infinity, 0x02 and 0x03 = compressed, 0x04 = uncompressed
	# compressed keys: <sign> <x> where <sign> is 0x02 if y is even and 0x03 if y is odd
	if compressed:
		if pubkey.point.y() & 1:
			key = '03' + '%064x' % pubkey.point.x()
		else:
			key = '02' + '%064x' % pubkey.point.x()
	else:
		key = '04' + \
			  '%064x' % pubkey.point.x() + \
			  '%064x' % pubkey.point.y()

	return key


def checksum(data):
	checksum_token = sha256(binascii.a2b_hex(data)).hexdigest()
	checksum_token = sha256(binascii.a2b_hex(checksum_token)).hexdigest()
	return (checksum_token[:8])


def wallet_import_format(xpriv, prefix="80", compressed=True):
	compressed_token = "01"
	if (compressed == False):
		compressed_token = ""
	token = checksum(prefix + xpriv + compressed_token)
	data = prefix + xpriv + compressed_token + token
	wif = base58.b58encode(binascii.a2b_hex(data))
	wif = wif.decode()
	return (wif)


def resize_bin(bin, nbits):
	if nbits - len(bin) > 0:
		for i in range(0, nbits - len(bin)):
			bin = "0" + bin
	return (bin)


def putnbr_base(nb, base):
	out = ""
	nbr = nb
	while (nbr >= base):
		out =  str(int(nbr % base)) + " " + out
		nbr = int(nbr // base) 
	out =  str(int(nbr % base)) + " " + out
	return(out)



def main():
	compressed_xpub = True
	compressed_wif = True
	prefix = "00"
	base = 256
	base_spec = False
	if (len(sys.argv) == 2):
		compressed_xpub = bool(sys.argv[1])
	if (len(sys.argv) == 3):
		compressed_xpub = bool(sys.argv[1])
		prefix = str(sys.argv[2])
	if (len(sys.argv) == 4):
		compressed_xpub = bool(sys.argv[1])
		prefix = str(sys.argv[2])
		compressed_wif = bool(sys.argv[3])
	if (len(sys.argv) == 5): 
		compressed_xpub = bool(sys.argv[1])
		prefix = str(sys.argv[2])
		compressed_wif = bool(sys.argv[3])
		base = int(sys.argv[4])
		base_spec = True
	entropy = randbits(256)
	xpriv = hex(entropy)[2:]
	if (len(xpriv) < 64):
		xpriv = resize_bin(xpriv, 64)
	xpub = get_xpub(xpriv, compressed_xpub)
	xpub_b58 = base58.b58encode(bytes.fromhex(xpub)).decode()
	xpriv_b58 = base58.b58encode(bytes.fromhex(xpriv)).decode()
	xpub_hash = get_xpub_hash(xpub)
	address = get_addr(xpub, prefix)
	wif = wallet_import_format(xpriv, "80" ,compressed_wif)
	print("Compressed_xpub : {}      Prefix : {}       Compressed_wif : {}\n".format(compressed_xpub, prefix, compressed_wif))
	print("xpriv_hex\t: {}\nxpriv_b58\t: {}\nxpub_hex\t: {}\nxpub_b58\t: {}\nxpub_hash\t: {}\naddress\t\t: {}\nWIF\t\t: {}\n".format(xpriv, xpriv_b58, xpub, xpub_b58, xpub_hash, address, wif))
	print("=================================")
	if (base_spec == True)
		print("xpriv in base ", base, "       :")
		print(putnbr_base(int(xpriv, 16), base))

	
main()
