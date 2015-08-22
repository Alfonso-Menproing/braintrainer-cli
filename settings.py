import comunicatorclient
import json
import os
import sys
CHOOSE = False
PROGRAM_DIR = os.path.dirname(sys.argv[0])
cc=comunicatorclient.ComunicatorClient()
core_settings = None

def load_props():
    global core_settings
    global CHOOSE
    try:
        core_settings = json.loads(cc.send("get current "))
    except:
        core_settings={"BPM":"110", "duration":"60"}
        CHOOSE = True
load_props()

def get_prop(item):
    if item in core_settings:
        return core_settings[item]
    else:
        return None

def check():
    try: 
        cc.send("check")
    except:
        pass
