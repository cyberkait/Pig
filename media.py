# imports
from dice import Die
import playsound as ps
import random


# dictionary of pig sounds
pigs = {
    1: "sound\pig1.wav",
    2: "sound\pig2.wav",
    3: "sound\pig3.wav",
    4: "sound\pig4.wav",
    5: "sound\pig5.wav",
    6: "sound\pig6.wav",
    7: "sound\pig7.wav",
    8: "sound\pig8.wav",
    9: "sound\pig9.wav",
    10: "sound\pig10.wav",
    11: "sound\pig11.wav",
    12: "sound\pig12.wav",
    13: "sound\pig13.wav",
    14: "sound\pig14.wav",
    15: "sound\pig15.wav",
    16: "sound\pig16.wav",
}


# All other sounds.
loserSound = "sound\lose.wav"

# functions


def p_roll():
    """
    Plays roll sound.
    """
    ps.playsound("sound\dice.wav")


def p_win():
    """
    Plays win sound.
    """
    ps.playsound("sound\win.wav")


def p_loose():
    """
    Plays lose sound.
    """
    ps.playsound("sound\lose.wav")


def p_bank():
    ps.playsound("sound\BScore.wav")


def pigSound():
    num = random.randint(1, 16)
    ps.playsound(pigs[num])
