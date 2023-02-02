from nose.tools import *
from ex47.game import Room


def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN")

def test_basic():
    print("I RAN!")



def testRoom():
    gold = Room("GoldRoom", """This room has gold in it
    and you can grab. There's a door to the north.""")

    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def testRoomPaths():
    center =  Room("Center", "Test room in the center")
    north = Room("North", "Test room in the north")
    south = Room("South", "Test room in the south")

    center.addPaths({"north":north, "south":south})
    assert_equal()

