# BTC_KeypairGenerator

"The aim of this repo is to generate a random Bitcoin Keypair and showing address and wallet import format of the private key"

##  Use :

```
 ./btc_keypair [compressed] [address_prefix] 
```
compressed and address_prefix are both optional 
default compressed is False
default prefix is "00"

 `````
 ./btc_keypair 
 ./btc_keypair True
 ./btc_keypair True C4
 `````


### Requierements :

- base58  : pip install base58
- ecdsa   : pip install ecdsa
- secrets : pip install secrets



### Usefull links :

- [Checksum](https://learnmeabitcoin.com/technical/checksum)
- [Mnemonic](https://learnmeabitcoin.com/technical/mnemonic)
- [ECDSA](https://learnmeabitcoin.com/technical/ecdsa)
- [Private_Keys](https://learnmeabitcoin.com/technical/private-key)
- [Public_Keys](https://learnmeabitcoin.com/technical/public-key)
- [Adress](https://learnmeabitcoin.com/technical/address)
- [Extended_Keys](https://learnmeabitcoin.com/technical/extended-keys)

Thanks to https://learnmeabitcoin.com/ for all the informations needed to understand the Bitcoin Protocol.
