import readline
from glob import glob

def completer():
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
                    return None
                else:
                    return [c + " " for c in ll if c.startswith(line)][state]
            self.listCompleter = listCompleter
    t = tabCompleter()
                            # tool command
    t.createListCompleter(["clear", "exit", "banner","exec","restart", "upgrade", 'search'
                            # modules
                            # auxiliary modules
                             ,"use auxiliary/gather/ip_gather","use auxiliary/gather/ip_lookup", "use auxiliary/core/pyconverter"
                            # exploit modules
                             ,"use exploit/windows/ftp/ftpshell_overflow", "use exploit/android/login/login_bypass", "use exploit/windows/http/oracle9i_xdb_pass"])
    readline.set_completer_delims('\t')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(t.listCompleter)
