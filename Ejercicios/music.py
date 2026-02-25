import sys
import time

def play_music():
    
    song_sequence = [
    ("I wanna da- 🕺", 0.55),
    ("I wanna dance in the lights ✨", 0.95),
    ("I wanna ro- 🤘", 0.55),
    ("I wanna rock yo' body 🔥", 0.90),
    ("I wanna go 🚗", 0.45),
    ("I wanna go for a ride 🛣️", 0.85),
    ("Hop in the music and 🎶", 0.95),
    ("Rock your body 🕺", 0.75),
    ("Rock that body 👯‍♀️", 0.65),
    ("come on, come on! 🙌", 0.12),
    ("Rock your body 💃", 0.78),
    ("(Rock that body) 📢", 0.10),
    ("Rock that body 💥", 0.80),
    ("come on, come on! 🥳", 0.12),
    ("Rock your body 🎤", 0.95)
]

    
    for line in song_sequence:
        print(line[0]) 
        
        if len(line) == 2:
            time.sleep(line[1])
        elif len(line) == 3:
            time.sleep(line[2]) 

play_music()