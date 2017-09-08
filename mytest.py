# from lastpass-python.lastpass.vault import Vault
from lastpass import Vault

vault = Vault.open_remote('', '')
index = 0
for i in vault.accounts:
    print("{} \n name:{} \n username:{} \n password:{} \n url:{} \n group:{} \n other:{} \n\n".format(index + 1, i.name, i.username, i.password, i.url, i.group, i.other))
    index += 1;
