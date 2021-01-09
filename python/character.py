"""
author: Wang Shuowei
date: 2020.01.05
"""


class Character():
    def __init__(self):
        self.init_attribute_table = {"Knight": [9, 12, 10, 11, 15, 13, 12, 9, 9, 7],
                                     "Mercenary": [8, 11, 12, 11, 10, 10, 16, 10, 8, 9],
                                     "Warrior": [7, 14, 6, 12, 11, 16, 9, 8, 9, 11],
                                     "Herald": [9, 12, 10, 9, 12, 12, 11, 8, 13, 11],
                                     "Thief": [5, 10, 11, 10, 9, 9, 13, 10, 8, 14],
                                     "Assassin": [10, 10, 14, 11, 10, 10, 14, 11, 9, 10],
                                     "Sorcerer": [6, 9, 16, 9, 7, 7, 12, 16, 7, 12],
                                     "Pyromancer": [8, 11, 12, 10, 8, 12, 9, 14, 14, 7],
                                     "Cleric": [7, 10, 14, 9, 7, 12, 8, 7, 16, 13],
                                     "Deprived": [1, 10, 10, 10, 10, 10, 10, 10, 10, 10]}

        self.init_attribute = dict()
        self.attribute = dict()
        self.ability = dict()

        self.load_init_character("Knight")

    def give_value_to_init_attribute(self, att_list):
        self.init_attribute["level"] = att_list[0]
        self.init_attribute["vigor"] = att_list[1]
        self.init_attribute["attunement"] = att_list[2]
        self.init_attribute["endurance"] = att_list[3]
        self.init_attribute["vitality"] = att_list[4]
        self.init_attribute["strength"] = att_list[5]
        self.init_attribute["dexterity"] = att_list[6]
        self.init_attribute["intelligence"] = att_list[7]
        self.init_attribute["faith"] = att_list[8]
        self.init_attribute["luck"] = att_list[9]

    def load_init_character(self, name):
        self.give_value_to_init_attribute(self.init_attribute_table[name])
        self.attribute = self.init_attribute.copy()

    def calculate(self):
        self.ability["HP"] = self.function7()
        self.ability["FP"] = self.function8()
        self.ability["Stamina"] = self.function9()
        self.ability["Equipment load"] = self.function10()
        self.ability["Poise"] = self.function11()
        self.ability["Item Discovery"] = self.function12()
        self.ability["Attunement Slots"] = self.function13()

        self.ability["Physical"] = self.function14()
        self.ability["VS Strike"] = self.ability["Physical"]
        self.ability["VS Slash"] = self.ability["Physical"]
        self.ability["VS Thrust"] = self.ability["Physical"]

        self.ability["Magic"] = self.function15()
        self.ability["Fire"] = self.function16()
        self.ability["Lightning"] = self.function17()
        self.ability["Dark"] = self.function18()

        self.ability["Bleed"] = self.function19()
        self.ability["Poison"] = self.function20()
        self.ability["Frost"] = self.function21()
        self.ability["Curse"] = self.function22()

        self.ability["Level"] = self.function23()
        self.ability["Souls to next level"] = self.function24(self.ability["Level"])
        self.ability["Souls spend sum"] = self.function25(self.ability["Level"])

    def att_sum(self):
        return sum(self.attribute.values()) - self.attribute["level"]

    def init_att_sum(self):
        return sum(self.init_attribute.values()) - self.init_attribute["level"]

    def function1(self, att):
        if att < 150:
            return (att - 1)*60/149 + 40
        elif att < 170:
            return (att + 50)/2
        elif att < 240:
            return (att - 240)/7 + 120
        else:
            return (att - 240)*10/217 + 120

    def function2(self, att):
        if att < 150:
            return (att - 1)*30/149 + 90
        elif att < 190:
            return att - 30
        elif att < 240:
            return (att - 240)*3/10 + 175
        else:
            return (att - 240)*25/651 + 175

    def function3(self, att):
        if att < 15:
            return att/3
        elif att < 25:
            return (att - 15)*17/10 + 5
        elif att < 40:
            return (att - 40)*6/5 + 40
        else:
            return (att - 40)*20/59 + 40

    def function4(self, att):
        if att < 30:
            return att/3
        elif att < 40:
            return (att - 10)/2
        elif att < 60:
            return (att - 20)*3/4
        else:
            return (att - 60)*10/39 + 30

    def function5(self, att):
        if att < 30:
            return att*2/3
        elif att < 40:
            return att*2 - 40
        elif att < 60:
            return (att - 40)*3/2 + 40
        else:
            return (att - 60)*10/13 + 70

    def function6(self, att):
        if att < 30:
            return 0
        elif att < 40:
            return att*3 - 90
        elif att < 60:
            return att/2 + 10
        else:
            return (att - 60)*10/39 + 40

    def function7(self):
        hp_list = [0, 300, 301, 305, 311, 320, 331, 345, 362, 381, 403, 427, 454, 483, 515, 550, 594, 638, 681, 723, 764,
                   804, 842, 879, 914, 947, 977, 1000, 1019, 1038, 1056, 1074, 1092, 1109, 1125, 1141, 1157, 1172, 1186,
                   1200, 1213, 1226, 1238, 1249, 1260, 1269, 1278, 1285, 1292, 1297, 1300, 1302, 1304, 1307, 1309, 1312,
                   1314, 1316, 1319, 1321, 1323, 1326, 1328, 1330, 1333, 1335, 1337, 1340, 1342, 1344, 1346, 1348, 1351,
                   1353, 1355, 1357, 1359, 1361, 1363, 1365, 1367, 1369, 1371, 1373, 1375, 1377, 1379, 1381, 1383, 1385,
                   1386, 1388, 1390, 1391, 1393, 1395, 1396, 1397, 1399, 1400]
        return hp_list[self.attribute["vigor"]]

    def function8(self):
        fp_list = [0, 50, 53, 58, 62, 67, 72, 77, 82, 87, 93, 98, 103, 109, 114, 120, 124, 130, 136, 143, 150, 157, 165,
                   173, 181, 189, 198, 206, 215, 224, 233, 242, 251, 260, 270, 280, 283, 286, 289, 293, 296, 299, 302,
                   305, 309, 312, 315, 318, 320, 323, 326, 329, 332, 334, 337, 339, 342, 344, 346, 348, 350, 352, 355,
                   358, 361, 364, 366, 369, 372, 375, 377, 380, 383, 385, 388, 391, 394, 396, 399, 402, 404, 407, 409,
                   412, 415, 417, 420, 422, 425, 427, 430, 432, 434, 437, 439, 441, 444, 446, 448, 450]
        return fp_list[self.attribute["attunement"]]

    def function9(self):
        stamina_list = [0, 80, 82, 83, 85, 86, 88, 89, 91, 92, 94, 95, 97, 98, 100, 102, 104, 106, 108, 110, 112, 114,
                        116, 118, 120, 122, 125, 127, 129, 132, 134, 136, 139, 141, 144, 146, 149, 152, 154, 157, 160,
                        160, 160, 160, 160, 160, 161, 161, 161, 161, 161, 161, 162, 162, 162, 162, 162, 162, 163, 163,
                        163, 163, 163, 163, 164, 164, 164, 164, 164, 164, 165, 165, 165, 165, 165, 165, 166, 166, 166,
                        166, 166, 166, 167, 167, 167, 167, 167, 167, 168, 168, 168, 168, 168, 168, 169, 169, 169, 169,
                        169, 170]
        return stamina_list[self.attribute["endurance"]]

    def function10(self):
        return self.attribute["vitality"] + 40

    def function11(self):
        return 0

    def function12(self):
        return self.attribute["luck"] + 100

    def function13(self):
        temp = self.attribute["attunement"]
        slot_list = [10, 14, 18, 24, 30, 40, 50, 60, 80, 99]
        for i in range(10):
            if temp < slot_list[i]:
                return i
        return 10

    def function14(self):
        return int(self.function1(self.att_sum()) + \
               self.function3(self.attribute["vitality"]) + self.function4(self.attribute["strength"]))

    def function15(self):
        return int(self.function1(self.att_sum()) + self.function5(self.attribute["intelligence"]))

    def function16(self):
        return int(self.function1(self.att_sum()) + self.function5(self.attribute["strength"]))

    def function17(self):
        return int(self.function1(self.att_sum()) + self.function5(self.attribute["endurance"]))

    def function18(self):
        return int(self.function1(self.att_sum()) + self.function5(self.attribute["faith"]))

    def function19(self):
        return int(self.function2(self.att_sum()) + self.function6(self.attribute["endurance"]))

    def function20(self):
        return int(self.function2(self.att_sum()) + self.function6(self.attribute["vitality"]))

    def function21(self):
        return int(self.function2(self.att_sum()) + self.function6(self.attribute["vigor"]))

    def function22(self):
        return int(self.function2(self.att_sum()) + self.function6(self.attribute["luck"]))

    def function23(self):
        return self.att_sum() - self.init_att_sum() + self.init_attribute["level"]

    def function24(self, att):
        if att <= 10:
            return int(0.12*att**2+16*att+657.4)
        elif att < 802:
            return int(-1e-12*att**4 + 0.02*att**3 + 3.12*att**2 + 111.78*att - 786.2)
        else:
            return "-"

    def function25(self, att):
        souls_sum = 0
        for i in range(self.init_attribute["level"], att):
            souls_sum += self.function24(i)
        return souls_sum

if __name__ == "__main__":
    pass
