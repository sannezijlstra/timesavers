class Iterative():
    def __init__(self, board, max_depth = 1000):

    self.board = board
    self.max_depth = max_depth
    self.temp_depth = 1
    self.start = board #?????
    self.archive[]


    def check_depth(self):
        pass

# idee van een vaste breedte toevoegen
# dingen wegharken die niet bij je heuristieken passen

# A star:
# voorkeur voor bepaalde borden: minimaal en consistent 
# altijd onderschalen: consistent. 
# geen radomness 
# je gaat je borden rangschikken op voorkeur en aantal zetten dat nodig is om op het bord te komen 
# bord steeds minste aantal zetten naar doel en 
# altijd onderschattig, dus realiteit is altijd minder goed 
# kortste om er te komen + goeie schatting dat volgende zet oplossing is
# minimale kosten en minimale schatting --> garantie dat alles daarna slechter is 
# alles daarna heeft niet allebei van bovenstaande 
# slechtste schatting: 0 stappen: precies breadth first search!!! 
# betere schatting: iig 1 zet: voorkeur aan bord waar auto wel voor t bord staat 
# beter: als auto hier, 2 auto's daarvoor, 2 auto's aan de kant dus 2 zetten nodig --> minimale consistente onderschatting
# minimale heuristiek is heel lastig 
