import json
import os
import sys
import urllib2
import urllib
from utils import *
PROGRAM_DIR=os.path.dirname(os.path.abspath(__file__))
core_settings = {}

def load_props():
    global core_settings
    if len(sys.argv) > 1:
        core_settings.update(parse_argv())
    else:
        try:
            httphandle = urllib2.urlopen("http://127.0.0.1:8080/rook/get")
            response = json.loads(httphandle.read())
            httphandle.close()
            if "result" in response and response["result"]=="OK":
                del response["result"]
                core_settings=response
            else:
                core_settings={"BPM":180, "duration":10, "words":3, "maze" : "test", "count" : 20, "field" : 0, "timeout" : 5000}
        except:
            core_settings={"BPM":180, "duration":10, "words":3, "maze" : "test", "count" : 20, "field" : 0, "timeout" : 5000}
load_props()

def get_prop(item):
    if item in core_settings:
        return core_settings[item]
    else:
        return None

def send_data(datadict):
    try: 
        httphandle = urllib2.urlopen("http://127.0.0.1:8080/rook/set_data",
                urllib.urlencode(datadict))
        response = json.loads(httphandle.read())
        httphandle.close()
        return response
    except:
        pass

def main():
    print(send_data({1:3,2:4}))

if __name__ == "__main__":
    main()
