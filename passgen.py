# Import
import os
import secrets
import string
import pyperclip as pc

# Header
os.system('color 2')
print(" ")
print("      ███████╗ ██╗ ███╗  ██╗  █████╗  ██╗             ██████╗  ███████╗ ███╗  ██╗")
print("      ██╔════╝ ██║ ████╗ ██║ ██╔══██╗ ██║             ██╔════╝ ██╔════╝ ████╗ ██║")
print("      █████╗   ██║ ██╔██╗██║ ███████║ ██║             ██║  ██╗ █████╗   ██╔██╗██║")
print("      ██╔══╝   ██║ ██║╚████║ ██╔══██║ ██║             ██║  ╚██╗██╔══╝   ██║╚████║")
print("      ██║      ██║ ██║ ╚███║ ██║  ██║ ███████╗        ╚██████╔╝███████╗ ██║ ╚███║")
print("      ╚═╝      ╚═╝ ╚═╝  ╚══╝ ╚═╝  ╚═╝ ╚══════╝         ╚═════╝ ╚══════╝ ╚═╝  ╚══╝")
print(" ")
chars = string.digits + string.ascii_letters + string.punctuation
pc.copy(''.join(secrets.choice(chars) for _ in range(40)))
text = pc.paste()
print(text)
print(" ")
print("Your New Password ↑ was copy to your Clipboard")
# END
wait = input(" ")
