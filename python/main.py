"""
author: Wang Shuowei
date: 2021.01.06
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from DSIII import Ui_MainWindow
from character import Character
from functools import partial


class MyWindow(Ui_MainWindow):
    def __init__(self, main_window, character):
        super().setupUi(main_window)

        self.att_list = ["vigor", "attunement", "endurance", "vitality", "strength",
                         "dexterity", "intelligence", "faith", "luck"]

        self.ability_list = ["HP", "FP", "Stamina", "Equipment load", "Poise", "Item Discovery", "Attunement Slots",
                             "Physical", "VS Strike", "VS Slash", "VS Thrust", "Magic", "Fire", "Lightning", "Dark",
                             "Bleed", "Poison", "Frost", "Curse", "Level", "Souls to next level", "Souls spend sum"]

        self.att_text = {"vigor": self.vigor_text,
                         "attunement": self.attunement_text,
                         "endurance": self.endurance_text,
                         "vitality": self.vitality_text,
                         "strength": self.strength_text,
                         "dexterity": self.dexterity_text,
                         "intelligence": self.intelligence_text,
                         "faith": self.faith_text,
                         "luck": self.luck_text}

        self.ability_text = {"HP": self.text_HP,
                             "FP": self.text_FP,
                             "Stamina": self.text_Stamina,
                             "Equipment load": self.text_Equipment_Load,
                             "Poise": self.text_Poise,
                             "Item Discovery": self.text_Item_Discovery,
                             "Attunement Slots": self.text_Attunement_Slots,
                             "Physical": self.text_Physical,
                             "VS Strike": self.text_Strike,
                             "VS Slash": self.text_Slash,
                             "VS Thrust": self.text_Thrust,
                             "Magic": self.text_Magic,
                             "Fire": self.text_Fire,
                             "Lightning": self.text_Lightning,
                             "Dark": self.text_Dark,
                             "Bleed": self.text_Bleed,
                             "Poison": self.text_Poison,
                             "Frost": self.text_Frost,
                             "Curse": self.text_Curse,
                             "Level":self.text_Level,
                             "Souls to next level": self.text_soulsToNext,
                             "Souls spend sum": self.text_soulsSpendSum}

        self.init_att = {"vigor": self.init_vigor,
                         "attunement": self.init_attunement,
                         "endurance": self.init_endurance,
                         "vitality": self.init_vitality,
                         "strength": self.init_strength,
                         "dexterity": self.init_dexterity,
                         "intelligence": self.init_intelligence,
                         "faith": self.init_faith,
                         "luck": self.init_luck}

        self.att_button = {"vigor": [self.vigor_sub_button, self.vigor_add_button],
                           "attunement": [self.attunement_sub_button, self.attunement_add_button],
                           "endurance": [self.endurance_sub_button, self.endurance_add_button],
                           "vitality": [self.vitality_sub_button, self.vitality_add_button],
                           "strength": [self.strength_sub_button, self.strength_add_button],
                           "dexterity": [self.dexterity_sub_button, self.dexterity_add_button],
                           "intelligence": [self.intelligence_sub_button, self.intelligence_add_button],
                           "faith": [self.faith_sub_button, self.faith_add_button],
                           "luck": [self.luck_sub_button, self.luck_add_button]}

        self.all_refresh(character)

        # set the connect on the combobox to change the character's birth
        self.comboBox.activated[str].connect(partial(self.change_birth, character))

        for att_str in self.att_list:
            # set the connect on the button (0 for sub, 1 for add)
            for sign in [0, 1]:
                self.att_button[att_str][sign].clicked.connect(partial(self.change_attribute, sign, character, att_str))
            # set the connect on the att_text input
            self.att_text[att_str].editingFinished.connect(partial(self.input_attribute, character, att_str))
        """
        Can't use lambda here
        Although the connect setup complete after the loop
        The lambda functions are not totally determined
        All the lambda function's parameter point to the address of the variable you put in
        All lambda will use the last att as its parameter
        Just use functools.partial to get the same effect
        
        wrong code:
        for att in self.att_list:
            for sign in [0, 1]:
                self.att_button[att_str][sign].clicked.connect(lambda: self.changeAttribute(sign, character, att_str))
            self.att_text[att_str].textChanged.connect(lambda: self.inputAttribute(character, att_str))
        """
    def change_birth(self, character, name):
        character.load_init_character(name)
        self.all_refresh(character)

    def change_attribute(self, signal, character, att_str):
        if signal:
            character.attribute[att_str] += 1
            if character.attribute[att_str] > 99:
                character.attribute[att_str] = 99
        else:
            character.attribute[att_str] -= 1
            if character.attribute[att_str] < character.init_attribute[att_str]:
                character.attribute[att_str] = character.init_attribute[att_str]
        self.att_text[att_str].setText(str(character.attribute[att_str]))
        self.calculate_refresh(character)

    def input_attribute(self, character, att_str):
        try:
            input_num = int(self.att_text[att_str].text())
        except ValueError:
            input_num = character.init_attribute[att_str]

        if input_num < character.init_attribute[att_str]:
            character.attribute[att_str] = character.init_attribute[att_str]
        elif input_num > 99:
            character.attribute[att_str] = 99
        else:
            character.attribute[att_str] = input_num
        self.att_text[att_str].setText(str(character.attribute[att_str]))
        self.calculate_refresh(character)

    def all_refresh(self, character):
        for att_str in self.att_list:
            self.att_text[att_str].setText(str(character.attribute[att_str]))
            self.init_att[att_str].setText(str(character.init_attribute[att_str]))
        self.calculate_refresh(character)

    def calculate_refresh(self, character):
        character.calculate()
        for ability_str in self.ability_list:
            self.ability_text[ability_str].setText(str(character.ability[ability_str]))


if __name__ == "__main__":
    Me = Character()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyWindow(MainWindow, Me)

    MainWindow.show()
    sys.exit(app.exec())
