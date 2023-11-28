import tkinter as tk
import tkinter.ttk as ttk
from pokemon import Pokemon as Pokemon
# using code from https://stackoverflow.com/a/47148198

# responsibility: display all the team member stuff!
class TeamMemberFrame(tk.Frame):
    def __init__(self, parent=None):
        # parent constructor should be first!!
        tk.Frame.__init__(self, parent)
        self.make_widgets()
        self.setup_layout()
        # actually making it
        self.parent = parent
        #self.pack()
    def make_widgets(self):
        # can't assume that self.parent is a root window, so use
        # self.winfo_toplevel()
        # to get root window
        # we won't use that though hehe
        # ~~~~~~
        # init display vars for tk
        self.__initTkVars()
        # init labels
        self.__initLabels()
        
    def __initTkVars(self):
        self.speciesVariable = tk.StringVar()
        self.levelVariable = tk.IntVar()
        self.moveVariables = []
        for i in range(4):
            self.moveVariables.append(tk.StringVar())
        self.abilityVariable = tk.StringVar()
        self.heldItemVariable = tk.StringVar()
    def __initLabels(self):
        self.testLabel = tk.Label(self, text="Test Label")
        #self.testLabel.pack()
        # needed:
        # species, helditem, ability, moves (4 total), species
        # species
        self.speciesLabel = tk.Label(self, textvariable = self.speciesVariable)
        #self.speciesLabel.pack(side="left", fill="x")
        # helditem
        self.heldItemLabel = tk.Label(self, textvariable=self.heldItemVariable)
        #self.heldItemLabel.pack(side="left", fill="x")
        # ability
        self.abilityLabel = tk.Label(self, textvariable=self.abilityVariable)
        #self.abilityLabel.pack(side="left", fill="x")
        # moves
        self.moveLabels = []
        for i in range(4):
            self.moveLabels.append(tk.Label(self, textvariable=self.moveVariables[i]))
            #self.moveLabels[i].pack(side="left", fill="x")
    def setup_layout(self):
        self.config(bg="blue")
        self.speciesLabel.grid(row=1,column=0, columnspan=2)
        self.heldItemLabel.grid(row=2, column=0)
        self.abilityLabel.grid(row=2,column=1)
        # moves
        self.moveLabels[0].grid(row=4,column=0)
        self.moveLabels[1].grid(row=4,column=1)
        self.moveLabels[2].grid(row=5,column=0)
        self.moveLabels[3].grid(row=5,column=1)
            
    # getters and setters for species, held item, ability, and moves
    # species
    def updateSpecies(self, newSpecies: str):
        self.speciesVariable.set(newSpecies)
        #self.speciesLabel.pack()
    def getSpecies(self):
        return self.speciesLabel.get()
    # held item
    def updateHeldItem(self, newHeldItem: str):
        self.heldItemVariable.set(newHeldItem)
        #self.heldItemLabel.pack()
    def getAbility(self):
        return self.abilityLabel.get()
    # ability
    def updateAbility(self, newAbility: str):
        self.abilityVariable.set(newAbility)
        #self.abilityLabel.pack()
    def getAbility(self):
        return self.abilityLabel.get()
    # move
    def updateMove(self, newMove: str, moveIndex: int):
        """updateMove
        Update move label

        Args:
            newMove (str):
            moveIndex (int): between 0 and 3
        """
        self.moveVariables[moveIndex].set(newMove)
        #self.moveLabels[moveIndex].pack()
    def getMoveFromIndex(self, moveIndex: int):
        """
        Gets name of displayed move, from index. Will include any blank moves in its count.

        Args:
            moveIndex (int): from 0 to 3

        Returns:
            string: move name
        """
        return self.moveLabels[moveIndex].get()



class MainWindow(tk.Frame):
    def __init__(self, parent=None):
        # parent constructor should be first!!
        tk.Frame.__init__(self, parent)
        self.make_widgets()
        self.setup_layout()
        self.test_member_setup()
        # actually making it
        self.parent = parent
        #self.pack()
    def make_widgets(self):
        self.team_members_frames = []
        for i in range(6):
            self.team_members_frames.append(TeamMemberFrame())
        self.species_combobox = ttk.Combobox(state="readonly")
    def setup_layout(self):
        # team member layout
        self.team_members_frames[0].grid(row=2,column=0)
        self.team_members_frames[1].grid(row=2,column=1)
        self.team_members_frames[2].grid(row=3,column=0)
        self.team_members_frames[3].grid(row=3,column=1)
        self.team_members_frames[4].grid(row=4,column=0)
        self.team_members_frames[5].grid(row=4,column=1)
        self.species_combobox.grid(row=2,column=3)
        self.species_combobox['values'] = ("Pikachu", "Clodsire")
    def test_member_setup(self):
        for i in range(5):
            test("testing setup " + str(i), self.team_members_frames[i])
        test2("testing setup 5", self.team_members_frames[5])
    #def add_species_to_combobox(self, speciesName: str):
    #    print(self.species_combobox['values'])    


def test(printstr: str, pokemonFrame:TeamMemberFrame):
    pokemonFrame.updateSpecies("Pikachu")
    print(printstr)
    pokemonFrame.updateAbility("Static")
    pokemonFrame.updateHeldItem("Light Ball")
    pokemonFrame.updateMove("Quick attack", 0)
    pokemonFrame.updateMove("Thunderbolt", 1)
    pokemonFrame.updateMove("Thunder Wave", 2)
    pokemonFrame.updateMove("Volt Tackle", 3)
def test2(printstr: str, pokemonFrame:TeamMemberFrame):
    pokemonFrame.updateSpecies("Clodsire")
    print(printstr)
    pokemonFrame.updateAbility("Unaware")
    pokemonFrame.updateHeldItem("Leftovers")
    pokemonFrame.updateMove("Earthquake", 0)
    pokemonFrame.updateMove("Poison Jab", 1)
    pokemonFrame.updateMove("Tera Blast", 2)
    pokemonFrame.updateMove("Body Press", 3)
