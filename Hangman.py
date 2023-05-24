import imp
import pygame
from sys import exit
from Szavak import Szavak
from Gombok import Gombok 
from Corpses import Corpses




# szavak beolvasás
szósorok = []
with open('szavak.txt', 'r', encoding='utf-8') as file:
    for sor in file.read().splitlines():
        szósorok.append(Szavak(sor))