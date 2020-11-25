# Created by MechAviv
# Quest ID :: 20831
# Lesson 3 - Battle Basics 2

sm.setSpeakerID(1102102)
if sm.sendAskYesNo("Did you enjoy the drink? You better have! It is the special concoction of my people, the Piyo Tribe!\r\nNow... Pop quiz! Do you remember how to fight? Defeat 3 #o9300730#  monsters and bring me 3 #t4000489# items!"):
    sm.setSpeakerID(1102102)
    sm.removeEscapeButton()
    sm.sendNext("What do you mean, you don't know what to do! Press the Ctrl key to perform a basic attack! What do you mean, I forgot to tell you how to pick up items? Just press the Z key! ")


    sm.startQuest(20831)
    for i in range(3):
        sm.spawnMob(9300730, -364, -7, False)
    sm.playSound("Aran/balloon", 100)
    sm.avatarOriented("UI/tutorial.img/5")
else:
    sm.setSpeakerID(1102102)
    sm.sendNext("What? Your failure is my failure as a teacher, and I never fail!")


