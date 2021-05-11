# Special Variable __name__ 
# __name__ denotes the running file is main file or not.
# if the running file is main running file like in java, then __name__ == __main__ automatically.
# if running file is not main running file then, __name__ == NAME_OF_FILE.

# Main use of __name__ is to coditionally run main() if running file is main file.

import DemoCalcModule as demo

print(__name__) # Prints __main__ if it is main running file. 

def notMain():
    print('I am just called normally.') # runs even it is not main ruunning file.

def untilMain():
    print('I am called by main() because it is main running file.') # doesnt run until it is main running file.

notMain()
def main():
    untilMain()

if __name__ == '__main__':  # This is main use.
    main()
    