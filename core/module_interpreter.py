from __main__ import * # import all stuff in the program namespace
from utilities.color import * # import colors function
from core.banner import Banner # import banner
from utilities.screen_cleaner import clear # import screen cleaner == clear command in unix and unix like system
from core.module_obtainer import obtainer # import module_obtainer package
from imp import reload # import reload function from importlib lib
import core.interpreter, readline # import main interpreter
from core.interpreter import interpreter
from os import system # import system function from os lib
from glob import glob
from core.validator import validator

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
    t.createListCompleter(["set", "exploit", "back", "check", "help", "info", 'banner', 'run', 'exec', 'clear','search'])
    t.createListCompleter(["set", "exploit", "back", "check", "help", "info", 'banner', 'run', 'exec','clear'])
    readline.set_completer_delims('\t')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(t.listCompleter)
#

class module_interpreter(object):
    def command_set_call(self, option_name, option_value):
        self.option_name = option_name
        self.option_value = option_value
        self.commnad_set_configure(module_interpreter, self.option_name, self.option_value)

    def help_message(self):
        print('')
        print('Options:              Require:              Description:              Value:')
        print('--------              --------              ------------              ------')
        for opt,val in obtainer.options.items():
            print("{:23s}".format(opt)+''+'            '.join(val))
        print('')

    def command_info_call(self):
        try:
            print('')
            print(green('   Author: ') + obtainer.info['author'])
            print(green('   Date: ') + obtainer.info['date'])
            print(green('   Rank: ') + obtainer.info['rank'])
            print(green('   Category: ') + obtainer.info['category'])
            print(green('   Path: ') + obtainer.info['path'])
            print(green('   License: ') + obtainer.info['license'])
            try:
                try:
                    obtainer.extra_info_obtainer(obtainer,__file__)
                except Exception:
                    pass
                try:
                    obtainer.extra_info['cve']
                except (KeyError,NameError):
                    pass
                else:
                    if type(obtainer.extra_info['cve']) != list:
                        pass
                    else:
                        print(green('   CVE ID: '), end='')
                        for id in obtainer.extra_info['cve']:
                            print(id,end=', ')
            except Exception:
                pass
            print('\n\n')
            print(green('Module Options:'))
            print(green('-'*16))
            self.help_message(module_interpreter)
            print('\n')
            print(green('Description: ') + obtainer.info['description'] + '\n')
            print(green('References: '))
            for ref in obtainer.info['references']:
                print(red(' - ') + ref)
        except KeyError:
            print('\n' + red('[!]') + green(' You') + ' should define author,date,rank,category,path,license,description,rseferences keys in your info dictionary\n')
            pass
        if obtainer.extra_info_obtainer(obtainer,__file__):
            try:
                print(green('\nTargets')+ red('[{0}]'.format(len(obtainer.extra_info['targets']))) + green(':'))
                for element in obtainer.extra_info['targets']:
                    print(red(' - ') + element)
            except (NameError,KeyError,TypeError):
                pass
        print('')
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
                validator(self.shell_ask).validate_module_interpreter_mode()
            except (KeyboardInterrupt,EOFError):
                print('\n' + red('\n[!]') + green(' type') + gray(' exit') + ' to close the program\n')

    def commnad_set_configure(self, option_name, option_value):
        module_interpreter.option_name = option_name
        module_interpreter.option_value = option_value
        if module_interpreter.option_name in obtainer.options:
            obtainer.options[str(module_interpreter.option_name)][2] = module_interpreter.option_value
        else:
            print('\n' + red('[!]') + green(' option') + ' not define in module\n')
