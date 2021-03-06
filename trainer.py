#!/usr/bin/env python2
# -.- coding: utf-8 -.-
import ui
import trainer_config
import table
def main():
    uicurses = ui.UICurses()  
    uicurses.add_str("Select Training:")
    training = uicurses.get_str()
    if training in dir(trainer_config):
        current_training=eval("trainer_config." + training)
        for current in current_training:
            uicurses.clear()
            uicurses.add_dict(current)
            uicurses.wait_any_key(None)
            if "N" in current:
                N=current["N"]
            else:
                N=1
            for n_round in range(1,N+1):
                uicurses.clear()
                exercise = table.exercises_list[current["exercise"]](uicurses, current)
                exercise.run()
                if "rest" in current:
                    rest=current["rest"]
                else:
                    rest=trainer_config.DEFAULT_REST
                uicurses.clear()
                uicurses.add_str_center(str(n_round) + ", RESTING: ", -1,0)
                for i in range(rest,-1,-1):
                    uicurses.add_str_center(str(i),0,0,True)
                    uicurses.wait_any_key(1000)
            
    else:
        uicurses.add_str("NOT FOUND")
    uicurses.get_str()
    uicurses.quit()

if __name__ == "__main__":
    main()
