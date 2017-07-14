from core.interpreter import interpreter
from core.banner import Banner
from sys import argv
from argparse import ArgumentParser, SUPPRESS

sample = """from core.module_obtainer import obtainer
info = {
        'author'            :'Creator name',
        'date'              :'Create date',
        'rank'              :'Rank of the module',
        'category'          :'Main category of the module',
        'path'              :'Module create path',
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


def main():
    parser = ArgumentParser(prog='PySploit',usage='python3 PySploit.py [options]',  add_help=False)
    help_arguments = parser.add_argument_group('help arguments')
    help_arguments.add_argument('-v', '--version', action='version', version="version 0.1")
    help_arguments.add_argument('-h', '--help', action='help', default=SUPPRESS, help='Show this help message and exit.')
    optional_arguments = parser.add_argument_group('optional arguments')
    optional_arguments.add_argument('-c', '--create', dest='filename', required=False, help='create module sample')
    args = parser.parse_args()
    if len(argv) > 1:
        if args.filename is not None:
            filename = open(args.filename, 'w')
            filename.write(sample)

    else:
        Banner()
        while True:
            interpreter().start_interpreter()

if __name__ == '__main__':
    main()
