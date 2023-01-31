from sys import exit
from random import randint
from textwrap import dedent


class Scene():
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


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


class Map():
    pass
