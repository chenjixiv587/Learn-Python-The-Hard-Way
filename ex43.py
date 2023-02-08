from sys import exit
from random import randint
from textwrap import dedent


class Scene():
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


# 死亡情景


class Death(Scene):
    # 玩家死亡的时候 嘲讽语句
    quips = [
        "You died, You kinda suck this.",
        "Your mom would be proud ... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
        The Gothons of Planet Percal #25 have invaded your ship and
        destroyed your entire crew.  You are the last surviving
        member and your last mission is to get the neutron destruct
        bomb from the Weapons Armory, put it in the bridge, andblow the ship up after getting into an escape pod.
        You're running down the central corridor to the Weapons
        Armory when a Gothon jumps out, red scaly skin, dark grimy
        teeth, and evil clown costume flowing around his hate
        filled body.  He's blocking the door to the Armory and
        about to pull a weapon to blast you.
        """))
        action = input("> ")
        if action == "shoot":
            print(dedent("""
            he lives and you dead
            """))
            return 'death'
        elif action == "dodge":
            print(dedent("""
            he lives and you dead
            """))
            return 'death'
        elif action == "tell a joke":
            print(dedent("""
            you r lucky.
            """))
            return 'laserWeaponArmory'
        else:
            print("DOES NOT COMPUTE")
            return 'centralCorridor'


class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
        the code is 3 digits.
        """))
        code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZZEDDDDD")
            guesses += 1
            guess = input("[keypad]> ")
        if guess == code:
            print(dedent("""
            go to the bridge
            """))
            return 'theBridge'
        else:
            print(dedent("""
            you will be dead.
            """))
            return 'death'


class TheBridge(Scene):
    def enter(self):
        print(dedent("""
        they haven't put their weapon out
        """))
        action = input("> ")
        if action == "throw the bomb":
            print(dedent("""uuuuu died"""))
            return 'death'
        elif action == "slowly place the bomb":
            print(dedent("put the bomb"))
            return 'escapePod'
        else:
            print("DOSE NOT COMPUTE")
            return 'theBridge'


class EscapePod(Scene):
    def enter(self):
        print(dedent("""You rush through the ship desperately trying to make it 
        There's 5 pods, which one do you take?
        """))
        goodPod = randint(1, 5)
        guess = input("[pod #]> ")
        if int(guess) != goodPod:
            print(
                dedent("""You jump into pod {guess} and hit the eject button"""))
            return 'death'
        else:
            print(dedent("""
            You jump into pod {guess} and hit the eject button
            You won!
            """))
            return 'finished'


class Finished(Scene):
    def enter(self):
        print("You win, good job")
        return 'finished'


class Engine():
    def __init__(self, sceneMap):
        self.sceneMap = sceneMap

    def play(self):
        currentScene = self.sceneMap.openingScene()
        lastScene = self.sceneMap.nextScene("finished")
        while currentScene != lastScene:
            nextSceneName = currentScene.enter()
            currentScene = self.sceneMap.nextScene(nextSceneName)
        # be sure to print out the last scene
        currentScene.enter()


class Map():
    scenes = {
        "centralCorridor": CentralCorridor(),
        "laserWeaponArmory": LaserWeaponArmory(),
        "theBridge": TheBridge(),
        "escapePod": EscapePod(),
        "death": Death(),
        "finished": Finished(),
    }

    def __init__(self, startScene):
        self.startScene = startScene

    def nextScene(self, sceneName):
        val = Map.scenes.get(sceneName)
        return val

    def openingScene(self):
        return self.nextScene(self.startScene)


AMap = Map('centralCorridor')
AGame = Engine(AMap)
AGame.play()
