from __main__ import * # import all stuff in the program namespace
from utilities.color import * # import colors function
from core.banner import Banner # import banner
from utilities import screen_cleaner # import screen cleaner == clear command in unix and unix like system
from core.module_obtainer import obtainer # import module_obtainer package
from imp import reload # import reload function from importlib lib
import core.interpreter, readline # import main interpreter
from core.interpreter import interpreter
from os import system # import system function from os lib
from glob import glob

def module_completer():
# source: https://gist.github.com/iamatypeofwalrus/5637895
    class tabCompleter(object):

        def pathCompleter(self,text,state):
            line   = readline.get_line_buffer().split()
            return [x for x in glob(text+'*')][state]
        def createListCompleter(self,ll):
            pass
            def listCompleter(text,state):
                line   = readline.get_line_buffer()
                if not line:
                    return [c + " " for c in ll][state]
                else:
                    return [c + " " for c in ll if c.startswith(line)][state]

            self.listCompleter = listCompleter
    t = tabCompleter()
    t.createListCompleter(["set", "exploit", "back", "check", "help", "info", 'banner', 'run', 'exec', 'restart'])
    readline.set_completer_delims('\t')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(t.listCompleter)
#

class module_interpreter(object):
    def command_set_call(self, option_name, option_value):
        self.option_name = option_name
        self.option_value = option_value
        self.commnad_set_configure(self.option_name, self.option_value)

    def help_message(self):
        print('')
        print('Options:              Require:              Description:              Value:')
        print('--------              --------              ------------              ------')
        for opt,val in self.options.items():
            print("{:23s}".format(opt)+''+'            '.join(val))
        print('')

    def command_info_call(self):
        try:
            print('')
            print(green('   Author: ') + self.info['author'])
            print(green('   Date: ') + self.info['date'])
            print(green('   Rank: ') + self.info['rank'])
            print(green('   Category: ') + self.info['category'])
            print(green('   Path: ') + self.info['path'])
            print(green('   License: ') + self.info['license'])
            print('\n\n')
            print(green('Module Options:'))
            print(green('-'*16))
            self.help_message()
            print('\n')
            print(green('Description: ') + self.info['description'] + '\n')
            print(green('References: '))
            for i in self.info['references']:
                print(red(' - ') + i)
            print('')
        except KeyError:
            print('\n' + red('[!]') + green(' You') + ' should define author,date,rank,category,path,license,description,rseferences keys in your info dictionary\n')
            pass

    def __init__(self, module, category, module_input):
        self.module_input = module_input
        from core.module_obtainer import obtainer
        obtainer.obtaining_info(obtainer,self.module_input)
        module_completer() # start completer
        self.module_name = module # get module_name variable from interpreter
        self.category = category # get category variable from interpreter
        self.options = obtainer.options
        self.info = obtainer.info
        self.exploit = obtainer.exploit
        self.required = obtainer.required
        while True:
            try:
                self.shell_ask = input(underline("PySploit") +  " " + self.category + "(" + red(self.module_name) + ") >> ").split() # get input from user and split it
                if self.shell_ask[0] == "clear" or self.shell_ask[0] == "Clear" or self.shell_ask[0] == "CLEAR":
                    clear()
                elif self.shell_ask[0] == "banner" or self.shell_ask[0] == "Banner" or self.shell_ask[0] == "BANNER":
                    Banner()
                elif self.shell_ask[0] == 'exit' or self.shell_ask[0] == "Exit" or self.shell_ask[0] == 'close' or self.shell_ask[0] == 'Close' or \
                                self.shell_ask[0] == "EXIT" or self.shell_ask[0] == "CLOSE" or self.shell_ask[0] == "back" or self.shell_ask[
                    0] == "Back" or self.shell_ask[0] == "BACK":
                    from core.main_completer import completer# import completer
                    reload(core.interpreter)
                    completer() # start completer
                    while True:
                        interpreter.start_interpreter(interpreter) # restart interpreter
                elif self.shell_ask[0] == "Help" or self.shell_ask[0] == "help" or self.shell_ask[0] == "HELP":
                    self.help_message()
                elif self.shell_ask[0] == 'set' or self.shell_ask[0] == "Set" or self.shell_ask[0] == "SET":
                    self.command_set_call(self.shell_ask[1], self.shell_ask[2])
                elif self.shell_ask[0] == 'info' or self.shell_ask[0] == 'Info' or self.shell_ask[0] == 'INFO' or self.shell_ask[0] == 'information' or self.shell_ask[0] == 'Information' or self.shell_ask[0] == 'INFORMATION':
                    self.command_info_call()
                elif self.shell_ask[0] == 'exploit' or self.shell_ask[0] == 'Exploit' or self.shell_ask[0] == 'EXPLOIT' or self.shell_ask[0] == 'run' or self.shell_ask[0] == 'Run' or self.shell_ask[0] == 'RUN':
                    for o,v in obtainer.options.items():
                        if v[0] == "yes" or v[0] == "Yes" or v[0] == "YES":
                            if len(obtainer.options[str(o)][2]) <= 0:
                                print(red('\n[!]') + green(' You') + " should set {0} options\n".format(o))
                            else:
                                if self.required['start_required'] == True or self.required['start_required'] == "True" or self.required['start_required'] == "TRUE":
                                    print('\n' + blue('[~]') + ' starting module ...\n')
                                    self.exploit()
                                    print('\n' + green('[#]') + ' end running module\n')
                                else:
                                    self.exploit()
                        else:
                            if self.required['start_required'] == True or self.required['start_required'] == "True" or self.required['start_required'] == "TRUE":
                                print('\n' + blue('[~]') + ' starting module ...\n')
                                self.exploit()
                                print('\n' + green('[#]') + ' end running module\n')
                            else:
                                self.exploit()

                elif self.shell_ask[0] == 'check' or self.shell_ask[0] == 'Check' or self.shell_ask[0] == 'CHECK':
                    if self.required['check_required'] == True or self.required['check_required'] == "True" or self.required['check_required'] == "TRUE":
                        obtainer.check()
                    else:
                        print('\n' + green('[#]') + " Module don't have check option\n")
                elif self.shell_ask[0] == 'exec' or self.shell_ask[0] == 'execute':
                    try:
                        self.shell_ask.remove('exec' if self.shell_ask[0] == 'exec' else 'execute')
                        system(' '.join(self.shell_ask))
                    except IndexError:
                        print(red("\n[!] ") + green("Please ") + " enter the command\n")
                else:
                    print('\n' + red('[!]') + green(' option') + ' not found\n')
            except (KeyboardInterrupt,EOFError):
                print('\n' + red('\n[!]') + green(' type') + gray(' exit') + ' to close the program\n')
            except IndexError:
                return None

    def commnad_set_configure(self, option_name, option_value):
        self.option_name = option_name
        self.option_value = option_value
        if self.option_name in self.options:
            self.options[str(self.option_name)][2] = self.option_value
        else:
            print('\n' + red('[!]') + green(' option') + ' not define in module\n')
