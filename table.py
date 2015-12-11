import secuencialbin
import secuencialdec
import reader
import speedwords
exercises_list = {
        "Binarios Secuenciales" : secuencialbin.SecuencialBin,
        "Decimales Secuenciales" : secuencialdec.SecuencialDec, 
        "Column Reader" : reader.SecuencialReader,
        "Line Reader" : reader.LineReader,
        "Speed Words" : speedwords.SpeedWords
        }
default_config = {
        "Binarios Secuenciales" : {"BPM" : 160, "duration" : 10},
        "Decimales Secuenciales" : {"BPM" : 180, "duration" : 10}, 
        "Column Reader" : {"text" : "random", "BPM" : 250, "words" : 3},
        "Line Reader" : {"text" : "random", "BPM" : 250, "words" : 3},
        "Speed Words" : {"count" : 20, "timeout" : 800, "maze" : "palabras", "field" : 0}
        }
