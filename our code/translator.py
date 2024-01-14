import tkinter as tk
from gtts import gTTS
import googletrans
from tkinter import Frame, Label, PhotoImage, Scrollbar, Text, ttk, messagebox
from tkinter.constants import END, GROOVE, LEFT
import langdetect
import textblob
import os
import pycountry
from playsound import playsound

window = tk.Tk()
window.title("Language Translator")
window.geometry("1080x400")

# ttk style
style = ttk.Style()
style.configure("TButton", foreground="black", background="red", font=("Roboto", 15, "bold"), borderwidth="2")
style.configure("new.TButton", foreground="black", background="green")

# icon
image_icon = PhotoImage(file="icon.png")
window.iconphoto(False, image_icon)

# arrow image
arrow_image = PhotoImage(file="arrow.png")
image_label = Label(window, image=arrow_image, width=150)
image_label.place(x=463, y=40)

# All language
language = googletrans.LANGUAGES
language_list = list(language.values())

# left side language combobox
left_combo = ttk.Combobox(window, values=language_list, font="Roboto 12", state='r')
left_combo.place(x=110, y=40)
left_combo.set("english")

# left side frame and text box
f_left = Frame(window, bg="gray70", bd=5)
f_left.place(x=10, y=100, width=440, height=250)

left_text = Text(f_left, font="Roboto 16", bg="white", relief=GROOVE)
left_text.place(x=-3, y=-3, width=412, height=246)

scrollbar_left = Scrollbar(f_left)
scrollbar_left.pack(side="right", fill="y")

scrollbar_left.configure(command=left_text.yview)
left_text.configure(yscrollcommand=scrollbar_left.set)

# right side language combobox
right_combo = ttk.Combobox(window, values=language_list, font="Roboto 12", state='r')
right_combo.place(x=730, y=40)
right_combo.set("hindi")

# left side frame and text box
f_right = Frame(window, bg="gray70", bd=5)
f_right.place(x=630, y=100, width=440, height=250)

right_text = Text(f_right, font="Roboto 16", bg="white")
right_text.place(x=-3, y=-3, width=412, height=246)

scrollbar_right = Scrollbar(f_right)
scrollbar_right.pack(side="right", fill="y")

scrollbar_right.configure(command=right_text.yview)
right_text.configure(yscrollcommand=scrollbar_right.set)

# Translate Button
def translate():
    translate_btn.configure(style="new.TButton")

    try:
        text_ = left_text.get(1.0, END)
        c2 = left_combo.get()
        c3 = right_combo.get()

        if text_:
            lan = langdetect.detect(text_)

            for i, j in language.items():
                if j == c3:
                    lan_ = i

            left_language_name = pycountry.languages.get(alpha_2=lan)

            try:
                left_combo.set(left_language_name.name.lower())
            except Exception as e:
                left_combo.set("english")

            words = textblob.TextBlob(text_)
            words = words.translate(from_lang=lan, to=str(lan_))
            right_text.delete(1.0, END)
            right_text.insert(END, words)

    except Exception as e:
        print("Translation Error:", e)
        messagebox.showerror("Translation Error", f"Error: {e}")

        # Debugging code
        print("Debugging Info:")
        print("text_:", text_)
        print("c2:", c2)
        print("c3:", c3)

# Translate Button
translate_btn = ttk.Button(window, text="Translate", command=translate)
translate_btn.place(x=476, y=250)

# Play button
def play():
    text_ = right_text.get(1.0, END)
    try:
        words = textblob.TextBlob(text_)
        lan = langdetect.detect(text_)
        myobj = gTTS(text=text_, lang=lan, slow=False)
        myobj.save("audio.mp3")
        os.system("audio.mp3")
    except Exception as e:
        print(e)
        messagebox.showerror("audio", "no text to play")

# Play button
play_btn = ttk.Button(window, text="Play", command=play)
play_btn.place(x=476, y=290)

# window loop
window.configure(bg="gray95")
window.mainloop()
