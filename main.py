import sys 
def get_book_text(path_to_file):
    with open(path_to_file) as f: 
        file_contents = f.read()
        return file_contents

from stats import word_count
from stats import character_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    number = character_count(sys.argv[1])
    word = word_count(sys.argv[1])
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word} total words") 
    print("--------- Character Count -------")
    for num in number:
        print(f"{num['char']}: {num['num']}")

    print ("""============= END =============== """)
    
    return 
    
   

main()