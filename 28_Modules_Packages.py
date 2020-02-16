# PyPi with pip install

# PyPi is a repository for open-source third-party packages

# when we install python 'pip' is also installed along with it
#  -- except ubuntu
#  -- use command on terminal for ubuntu to install pip for python3  `sudo apt install python3-pip`

# There are numerous packages available for most of the business case you think of

# pip is a command line tool [ensure your firewall access is available for pip install]
# ex : pip install <package-name>
# run the below command on your terminal/cmd
#
#  `pip install requests` [for ubuntu - `pip3 install requests`]
#
# [requests - is a package used to handle http(s) requests]
#
# another example
# `pip install colorama`
#
# [colorama is used to print colored texts on the command line or terminal]


from colorama import Fore
from colorama import init
init()


print(Fore.RED + "some red texts")
print(Fore.GREEN + "something in green")
print(Fore.CYAN + "something in cyan")
print(Fore.YELLOW + "something in yellow")

print("However the following any output to STDOUT will be in previous set color")
print("To handle this call to init should be as: init(autoreset=True)")

# any workflow/use case simply do a google search

'''

How to create your own module and packages

Ideally, modules are just .py scripts that you call in another.py scripts
Packages are collections of modules

Lets create 2 files 
 - mymodule.py
 - 30_my_program.py
 
both in same location

'''
