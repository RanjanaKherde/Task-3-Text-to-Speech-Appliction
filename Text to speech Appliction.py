#!/usr/bin/env python
# coding: utf-8

# In[9]:


import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pyttsx3
import os
class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        master.title("Text to Speech Converter")

        
        self.label = tk.Label(master, text="Enter text:")
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.text_entry = tk.Text(master, width=50, height=10)
        self.text_entry.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

       
        self.language_label = tk.Label(master, text="Select Language:")
        self.language_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.language_var = tk.StringVar()
        self.language_dropdown = ttk.Combobox(master, textvariable=self.language_var)
        self.language_dropdown['values'] = ['en', 'es', 'fr']  # Example languages, you can add more
        self.language_dropdown.grid(row=1, column=1, padx=5, pady=5)

       
        self.voice_label = tk.Label(master, text="Select Voice:")
        self.voice_label.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
        self.voice_var = tk.StringVar()
        self.voice_dropdown = ttk.Combobox(master, textvariable=self.voice_var)
        self.voice_dropdown.grid(row=1, column=3, padx=5, pady=5)

        
        self.rate_label = tk.Label(master, text="Rate:")
        self.rate_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.rate_slider = tk.Scale(master, from_=50, to=200, orient=tk.HORIZONTAL)
        self.rate_slider.set(100)  # Default rate
        self.rate_slider.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

        self.pitch_label = tk.Label(master, text="Pitch:")
        self.pitch_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.pitch_slider = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL)
        self.pitch_slider.set(50)  # Default pitch
        self.pitch_slider.grid(row=3, column=1, columnspan=3, padx=5, pady=5)

        self.volume_label = tk.Label(master, text="Volume:")
        self.volume_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.volume_slider = tk.Scale(master, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)
        self.volume_slider.set(1)  # Default volume
        self.volume_slider.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

        
        self.play_button = tk.Button(master, text="Play", command=self.play_text)
        self.play_button.grid(row=5, column=0, padx=5, pady=5)

        self.pause_button = tk.Button(master, text="Pause", command=self.pause_text)
        self.pause_button.grid(row=5, column=1, padx=5, pady=5)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_text)
        self.stop_button.grid(row=5, column=2, padx=5, pady=5)

        self.save_button = tk.Button(master, text="Save as Audio", command=self.save_audio)
        self.save_button.grid(row=5, column=3, padx=5, pady=5)

       
        self.engine = pyttsx3.init()

    def play_text(self):
        pass

    def pause_text(self):
        pass

    def stop_text(self):
        pass

    def save_audio(self):
        pass
class TextToSpeechApp:
   
    def play_text(self):
        text = self.text_entry.get("1.0", tk.END)
        language = self.language_var.get()
        rate = self.rate_slider.get()
        pitch = self.pitch_slider.get()
        volume = self.volume_slider.get()

        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        self.engine.setProperty('pitch', pitch)
        self.engine.setProperty('voice', language)

        self.engine.say(text)
        self.engine.runAndWait()

    def pause_text(self):
        self.engine.pause()

    def stop_text(self):
        self.engine.stop()

    def save_audio(self):
        text = self.text_entry.get("1.0", tk.END)
        language = self.language_var.get()
        rate = self.rate_slider.get()
        pitch = self.pitch_slider.get()
        volume = self.volume_slider.get()

        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        self.engine.setProperty('pitch', pitch)
        self.engine.setProperty('voice', language)

        file_path = filedialog.asksaveasfilename(defaultextension=".mp3")
        if file_path:
            self.engine.save_to_file(text, file_path)
            self.engine.runAndWait()
            messagebox.showinfo("Save", f"Audio saved as {file_path}")
    def main():
        root = tk.Tk()
        app = TextToSpeechApp(root)
        root.mainloop()

    if __name__ == "__main__":
        main()







