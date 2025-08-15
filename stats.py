def word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        num = len(words)
        return num

def sort_on(items):
    return items["num"]

def character_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        lower_case = file_contents.lower()
        letters = set()
        letter_count = []
        for case in lower_case:
            if case.isalpha() == True :
                letters.add(case)    
        for let in letters:
            letter_dit = { "char" : let, "num" : 0 }
            letter_count.append(letter_dit)
        for case in lower_case:
            for count in letter_count:
                if case == count["char"] :
                    count["num"] += 1
                    letter_count.sort(reverse=True, key=sort_on)
    return letter_count
                        
    