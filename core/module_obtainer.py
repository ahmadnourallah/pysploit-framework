from os import getcwd
from sys import path
from utilities.color import *
from imp import reload

class obtainer(object):
    def obtaining_info(self, module):
        try:
            self.category = str(module).split('/')[-1+1]
            self.module_name = str(module).split('/')[-1]
            self.module_path = str(getcwd() + '/module/{}.py'.format(module)).split('/')
            self.module_path.remove(self.module_name+'.py')
            self.module_path = '/'.join(self.module_path)
            path.append(self.module_path)
        except IndexError:
            print('\n' + red('[!]') + green(' Module') + ' not found\n')
            return False

        try:
            try:
                module = __import__(self.module_name)
            except ValueError:
                print(red('\n[!]') + green(' Please') + ' enter the full module name\n')
                return False
            reload(module)
            self.exploit = getattr(__import__(self.module_name, fromlist=['exploit']), 'exploit')
            self.options = getattr(__import__(self.module_name, fromlist=['options']), 'options')
            self.info = getattr(__import__(self.module_name, fromlist=['info']), 'info')
            self.required = getattr(__import__(self.module_name, fromlist=['required']), 'required')
            if self.required['check_required'] == True or self.required['check_required'] == "True" or self.required['check_required'] == "TRUE":
                self.check = getattr(__import__(self.module_name, fromlist=['check']), 'check')
        except AttributeError:
            print('\n' + red('[!]') + green(' You') + ' must define all the requirement\n')
            pass
            return False
        except SyntaxError:
            print('\n' + red('[!]') + green(' Check') + ' for your syntax and in your module and try again\n')
        except ImportError:
            print('\n' + red('[!]') + green(' Module') + ' not found\n')
            return False
        else:
            return True
