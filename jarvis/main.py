import queue
import sounddevice as sd
import vosk
import json
import pyttsx3
import webbrowser
import threading
import tkinter as tk
from tkinter import messagebox


engine = pyttsx3.init()

def falar(texto):
    def run():
        engine.say(texto)
        engine.runAndWait()
    threading.Thread(target=run).start()


def executar_comando(comando):
    comando = comando.lower().strip()
    print("Executando:", comando)

    if "leonardo" in comando:
        falar("Abrindo GitHub")
        webbrowser.open("https://github.com/LeozinDoGraal")

    elif "google" in comando:
        falar("Abrindo Google")
        webbrowser.open("https://www.google.com")

    elif "youtube" in comando:
        falar("Abrindo YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "discorde" in comando:
        falar("Abrindo Discord")
        webbrowser.open("https://discord.com/app")


    elif "chat" in comando:
        falar("Abrindo chat gpt goat")
        webbrowser.open("https://chatgpt.com/")

    else:
        print("Não reconhecido:", comando)


q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))


def ouvir():
    model = vosk.Model("vosk-model-small-pt-0.3")
    rec = vosk.KaldiRecognizer(model, 16000)

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):

        print("Jarvis ouvindo...")

        while True:
            data = q.get()

            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
            else:
                result = json.loads(rec.PartialResult())

            texto = result.get("text", "").strip().lower()

            if texto:
                print("Você disse:", texto)

                # WAKE WORD SIMPLES (do jeito que você pediu)
                if ("jarvis" in texto or 
                    "jarves" in texto or 
                    "jardins" in texto):

                    comando = (texto
                               .replace("jarvis", "")
                               .replace("jarves", "")
                               .replace("jardins", "")
                               .strip())
                else:
                    comando = texto

                if comando:
                    executar_comando(comando)


def iniciar_jarvis():
    falar("Jarvis ativado")
    thread = threading.Thread(target=ouvir, daemon=True)
    thread.start()


def login():
    if entry_user.get() == "admin" and entry_pass.get() == "admin":
        messagebox.showinfo("Sucesso", "Login realizado!")
        iniciar_jarvis()
        login_frame.pack_forget()
        main_frame.pack()
    else:
        messagebox.showerror("Erro", "Login incorreto")

root = tk.Tk()
root.title("Jarvis")
root.geometry("300x200")

login_frame = tk.Frame(root)
login_frame.pack()

tk.Label(login_frame, text="Usuário").pack()
entry_user = tk.Entry(login_frame)
entry_user.pack()

tk.Label(login_frame, text="Senha").pack()
entry_pass = tk.Entry(login_frame, show="*")
entry_pass.pack()

tk.Button(login_frame, text="Login", command=login).pack(pady=10)

main_frame = tk.Frame(root)
tk.Label(main_frame, text="Jarvis rodando...").pack(pady=20)

root.mainloop()