from random import shuffle

#classblueprint
#obj is example

class Card:
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]

    values = [None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    def __init__(self,v,s):
        """suit + value are ints"""
        #assign value and suit
        self.value = v
        self.suit = s
    def __lt__(self,e2):
        if self.value<e2.value:
            return True
        if self.value == e2.value:
            if self.suit < e2.suit:
                return True
            else:
                return False
        return False
    def __gt__(self,e2):
        if self.value>e2.value:
            return True
        if self.value == e2.value:
            if self.suit > e2.suit:
                return True
            else:
                return False
        return False
    def __repr__(self):
        v = self.values[self.value] + \
            " of " + \
            self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        #values
        for i in range(2,15):
            #suits
            for j in range(4):
                self.cards\
                    .append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

#player class

class Player:
    def __init__(self,name):
        self.wins = 0
        self.card = None
        self.name = name


#class game

class Game :
    def __init__(self):
        name1 = input("please enter name of the first player")
        name2 = input("please enter name of the second player")
        #obj create
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self,winner):
        w = "{} wins the round"
        w= w.format(winner)
        print(w)

    
    def draw(self,p1n,p1c,p2n,p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n,
                    p1c,
                    p2n,
                    p2c)
        print(d)


    def play_game(self):
        cards = self.deck.cards
        print("WAR BEGINS!!!!!")
        while len(cards) >= 2:
            m = "press 'q' to exit and any other key to play"
            response = input(m)
            if response == 'q' :
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw (p1n,
                       p1c,
                       p2n,
                       p2c)
            if p1c >p2c:
                self.p1.wins +=1
                self.wins(self.p1.name)
            else:
                self.p2.wins +=1
                self.wins(self.p2.name)
        win = self.winner(self.p1,self.p2)
        print("The war has ended.{} is victoroius".format(win))

    def winner(self,p1,p2):
        if p1.wins >p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "the tides are all matched up and tied but nobody"


#object create
game = Game()
game.play_game()