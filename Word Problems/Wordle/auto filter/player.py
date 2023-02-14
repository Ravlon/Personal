import sys
from filter import *
from Luca.utils import yes
from Luca.formatter.formatter import grid
import numpy as np
LEN_OF_WORDS = 5
WORDLE_LIMIT = 6
COLOURS = ["*","?","$"]

def bit_calc(previous, current):
    #raise error if current > previous
    if current<previous:
        return abs(np.log2(current/previous))
    else:
        return 0.00

def result(attempt: list, answer: list):
    """ $ is green
        ? is yellow
        * is grey"""
    size = len(attempt)
    res = ["*" for x in range(size)]        #default is GREY letter
    double_checker = answer[:]              #List to ensure correct result for double+ letters
    for i in range(size):
        if attempt[i] == answer[i]:
            res[i] = "$"                    #GREEN
        else:
            double_checker.append(double_checker[0])
        double_checker.pop(0)
    for i in range(size):
        if res[i] == "*":                   #AVOID GREEN LETTERS
            for j in range(len(double_checker)):
                if attempt[i] == double_checker[j]:
                    res[i] = "?"            #YELLOW
                    double_checker.pop(j)
                    break       
    return "".join(res)

def recursive_loop(level:int, symbols:list, text:str, array:list):
    for i in symbols:
        temp_text = text + i
        if level+1 < LEN_OF_WORDS:
            recursive_loop(level+1, symbols, temp_text, array)
        else:
            array.append(list(temp_text))

def poss_colours():
    colours = COLOURS
    possibilities = []
    depth = 0
    recursive_loop(depth, colours, "", possibilities)
    return possibilities

def word_recur_loop(level:int, max_words:int, full_array:list, current_array:list, resulted_array: list):
    for i in full_array:
        temp_array = current_array[:]
        temp_array[level] = i
        if level+1 < max_words:
            word_recur_loop(level+1, max_words, full_array, temp_array, resulted_array)
        else:
            resulted_array.append(temp_array)

def possible_results(n_words:int):
    result_array = []
    temp = [[] for i in range(n_words)]
    depth = 0
    full_array = poss_colours()
    word_recur_loop(depth, n_words, full_array, temp, result_array)
    return result_array
    
def expected_bit(wordle_list, words:list, results, size):
    summa = 0.00
    for res in results:
        fraction = len(filter(wordle_list, words, res))
        if fraction:
            prob = fraction/size
            info = np.log2(np.reciprocal(prob))
            summa += prob*info
    return round(summa,2)

def best_guess(filtered_array, colour_set, top_n = 5):
    result_array = []
    for word in filtered_array:
        formatted_word = [word]
        bits = expected_bit(filtered_array, formatted_word, colour_set, len(filtered_array))
        result_array.append([bits, "".join(word)])
    result_array = sorted(result_array, reverse=True)
    return result_array[:top_n]

def game(initial_best, wordles, colour_set):
    header = ["Words","Color","Bests"]
    matrix = [["","*****",i] for i in initial_best]
    forms = [(" ",">","5"),("*",">","5"),(" ",">","10")]
    size = len(wordles)
    attempt = 0
    while True:
        print(" |[     ]|[     ]| " + "{: >10}".format(str(size))+" |")
        table = grid(matrix, forms, header)
        print(table)
        sys.stdout.write("\x1b[1A"*(WORDLE_LIMIT+3))
        print("\r |[", end = "")
        word = input()
        matrix[attempt][0] = word
        sys.stdout.write("\x1b[1A"*(1))
        print("\r |["+ word + "]|[", end = "")
        result = input()
        matrix[attempt][1] = result
        new_wordles = filter(wordles, [i[0] for i in matrix[:attempt+1]],[i[1] for i in matrix[:attempt+1]])
        size = len(new_wordles)
        new_best = best_guess(new_wordles, colour_set, top_n=WORDLE_LIMIT)
        for i in range(WORDLE_LIMIT):
            if i<len(new_best):
                matrix[i][2] = "".join(new_best[i][1]) + " " + str(new_best[i][0])
            else:
                matrix[i][2] = "-"*5
        sys.stdout.write("\x1b[1A"*(1))
        attempt += 1

def simulation(initial_best, wordles, colour_set, solution):
    header = ["Words","Color","Bests"]
    matrix = [["","*****",i] for i in initial_best]
    forms = [(" ",">","5"),("*",">","5"),(" ",">","10")]
    size = len(wordles)
    previous_size = size
    attempt = 0
    while True:
        print(" |[     ]|       | " + "{: >10}".format(str(size))+" | "+str(round(bit_calc(previous_size,size),2)))
        table = grid(matrix, forms, header)
        print(table)
        sys.stdout.write("\x1b[1A"*(WORDLE_LIMIT+3))
        print("\r |[", end = "")
        word = input()
        matrix[attempt][0] = word
        sys.stdout.write("\x1b[1A"*(1))
        matrix[attempt][1] = result(list(word), list(solution))
        new_wordles = filter(wordles, [i[0] for i in matrix[:attempt+1]],[i[1] for i in matrix[:attempt+1]])
        previous_size = size
        size = len(new_wordles)
        new_best = best_guess(new_wordles, colour_set, top_n=WORDLE_LIMIT)
        for i in range(WORDLE_LIMIT):
            if i<len(new_best):
                matrix[i][2] = "".join(new_best[i][1]) + " " + str(new_best[i][0])
            else:
                matrix[i][2] = "-"*5
        attempt += 1

if __name__ == "__main__":
    wordles = array_maker()
    wordle_best = []
    with open(r"C:\Users\lucas\OneDrive\Code\Altro\Word Problems\Wordle\auto filter\onestepexpectedinfo.txt", "r") as file:
        count = 0
        for line in file.readlines():
            if count < WORDLE_LIMIT:
                best = line.split(" ")
                wordle_best.append(best[1].rstrip())
                count +=1
            else:
                break
    colour_list = possible_results(1)
    game_bool = yes("Solved game? ")
    
    if game_bool:
        answer = input("Solution of the game:")
        simulation(wordle_best, wordles, colour_list, answer)
    else:
        game(wordle_best, wordles, colour_list)