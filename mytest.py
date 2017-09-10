# from lastpass-python.lastpass.vault import Vault
from lastpass import Vault

vault = Vault.open_remote('', '')
index = 0
print("Accounts:-------------------\n")
for i in vault.accounts:
    print(str(index) + ". " + str(i))
    index += 1
print("\n\n\nSecureNote:------------------\n")
index = 0
for i in vault.accounts:
    print(str(index) + ". " + str(i))
    index += 1
