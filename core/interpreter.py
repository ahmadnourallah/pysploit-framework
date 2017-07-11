from utilities.color import * # import utilites
from utilities.screen_cleaner import clear # import utilites
from core.main_completer import completer # completer import
from imp import reload # import reload function from imp module
from os import system
class interpreter(object):
    def start_interpreter(self):
        completer()
        try:
            self.main_ask = input(underline("PySploit") + " >> ").split()
            if self.main_ask[0] == "clear" or self.main_ask[0] == "Clear" or self.main_ask[0] == "CLEAR":
                clear()
            elif self.main_ask[0] == "banner" or self.main_ask[0] == "Banner" or self.main_ask[0] == 'BANNER':
                Banner()
            elif self.main_ask[0] == 'exit' or self.main_ask[0] == "Exit" or self.main_ask[0] == 'close' or self.main_ask[0] == 'Close':
                exit(0)
            elif self.main_ask[0] == "use" or self.main_ask[0] == "Use" or self.main_ask[0] == "USE":
                from core.module_obtainer import obtainer
                from core.module_interpreter import module_interpreter
                try:
                    if obtainer.obtaining_info(obtainer, self.main_ask[1]):
                        while True:
                            module_interpreter(self.main_ask[1].split('/')[-1], self.main_ask[1].split('/')[-1-1],self.main_ask[1])
                except IndexError:
                    print('\n' + red('[!]') + green(' You') + ' should enter the module name\n')
            elif self.main_ask[0] == 'restart' or self.main_ask[0] == 'Restart' or self.main_ask[0] == 'RESTART':
                import core.module_interpreter # import module_interpreter module from core foloder
                print('\n' + blue('[~]') + ' restarting the program ..... success\n')
                reload(core.module_interpreter)
                from core.module_interpreter import module_interpreter
            elif self.main_ask[0] == 'exec' or self.main_ask[0] == 'execute':
                try:
                    self.main_ask.remove('exec' if self.main_ask[0] == 'exec' else 'execute')
                    system(' '.join(self.main_ask))
                except IndexError:
                    print(red("\n[!] ") + green("Please ") + " enter the command\n")
            else:
                print('\n' + red('[!]') + green(' option') + ' not found\n')
        except (KeyboardInterrupt,EOFError):
            print('\n' + red('\n[!]') + green(' type') + gray(' exit') + ' to close the program\n')
        except IndexError:
            return None
