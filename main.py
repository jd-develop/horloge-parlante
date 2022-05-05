#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import vlc
import time
from datetime import datetime
from gtts import gTTS


def main():
    text = f'Il est {datetime.now().strftime("%H heures, %M minutes et %S secondes")}.'
    language = 'fr'

    speech = gTTS(text=text, lang=language, slow=False)
    speech.save("speech.mp3")
    media = vlc.MediaPlayer("speech.mp3")
    media.play()
    time.sleep(5)
    while media.is_playing():
        time.sleep(1)


if __name__ == '__main__':
    main()
