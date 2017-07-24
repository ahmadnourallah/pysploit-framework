from __main__ import *
from utilities.color import * # import utilites
from utilities.screen_cleaner import clear # import utilites
from core.banner import Banner # import banner
from imp import reload # import reload function from imp module
from os import system
from core.module_obtainer import obtainer

class validator(object):
    def __init__(self, command):
        self.command = command
    def validate_interpreter_mode(self):
        try:
            if self.command[0] == "clear" or self.command[0] == "Clear" or self.command[0] == "CLEAR":
                clear()
            elif self.command[0] == 'search' or self.command[0] == 'Search' or self.command[0] == 'SEARCH':
                try:
                    interpreter.search_module(query = self.command[1])
                except IndexError:
                    print(red('\n[!]') + green(' Invaild') + " syntax you should enter search query\n")
                except TypeError:
                    pass
            elif self.command[0] == "banner" or self.command[0] == "Banner" or self.command[0] == 'BANNER':
                Banner()
            elif self.command[0] == 'exit' or self.command[0] == "Exit" or self.command[0] == 'close' or self.command[0] == 'Close':
                exit(0)
            elif self.command[0] == "use" or self.command[0] == "Use" or self.command[0] == "USE":
                from core.module_obtainer import obtainer
                from core.module_interpreter import module_interpreter
                try:
                    if obtainer.obtaining_info(obtainer, self.command[1]):
                        while True:
                            module_interpreter(self.command[1].split('/')[-1], self.command[1].split('/')[-1+1],self.command[1])
                except IndexError:
                    print('\n' + red('[!]') + green(' You') + ' should enter the module name\n')
            elif self.command[0] == 'restart' or self.command[0] == 'Restart' or self.command[0] == 'RESTART':
                import core.module_interpreter # import module_interpreter module from core foloder
                print('\n' + blue('[~]') + ' restarting the program ..... success\n')
                reload(core.module_interpreter)
                from core.module_interpreter import module_interpreter
            elif self.command[0] == 'exec' or self.command[0] == 'execute':
                try:
                    self.command.remove('exec' if self.command[0] == 'exec' else 'execute')
                    system(' '.join(self.command))
                except IndexError:
                    print(red("\n[!] ") + green("Please ") + " enter the command\n")

            elif self.command[0] == 'upgrade' or self.command[0] == 'Upgrade' or self.command[0] == 'UPGRADE':
                interpreter.check_upgrade(interpreter)
            else:
                print('\n' + red('[!]') + green(' option') + ' not found\n')
        except (KeyboardInterrupt,EOFError):
            print('\n' + red('\n[!]') + green(' type') + gray(' exit') + ' to close the program\n')
        except IndexError:
            return None

    def validate_module_interpreter_mode(self):
        from core.module_interpreter import module_interpreter
        from core.interpreter import interpreter
        try:
            if self.command[0] == "clear" or self.command[0] == "Clear" or self.command[0] == "CLEAR":
                clear()
            elif self.command[0] == "banner" or self.command[0] == "Banner" or self.command[0] == "BANNER":
                Banner()
            elif self.command[0] == 'search' or self.command[0] == 'Search' or self.command[0] == 'SEARCH':
                try:
                    interpreter.search_module(query = self.command[1])
                except IndexError:
                    print(red('\n[!]') + green(' Invaild') + " syntax you should enter search query\n")
                except TypeError:
                    pass
            elif self.command[0] == 'exit' or self.command[0] == "Exit" or self.command[0] == 'close' or self.command[0] == 'Close' or \
                            self.command[0] == "EXIT" or self.command[0] == "CLOSE" or self.command[0] == "back" or self.command[
                0] == "Back" or self.command[0] == "BACK":
                import core.interpreter
                from core.main_completer import completer# import completer
                reload(core.interpreter)
                from core.interpreter import interpreter
                completer() # start completer
                while True:
                    interpreter.start_interpreter(interpreter) # restart interpreter
            elif self.command[0] == "Help" or self.command[0] == "help" or self.command[0] == "HELP":
                module_interpreter.help_message(module_interpreter)
            elif self.command[0] == 'set' or self.command[0] == "Set" or self.command[0] == "SET":
                try:
                    module_interpreter.command_set_call(module_interpreter,self.command[1], self.command[2])
                except IndexError:
                    print(red('\n[!]') + green(' Invaild') + " syntax you should enter option and new value\n")
            elif self.command[0] == 'info' or self.command[0] == 'Info' or self.command[0] == 'INFO' or self.command[0] == 'information' or self.command[0] == 'Information' or self.command[0] == 'INFORMATION':
                module_interpreter.command_info_call(module_interpreter)
            elif self.command[0] == 'exploit' or self.command[0] == 'Exploit' or self.command[0] == 'EXPLOIT' or self.command[0] == 'run' or self.command[0] == 'Run' or self.command[0] == 'RUN':
                opt = []
                val = []
                stat = []
                for o,v in obtainer.options.items():
                    opt.append(o)
                    val.append(v[2])
                    stat.append(v[0])
                i = 0
                while i < len(opt):
                    try:
                        if stat[i] == 'Yes':
                            if len(val[i]) <= 0:
                                print(red('\n[!]') + green(' You') + " should set {0} options\n".format(opt[i]))
                                break
                            else:
                                if obtainer.required['start_required'] == True or obtainer.required['start_required'] == "True" or obtainer.required['start_required'] == "TRUE":
                                    print('\n' + blue('[~]') + ' starting module ...\n')
                                    obtainer.exploit()
                                    print('\n' + blue('[~]') + ' end running module\n')
                                    break
                                else:
                                    obtainer.exploit()
                                    break

                        else:
                            if obtainer.required['start_required'] == True or obtainer.required['start_required'] == "True" or obtainer.required['start_required'] == "TRUE":
                                print('\n' + blue('[~]') + ' starting module ...\n')
                                obtainer.exploit()
                                print('\n' + blue('[~]') + ' end running module\n')
                                break
                            else:
                                obtainer.exploit()
                                break
                    except IndexError:
                        print
                    i += 1

            elif self.command[0] == 'check' or self.command[0] == 'Check' or self.command[0] == 'CHECK':
                if obtainer.required['check_required'] == True or obtainer.required['check_required'] == "True" or obtainer.required['check_required'] == "TRUE":
                    obtainer.check()
                else:
                    print('\n' + green('[#]') + " Module don't have check option\n")
            elif self.command[0] == 'exec' or self.command[0] == 'execute':
                try:
                    self.command.remove('exec' if self.command[0] == 'exec' else 'execute')
                    system(' '.join(self.command))
                except IndexError:
                    print(red("\n[!] ") + green("Please ") + " enter the command\n")
            elif self.command[0] == 'upgrade':
                interpreter.check_upgrade(interpreter)
            else:
                print('\n' + red('[!]') + green(' option') + ' not found\n')
        except (KeyboardInterrupt,EOFError):
            print('\n' + red('\n[!]') + green(' type') + gray(' exit') + ' to close the program\n')
        except IndexError:
            return None
