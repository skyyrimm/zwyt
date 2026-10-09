import sys
import time 
from threading import Lock, Thread 

lock = Lock()


def animate_text(text, delay=0.06):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
        
        
def sing_lyrics(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)


def sing_song():
    lyrics = [
        ("Well, maybe we got lost in translation,  ", 0.08),
        ("Maybe I asked for too much ", 0.079),
        ("But maybe this thing was a masterpiece ", 0.078),
        ("'til you tore it all up", 0.0789),
        ("Running scared, I was there ", 0.0889),
        ("I remember it   all too well              ", 0.178),
        ("And you call me up again   just to break me like a promise  ", 0.09999999),
        ("So casually cruel  in the name of bein' honest  ", 0.098),
        ("I'm a crumpled-up    piece of paper lyin' here ", 0.089),
        ("'Cause I remember it  all ,  all ,  all    ", 0.098999),
    ]
    
    delays = [0.1, 2.8, 5.0, 7.9, 10.1, 10.998, 16.9, 21.2, 25.3,28.4,]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyrics, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
        
        
if __name__ == "__main__":
    try:
        sing_song()
    except KeyboardInterrupt:
        pass