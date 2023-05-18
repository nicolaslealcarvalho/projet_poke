from typing import Optional
import pygame

NB_POKEMON: int = 151
__all__ : list['Sound'] = []


class Sound(object):
    """
    this class is use to play the song during the game

    Exemple:
    >>> mus = Sound("assets/sound/music/Pokemon-Go.wav")
    >>> a = mus.get()
    >>> print(a != None)
    True
    >>> b = mus.un_load()
    >>> print(mus.sound == None)
    True
    """

    def __init__(self, path: str):
        __all__.append(self)
        self.path = path
        self.sound: Optional[pygame.mixer.Sound] = None

    def get(self):
        """


        """

        if self.sound is None:
            self.load()
        return self.sound

    def load(self):
        if not self.sound:
            self.sound = pygame.mixer.Sound(self.path)

    def un_load(self):
        del self.sound
        self.sound = None

    def __str__(self):
        print("Sound : {}".format(self.path))


BATTLE = Sound('assets/sound/music/Pokemon-Go.wav')

POKE_SOUND: list[Optional[Sound]] = [None] * (NB_POKEMON + 1)

def to_3_digit(num: int) -> str:
    if num < 10:
        return "00" + str(num)
    if num < 100:
        return "0" + str(num)
    return str(num)

# def load_poke_sound():
#     for id_ in range(1, NB_POKEMON + 1):
#         sound = Sound(f'assets/sound/cry/{to_3_digit(id_)}Cry.wav')
#         POKE_SOUND[id_] = sound


# def unload_poke_sound():
#     for ps in POKE_SOUND:
#         if ps:
#             ps.un_load()