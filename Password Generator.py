import hashlib
import getpass
import os
import textwrap
import binascii

def gen_passwd(master_passwd, domain_name, username, length):
    salt = domain_name + username + str(length)
    rawpasswd = binascii.hexlify(hashlib.pbkdf2_hmac("sha256", master_passwd.encode(), salt.encode(), 1000000))
    strpasswd = rawpasswd.decode("utf-8")
    return strpasswd[:length]        

def main():
    print(textwrap.fill("This program creates secure passwords up to 64 characters long. The passwords contain combinations of letters and numbers. If you forget your password, you can always regenerate it, as long as you use the same master password."))
    password_match = False
    while password_match == False:
        master_passwd = getpass.getpass("Enter master password: ")
        check_passwd = getpass.getpass("Repeat master password or press enter to view password: ")
        if check_passwd == "":
            os.system("cls" if os.name == "nt" else "clear")
            print(master_passwd)
            match = input("Is this your password? (y/n) ")
            if match == "y":
                password_match = True
            os.system("cls" if os.name == "nt" else "clear")
        elif master_passwd == check_passwd:
            password_match = True
        else:
            print("Passwords didn't match.")
    
    first_loop = True
    while 0 == 0:
        if first_loop == False:
            stop = input(textwrap.fill("Press enter to generate another password or enter any input to stop.") + " ")
            os.system("cls" if os.name == "nt" else "clear")
            if stop != "":
                break
        else:
            first_loop = False
        domain_name = input(textwrap.fill("Please enter the domain name of the account (or something else you remember it by):") + " ")
        username = input("Please enter your username for this account: ")
        length = -1
        while length == -1:
            try:
                length = int(input("Please enter the length of the password (max. 64): "))
                if length <= 0:
                    raise ValueError()
            except ValueError:
                print("Please enter a positive number")
        passwd = gen_passwd(master_passwd, domain_name, username, length)
        print("Your password is", passwd)

os.system("cls" if os.name == "nt" else "clear")
main()
