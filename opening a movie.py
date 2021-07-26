#create a class
class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
    #importing os module
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = 'MP4'

#playing a video named my_video from the system
movie = Movie_MP4(r'D:\my_video.mp4')
movie.play()
