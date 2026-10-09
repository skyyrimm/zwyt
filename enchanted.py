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


def sing_lyric(lyric, delay, speed):
	time.sleep(delay)
	animate_text(lyric, speed)


def sing_song():
	lyrics = [
		("This is me praying that", 0.086),
		("This was the very first page", 0.0931),
		("Not where the story line ends", 0.091),
		("My thoughts will echo your name", 0.096),
		("until I see you again", 0.12),
		("These are the words I held back", 0.087),
		("as I was leaving too soon", 0.1256),
		("I was enchanted to meet you", 0.159799),
		("Please don't be in love with someone else", 0.132),
		("Please don't have somebody waiting on you ", 0.126),
		("Please don't be in love with someone else", 0.132),
		("Please don't have somebody waiting on you ", 0.131),
	]

	delays = [
		0.5,  # This is me praying that
		3.5,  # This was the very first page
		6.38,  # Not where the story line ends
		9.2,  # My thoughts will echo your name
		12.2,  # until I see you again
		14.98,  # These are the words I held back
		16.6,  # as I was leaving too soon
		20.3,  # I was enchanted to meet you
		26.5987,  # Please don't be in love with someone else
		32.3,  # Please don't have somebody waiting on you
		38.25,  # Please don't be in love with someone else
		42.23,  # Please don't have somebody waiting on you
	]

	threads = []
	for i in range(len(lyrics)):
		lyric, speed = lyrics[i]
		t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
		threads.append(t)
		t.start()

	for t in threads:
		t.join()


if __name__ == "__main__":
	try:
		sing_song()
	except KeyboardInterrupt:
		pass
