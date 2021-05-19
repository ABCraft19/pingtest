import getpass
mdp="test"
 
user_mdp=getpass.getpass('ip du serveur')

print ("le serveur {mdp} en en cours de ping ".format(mdp=user_mdp))

import subprocess

Host = ("{mdp}".format(mdp=user_mdp))

ping = subprocess.Popen(
    ["ping", Host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

out, error = ping.communicate()
print ("{out}".format(out=out))

import keyboard
print ("appuyer sur une p pour fermer le cmd")
while True:
    if keyboard.read_key() == "p":
        print("aurevoir")
        break