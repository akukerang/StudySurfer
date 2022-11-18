import sys, getopt
from classes.movieMaker import getVideo
def main():
    try:
        opts, values = getopt.getopt(sys.argv[1:], 'm:')
        for currArr, currVal in opts:
            if currArr in ('-m'):
                if currVal == 'csgo':
                    getVideo('./resources/gameplay/csgo.mp4')    
                elif currVal == 'subway':
                    getVideo('./resources/gameplay/ssgameplay.mp4')    
                elif currVal == 'mc':
                    getVideo('./resources/gameplay/minecraft.mp4')    
                else: 
                    print('Invalid option')           
    except getopt.error as err:
        print(str(err))


if __name__ == "__main__":
    main()         



