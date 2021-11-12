
from pysmx.SM2 import generate_keypair
from pysmx.SM3 import hash_msg
import base64
import os

def gen_network_key():
    network_key = '0x' + os.urandom(32).hex()
    netwok_string = base64.b64encode(bytes(network_key, encoding='utf8')).decode('utf-8')

    return netwok_string

def gen_keypair():
    pk, sk = generate_keypair()
    node_address = '0x'+hash_msg(pk)[24:]
    node_key = '0x'+sk.hex()

    return node_address,node_key

def main():
    
    node_address,node_key = gen_keypair()
    print('network_key:'+' "'+gen_network_key()+'"')
    print("node_address:"+' "'+node_address+'"')
    print("node_key:"+' "'+node_key+'"')
    
if __name__ == '__main__':
    main()
