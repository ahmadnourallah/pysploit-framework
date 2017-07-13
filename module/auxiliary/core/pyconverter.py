from utilities.color import *
from core.module_obtainer import obtainer
from subprocess import CalledProcessError, check_output

info = {
        'author'            :'Ahmad Nourallah',
        'date'              :'2017/7/7',
        'rank'              :'Excellent',
        'path'              :'auxiliary/core/pyconverter.py',
        'category'          :'auxiliary',
        'license'           :'GPL-2.0',
        'description'       :'convert your module from python version 2.x to python version 3\n             easy to work on framework without any problems',
        'references'        :['docs.python.org/2/library/2to3.html']
}
options = {
            'path'                :['Yes', 'use to set path file to convert','']
}
required = {
        'start_required'     :'True',
        'check_required'     :'False'
}

def exploit():
    try:
        print(obtainer.options['path'][2])
        output = check_output('2to3 -w --no-diffs {0} &> /dev/null'.format(obtainer.options['path'][2], shell=True))
    except CalledProcessError:
        print(red('[!]') + green(' Check if you installed 2to3 program and try again'))
        pass
    except FileNotFoundError:
        print(red('[!]') + green(' The') + ' file you entered is not exist')
        pass
    else:
        print(output)
