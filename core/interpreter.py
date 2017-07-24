from utilities.color import * # import utilites
from core.main_completer import completer # completer import
import os
from imp import reload
from urllib.request import urlopen
from urllib.error import URLError

class interpreter(object):
    def search_module(query):
        import utilities.files
        from core.module_obtainer import obtainer
        reload(utilities.files)
        from utilities.files import count_subfolders_files
        print('{:44}{:29}'.format('\nModules','Description'))
        print('{:43}{:29}'.format('-------','-----------'))
        count_subfolders_files('modules')
        unfiltered_result = []
        result = []
        for first_result in count_subfolders_files.result:
            for second_result in first_result:
                unfiltered_result.append(''.join(second_result))
                for final_result in unfiltered_result:
                    if final_result.endswith('.pyc') or final_result.startswith('__init__') or not final_result.endswith('.py'):
                        unfiltered_result.remove(final_result)
        for filt_result in unfiltered_result:
            result.append(filt_result.split('.')[0])
        try:
            for i in range(0,10):
                for root, dirs, files in os.walk('modules'):
                    if query in root+result[i]:
                        if result[i]+'.py' in files:
                            path = os.path.join(root, result[i]+'.py')
                            path = path.split('/')
                            path_first_index = path[0]
                            path.remove(path_first_index)
                            path = '/'.join(path)
                            if obtainer.description_obtainer(obtainer,path.split('.py')[0]):
                                print('{:44}{:44}'.format(path.split('.py')[0],obtainer.info['description']))
        except IndexError:
            pass
        except ImportError:
            pass

        print('')
    def check_upgrade(self):
        try:
            self.current_version = open('core/version.txt','r').read()
            self.new_version = urlopen('https://raw.githubusercontent.com/ahmadnourallah/pysploit-framework/master/core/version.txt').read()
            if float(self.current_version) < float(self.new_version):
                print(green("\n[~]") + blue(" Congratulations") + " new version avaliable go to 'https://github.com/ahmadnourallah/pysploit-framework to download it :)\n")
            else:
                print(red('\n[!]') + green(' You') + " have the latest version\n")
        except FileNotFoundError:
            print(red('\n[!]') + green(' Ohhhh,') + ' check if core/version.txt file is exist and try again\n')
            pass
        except URLError:
            print(red('\n[!]') + green(' check') + " your internet connection and try again\n")
            pass
    def start_interpreter(self):
        completer()
        from core.validator import validator
        while True:
            try:
                self.main_ask = input(underline("PySploit") + " >> ").split()
                validator(self.main_ask).validate_interpreter_mode()
            except (KeyboardInterrupt,EOFError):
                print('\n' + red('\n[!]') + green(' type') + gray(' exit') + ' to close the program\n')
