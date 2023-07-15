import sys

# My modules
import listm
import scraper

lm = listm.Listm()

argv = sys.argv[1:]

# args: h[help]
#       r[run]
#       a[add source to the current list]
#       d[delete source] s[show lists]
#       s[show a list or the name of all lists]
#       l[create]
#       dl[delete a list]

if len(argv) == 1:
    match argv[0]:
        case "-h":
            print("help")
        case "-s":
            lm.show_all()
        case _:
            print("Command not foud")
elif len(argv) == 2:
    match argv[0]:
        case "-r":
            data = lm.get(argv[1])
            scraper.core(data)
            
        case "-a":
            pass
        case "-d":
            pass
        case "-dl":
            pass
        case "-s":
            lm.show(argv[1])
            pass
        case "-l":
            pass
        case _:
            print("Command not foud")
elif len(argv) > 2:
    print("too many arguments")
    sys.exit()
else:
    print("Use the argument -h to see all commands")
