import easygui as eg
import random as r

try:
    import tkinter as tk
except:
    import Tkinter as tk
import pygubu

class country():
    def __init__(self, leader="", name="", race="", cities=[], cash=0, science=0, culture=0, piety=0, religion="", policies=[], discoveries=[]):
        self.leader = leader
        self.name = name
        self.race = race
        self.cash = cash
        self.science = science
        self.culture = culture
        self.piety = piety
        self.religion = religion
        self.policies = policies
        self.cities = cities
        self.discoveries = discoveries
    def GPT(self):
        return 3
    def CPT(self):
        return 2

class race():
    def __init__(self, name="", nameish="", description="", science=0, Stcash=0, Incash=0, culture=0, piety=0, discoveries=[], attack=0, defend=0, popgrowth=0, startUnit=""):
        self.name = name
        self.nameish = nameish
        self.description = description
        self.science = science
        self.Incash = Incash
        self.Stcash = Stcash
        self.culture = culture
        self.piety = piety
        self.discoveries = discoveries
        self.attack = attack
        self.defend = defend
        self.popgrowth = popgrowth

class city():
    def __init__(self, name="", buildings=[], population=0, location=None):
        self.name = name
        self.buildings = []
        self.population = population
        self.location = location

class location():
    def __init__(self, altitude=0, fertility=0, water=False, climate=0):
        self.altitude = altitude
        self.fertility = fertility
        self.water = water
        self.climate = climate
    def description(self):
        self.altW = rank(self.altitude, (-2, 10))
        self.fertW = rank(self.fertility, (0,10))
        if self.climate > 10 - 2:
            self.cliW = "Very Cold"
        elif self.climate > 10 - 2 * 2:
            self.cliW = "Cold"
        elif self.climate > 10 - 2 * 3:
            self.cliW = "Mild"
        elif self.climate > 10 - 2 * 4:
            self.cliW = "Dry"
        elif self.climate > 0:
            self.cliW = "Very Dry"
        return "A " + self.altW + " Plot Of Land With A " + self.cliw + " Climate. The Ground Here Is " + self.fertW + "."

def rank(item, minmax):
    rng = abs(minmax[0] - minmax[1])
    step = rng / 5
    if item > minmax[1] - step:
        string = "Very High"
    elif item > minmax[1] - step * 2:
        string = "High"
    elif item > minmax[1] - step * 3:
        string = "Medium"
    elif item > minmax[1] - step * 4:
        string = "Low"
    elif item > minmax[0]:
        string = "Very Low"
    else:
        print(item, minmax, "ERROR")



def say(*words):
    words = ' '.join(map(str, words))
    eg.msgbox(msg=words, title="Aiopa Conquest")

def options(message, *options):
    eg.buttonbox(msg=message, choices=(options), title="Aiopa Conquest")

def enter(message):
    return eg.enterbox(msg=message)

def carosel(message, items):
    num = 0
    maxnum = len(items) - 1
    while True:
        if num > maxnum:
            num = 0
        if num < 0:
            num = maxnum

        string = message + "\n" + items[num].name + "\n" + items[num].description
        sel = eg.buttonbox(msg=string, choices=("<<<", "Select", ">>>"))
        if sel == "<<<":
            num += -1
        if sel == ">>>":
            num += 1
        if sel == "Select":
            return items[num]

def init():
    dwarves = race(name="Dwarves", nameish="Dwarvish", Incash=10, Stcash=100, discoveries=["mining"], description="The dwarves live underground, and rarely leave their mountain homes unless it is to trade their copious amounts of gold.\nBegin with 100 gold\n+10% gold per turn\n+10% while defending")
    humans = race(name="Humans", nameish="Human", science=10, culture=10, description="The humans are naturally curious, and a set on gaining as much power for themselves as possible. However, when humans cannot explain something with science, they turn to religion.\n+10% science per turn\n+10% piety per turn")
    elves = race(name="Elves", nameish="Elvish")
    global races
    races = [dwarves, humans, elves]

def terrain(size, blobsize):
    world = []
    for i in range(1, size):
        island = []
        for j in range(1, blobsize):
            place = location(r.randint(-2, 10), r.randint(0, 10), bool(r.getrandbits(1)), r.randint(1, 10))
            island.append(place)


def begin():
    #say("Welcome to Aiopa Conquest!")
    global player

    player = country()

    #player.leader = enter("What is your country's leader named?")
    #player.name = enter("What is your country's name?")

    #player.race = carosel("Select your race:", races)

#init()
#begin()

class Application:
    def __init__(self, master):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('ConquestUI.ui')

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('Main Window', master)
        builder.get_object("Map View", self.mainwindow).lower()

        builder.connect_callbacks(self)

        self.refresh()

    def refresh(self):
        self.builder.get_variable("GoldString").set(str(player.GPT()) + "/t")
        self.builder.get_variable("CultureString").set(str(player.CPT()) + "/t")









init()
begin()
root = tk.Tk()
app = Application(root)
root.mainloop()
