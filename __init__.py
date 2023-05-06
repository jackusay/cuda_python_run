from cudatext import *

from cudax_lib import get_translation
_ = get_translation(__file__)  # I18N
PRE = '[Python Run]'

class Command:
    def python_run(self):   return run()

def run():
    txt = ed.get_text_all()
    app_proc(PROC_EXEC_PYTHON, txt)
    msg_status(PRE + _('JOB DONE'))