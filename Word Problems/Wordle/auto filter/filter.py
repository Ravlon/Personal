from Luca.utils import yes
import pathlib as pth
PATH = pth.Path(__file__).parent.absolute()

def array_maker():
    wordle_link = PATH.joinpath("wordle.txt")
    with open(wordle_link,"r") as file:
        array = [list(line.rstrip()) for line in file]
    return array

def count_letters(letter, word, colour):
    count = 0
    greys = 0
    non_greys = 0

    for i in range(len(word)):
        if word[i] == letter:
            count +=1
            if colour[i] == "*":
                greys += 1
            else:
                non_greys +=1
    return count, greys, non_greys

def counter(letter,fiver):
    count = 0
    for i in fiver:
        if letter == i:
            count+=1
    return count

def l_in_word(letter, array:list, with_out = True):
    size = len(array)
    for i in range(size):
        word = array[0]
        if (with_out^(letter in word)):              #with_out is True if you want to filter out words that do contain letter (e.g. grey letter). False if you want to filter out words that do NOT contain the letter.
            array.append(word)
        array.pop(0)
    return 0

def l_in_position(letter, array:list, position, with_out = True):
    size = len(array)
    for i in range(size):
        word = array[0]
        if (with_out^(letter == word[position])):   #with_out is True if you want to filter out the words where the letter is in that position. False if you want to filter out the words where the letter is not in that position.
            array.append(word)
        array.pop(0)
    return 0

def doubles (let, array:list, n_of_lett:int, exact = False):
    size = len(array)
    for i in range(size):
        word = array[0]
        if exact:                                   #exact is True when filtering out the word that do not have exact number of the letter whether it's less or more. False filters out words that do not have at least the numbers of letter as requested.
            if counter(let,word) == n_of_lett:
                array.append(word)
        else:
            if counter(let,word) >= n_of_lett:
                array.append(word)
        array.pop(0)
    return 0

def filter(array, tries, result):
    """Filter a given list of words that has been inserted by using the attempted words and the corresponding info receveid from them.
    The program was created to see how many possible answers are left in the Wordle game after certain attempts.

    Args:
        array (list): array of possible answers that is filtered with given info
        tries (list): words that have been attempted to gain further info. The words must be in list format and not in text. A list of multiple words can be used
        result (list): the info gained from the words that have been tried. This must be in the corresponding format as the "tries" argument. Char should be in *,?,$ format.

    Returns:
        list: filter list of possible answers, derived from given "array" argument
    """
    word_array = array[:]
    for a in range(len(tries)):         #go through the attempts
        for l in range(5):         #go through the letters of the attempt
            res = result[a][l]
            lett = tries[a][l]
            if res == "$":              #green
                l_in_position(lett, word_array, l, with_out=False)
            if res == "?":              #yellow
                l_in_word(lett,word_array, with_out = False)
                l_in_position(lett, word_array, l, with_out=True)
                count,gr,n_gr = count_letters(lett,tries[a], result[a])
                if count > 1:
                    if not(gr):
                        doubles(lett, word_array, n_gr, exact=False)
                    else:
                        doubles(lett, word_array, n_gr, exact=True)
            if res == "*":              #grey
                count, gr, n_gr = count_letters(lett,tries[a], result[a])
                if count == 1:
                    l_in_word(lett,word_array,with_out=True)
                else:
                    if not(n_gr):
                        l_in_word(lett,word_array,with_out=True)
                    else:
                        l_in_word(lett,word_array,with_out=False)
                        l_in_position(lett,word_array,l,with_out=True)
                        doubles(lett, word_array, n_gr, exact=True)
    return word_array

if __name__ == "__main__":
    word_set = array_maker()

    while True:    
        attempts = []
        results = []
        print("[[[[[ Legend: $ is green | ? is yellow | * is grey ]]]]]")
        limit = int(input("How many words have you tried: "))
        print("Words attempted")
        for i in range(limit):
            print(i,".  ", end="")
            attempts.append(list(input()))
        print("Results of attempts")
        for i in range(limit):
            print(i,".  ", end="")
            results.append(list(input()))

        possibilities = filter(word_set, attempts, results)
        size = len(possibilities)

        print("There are {0} words possible".format(size))

        hide_bool = yes("Hide words?")
        if not(hide_bool):
            for i in range(size):
                print("".join(possibilities[i]))
        
        escape = yes("Close program?")
        if escape:
            break
        else:
            continue