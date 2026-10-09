hp=100

def into():
    desison="no"
    print("so this is the dungeon people have been talking about... \n they say that if you take the right path you can rach a land of great fortunes... \n I wonder if it is worth entering")
    input("(do you wish to enter? yes or no)-").lower
    if  desison=="no" or desison=="n":
        print ("best not, could be dangorus")
    elif desison=="yes" or desison=="y":
        print("no time like the pressent, lets go")
        room_1()
def room_1():
    pass
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
print("when you are asked to input something you must input ether the word or the first letter of the word you with to pick, \n in most cases you will be asked to pick again if you mess up.\n without further ado, enjoy :)\n \n")
into()
