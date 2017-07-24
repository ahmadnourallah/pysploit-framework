from core.interpreter import interpreter
from core.banner import Banner
from sys import argv
from utilities.color import *
from utilities.files import *
from argparse import ArgumentParser, SUPPRESS
from subprocess import check_call, CalledProcessError, call
import os
import shutil
sample = """from core.module_obtainer import obtainer
info = {
        'author'            :'Creator name',
        'date'              :'Create date',
        'rank'              :'Rank of the module',
        'path'              :'Module create path',
        'category'          :'Main category of the module',
        'license'           :'Module license',
        'description'       :'Module description',
        'references'        :['References for further reading']
}
options = {
            'options_name'        :['require', 'description','value']
}
required = {
        'start_required'     :'False/True', # using default starter
        'check_required'     :'False/True' # module support on not support check option
}
def exploit(): # main exploit function
    pass # stuff to do
def check(): # check function if the module require it
    pass # stuff to do"""

def install():
    try:
        os.mkdir('/etc/pysploit-framework')
        os.mkdir('/etc/pysploit-framework/docs')
    except FileExistsError:
        print(red('\n[!]') + green(" /etc/pysploit-framework") + " folder is exist, try --unistall command before reinstall\n")
        exit()
    except PermissionError:
        print(red("\n[!]") + green(" You") + " should run command as root\n")
        exit()
    try:
        copy(['PySploit.py','core/','files','modules/','samples/','utilities/'], '/etc/pysploit-framework')
        copy(['README.md','LICENSE','pysploit'],'/etc/pysploit-framework/docs')
    except FileExistsError:
       print(red("\n[!]") + green(' Check') + " if all tool files exist and try again\n")
       exit()
    except PermissionError:
        print(red("\n[!]") + green(" You") + " should run command as root\n")
        exit()
    try:
        file = open('/bin/pysploit','w')
        file.write('cd /etc/pysploit-framework &> /dev/null')
        file.write('\npython3 PySploit.py $1 $2 $3 $4')
    except PermissionError:
        print(red("\n[!]") + green(" You") + " should run command as root\n")
        exit()
    try:
        call('chmod 777 /bin/pysploit', shell=True)
    except PermissionError:
        print(red("\n[!]") + green(" You") + " should run command as root\n")
        exit()
    else:
        print(blue('\n[CO]') + green(" Tool") + ' installed successfully type pysploit to run it\n')
def uninstall():
    try:
        rm('/etc/pysploit-framework/')
        rm('/bin/pysploit')
    except PermissionError:
        print(red("\n[!]") + green(" You") + " should run command as root\n")
        exit()
    except FileNotFoundError:
        print(red('\n[!]') + green(" Tool") + " does not installed on your device\n")
        exit()
    else:
        print(blue('\n[CO]') + green(" Tool") + ' uninstalled successfully\n')

def main():
    parser = ArgumentParser(prog='PySploit',usage='python3 PySploit.py [options]',  add_help=False)
    help_arguments = parser.add_argument_group('help arguments')
    help_arguments.add_argument('-v', '--version', action='version', version="version 1.2")
    help_arguments.add_argument('-h', '--help', action='help', default=SUPPRESS, help='show this help message and exit.')
    optional_arguments = parser.add_argument_group('optional arguments')
    optional_arguments.add_argument('-c', '--create', dest='filename', required=False, help='create module sample')
    optional_arguments.add_argument('-u', '--upgrade', required=False, action='store_true',  help='create module sample')
    optional_arguments.add_argument('-m', '--manual', required=False, action='store_true',  help='show tool man page')
    optional_arguments.add_argument('-i', '--install', required=False, action='store_true',  help='install tool on your computer')
    optional_arguments.add_argument('-un', '--uninstall', required=False, action='store_true',  help='uninstall tool from your computer')
    args = parser.parse_args()
    if len(argv) > 1:
        if args.filename is not None:
            filename = open(args.filename, 'w')
            filename.write(sample)
        elif args.upgrade == True:
            interpreter().check_upgrade()
        elif args.manual == True:
            try:
                check_call('man /etc/pysploit-framework/docs/pysploit',shell=True)
            except CalledProcessError:
                print(red('\n[!]') + green(' Tool') + " manual is not installed yet\n")
        elif args.install == True:
            install()
        elif args.uninstall == True:
            uninstall()
    else:
        Banner()
        while True:
            interpreter().start_interpreter()

if __name__ == '__main__':
    main()
