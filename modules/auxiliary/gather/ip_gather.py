import socket
from core.module_obtainer import obtainer
info = {
        'author'            :'Ahmad Nourallah',
        'date'              :'2017/7/11',
        'rank'              :'Excellent',
        'path'              :'auxiliary/gather/ip_gather.py',
        'category'          :'auxiliary',
        'license'           :'GPL-2.0',
        'description'       :'simple module to get ip address from host name',
        'references'        :['docs.python.org/3/library/socket.html#socket.gethostbyname']
}
options = {
            'target'                :['Yes', 'use to set target','']
}
required = {
        'start_required'     :'True',
        'check_required'     :'False'
}

def exploit():
    """ main exploit function """
    try:
        var = socket.gethostbyname(obtainer.options['target'][2])
        print(var)
    except socket.gaierror:
        print(Red + "Error:" + White + "You should enter right url.")
        return False
