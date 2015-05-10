# SHA-256 Password Generator
# Copyright 2015 Daniel Szoke
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
 

import hashlib
import getpass
import os
import textwrap

def gen_passwd(master_passwd, domain_name, username, length):
    to_hash = master_passwd + domain_name + username + str(length)
    hashobj = hashlib.sha256(to_hash.encode())
    hashdig = hashobj.hexdigest()
    return hashdig[:length]        

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
