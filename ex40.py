class Song(object):
    def __init__(self, lyrics) -> None:
        self.lyrics = lyrics

    def singMeASong(self):
        for line in self.lyrics:
            print(line)


lyrics = ["hhhh", "hjidsbisdivbisdbijv", "bcisidbisdiuvb"]
mySong = Song(lyrics)
mySong.singMeASong()
