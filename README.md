Olha o codigo em lua é esse mas assim tá pré definido com oq eu escolhi caso queira muda o comando de voz e em 

if "leonardo" in comando:
        falar("Abrindo GitHub")
        webbrowser.open("https://github.com/LeozinDoGraal")

Ali depois do if que tá escrito leonardo é o que vc tem que falar para acontecer as ações que no caso ai é abrir o git hub ai o link fica ali em baixo e os outros comandos estão abaixo desse ai para criar um comando é so copiar um desses e substituir pelo oq vc quer :D

As bibliotecas usadas ficaram abaixo: 

import queue
import sounddevice as sd
import vosk
import json
import pyttsx3
import webbrowser
import threading
import tkinter as tk
from tkinter import messagebox
