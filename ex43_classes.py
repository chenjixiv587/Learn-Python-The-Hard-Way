class Scene():
    def enter(self):
        pass


class Engine():
    def __init__(self, sceneMap) -> None:
        pass

    def play(self):
        pass


class Death(Scene):
    def enter(self):
        pass


class CentralCorridor(Scene):
    def enter(self):
        pass


class LaserWeaponArmory(Scene):
    def enter(self):
        pass


class TheBridge(Scene):
    def enter(self):
        pass


class EscapePod(Scene):
    def enter(self):
        pass


class Map():
    def __init__(self, startScene):
        pass

    def nextScene(self, sceneName):
        pass

    def openingScene(self):
        pass


AMap = Map("centralCorridor")
AGame = Engine(AMap)
AGame.play()
