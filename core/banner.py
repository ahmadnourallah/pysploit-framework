from random import choice
from utilities.color import white, green

class Banner():
    def __init__(self):
        def banner1():
            """ return first banner """
            print(white(''))
            print('oooooooooo               oooooooo8            o888            o88    o8')
            print('888    888 oooo   oooo 888        ooooooooo   888   ooooooo  oooo o888oo')
            print('888oooo88   888   888   888oooooo  888    888 888 888     888 888  888')
            print('888          888 888           888 888    888 888 888     888 888  888')
            print('o888o           8888    o88oooo888  888ooo88  o888o  88ooo88  o888o  888o')
            print('             o8o888                o888')
            print("")
            print(green('-') * 75)
            print('     Free exploit framework for pentester and python developer')
            print(green('-') * 75)
            print(white(''))


        def banner2():
            """ return second banner """
            print(white(''))
            print('ooooooooo.                .oooooo..o            oooo             o8o      .')
            print("888   `Y88.             d8P'    `Y8            `888             `'    .o8")
            print("888ooo88P'   `88.  .8'   `'Y8888o.   888' `88b  888  d88' `88b `888    888")
            print("888           `88..8'        `'Y88b  888   888  888  888   888  888    888")
            print("888            `888'    oo     .d8P  888   888  888  888   888  888    888 .")
            print("o888o            .8'     8''88888P'   888bod8P' o888o `Y8bod8P' o888o   '888'")
            print("             .o..P'                   888")
            print("888   .d88' oooo    ooo Y88bo.      oo.ooooo.   888   .ooooo.  oooo  .o888oo")
            print("             `Y8P'                   o888o")
            print('')
            print("       .o   .o          .o   .o          .o   .o")
            print("      .8'  .8'         .8'  .8'         .8'  .8'")
            print("  .888888888888'   .888888888888'   .888888888888'")
            print("    .8'  .8'         .8'  .8'         .8'  .8'")
            print(".888888888888'   .888888888888'   .888888888888'")
            print("  .8'  .8'         .8'  .8'         .8'  .8'")
            print(" .8'  .8'         .8'  .8'         .8'  .8' ")
            print('')
            print(green('-') * 75)
            print('     Free exploit framework for pentester and python developer')
            print(green('-') * 75)
            print(white(''))
        def banner3():
            print('                      ____        _____       __      _ __')
            print('                     / __ \__  __/ ___/____  / /___  (_) /_')
            print('                    / /_/ / / / /\__ \/ __ \/ / __ \/ / __/')
            print('                   / ____/ /_/ /___/ / /_/ / / /_/ / / /_')
            print('                  /_/    \__, //____/ .___/_/\____/_/\__/')
            print('                        /____/     /_/')
            print('')
            print(green('-') * 75)
            print('     Free exploit framework for pentester and python developer')
            print(green('-') * 75)
            print(white(''))

        choice([banner1, banner2, banner3])()
