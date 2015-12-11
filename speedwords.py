import random

import exercise
from settings import *
import time
import math
from timemanager import *
class SpeedWords(exercise.Exercise):
    def __init__(self, uicurses=None, dic_data=None):
        self.required = ["maze", "count", "field", "timeout"] 
        exercise.Exercise.__init__(self, uicurses, dic_data)

    def run(self):
        uicurses = self.uicurses
        self.maze_data = self.decode_maze(self.maze)
        uicurses.add_str("maze: " + str(self.maze))
        uicurses.add_str("count: " + str(self.count))
        uicurses.add_str("field: " + str(self.field))
        uicurses.add_str("timeout: " + str(self.timeout))
        index_list = []
        init_time = time.time()
        correct_count = 0
        for _ in range(self.count):
            current_index = random.randint(0,len(self.maze_data) - 1)
            index_list.append(current_index)
        self.show_words(index_list)
        total_time = time.time() - init_time
        time_per_word_ms = total_time * 1000.0 / self.count
        uicurses.add_str("time per word: " + str(time_per_word_ms))
        lines = uicurses.ymax
        cols = int(math.ceil(float(self.count)/uicurses.ymax))
        uicurses.clear()
        inserted = []
        i=0
        for col in range(cols):
            if col == cols-1:
                lines = min((lines, self.count))
            for line in range(lines):
                uicurses.grid_add_str(str(i+1), line,col,lines,cols)
                checking_word = uicurses.grid_get_str(line,col,lines,cols, 3)
                inserted.append(checking_word)
                i+=1
        uicurses.clear()
        i=0
        for col in range(cols):
            if col == cols-1:
                lines = min((lines, self.count))
            for line in range(lines):
                shown_word = self.maze_data[index_list[i]][self.field]
                checking_word = inserted[i]
                if checking_word==shown_word:
                    uicurses.grid_add_str(str(i+1) + " OK: "  + shown_word, line, col, lines, cols)
                    correct_count += 1
                else:
                    uicurses.grid_add_str(str(i+1) + " NOOK: " + shown_word + "(" + checking_word + ")", line, col, lines, cols)
                i+=1
        uicurses.wait_any_key(None)

    def show_words(self,index_list):
        for index in index_list:
            current_field = self.field
            tick()
            diff_t = self.timeout - tock() - 1
            while diff_t>0:
                self.uicurses.add_str_center(self.maze_data[index][current_field],-5, -5, True)
                t, key = self.uicurses.wait_any_key(diff_t)
                if key=="a":
                    current_field = (current_field + 1) % (len(self.maze_data[index]))
                else:
                    break
                diff_t = self.timeout - tock() - 1

    def decode_maze(self, maze):
        maze_data = []
        fhandle = open(PROGRAM_DIR + "/" + maze + "/index.txt", "r")
        for line in fhandle:
            maze_data.append(tuple(line.replace("\n","").split(";")))
        fhandle.close()
        return maze_data

def main():
    ex = SpeedWords()
    ex.run()
    ex.uicurses.quit()

if __name__ == "__main__":
    main()
