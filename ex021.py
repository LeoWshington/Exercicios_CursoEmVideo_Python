from pygame import mixer
import time
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
time.sleep(50)
