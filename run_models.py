import tkinter as tk
from tkinter import filedialog
from scipy.io.wavfile import write as write_wav
import os

from src.processing import translate_text, synthesize_speech


def select_input_file():
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename(
        title="Выберите текстовый файл для перевода",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    return filepath


def select_output_file(initial_filename):
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.asksaveasfilename(
        title="Куда сохранить аудиофайл?",
        initialfile=initial_filename,
        defaultextension=".wav",
        filetypes=(("WAV files", "*.wav"), ("All files", "*.*"))
    )
    return filepath


if __name__ == "__main__":
    input_path = select_input_file()
    if not input_path:
        print("Файл не выбран.")
    else:
        with open(input_path, 'r', encoding='utf-8') as f:
            original_text = f.read()

        translated_text = translate_text(original_text)
        print(f"Переведенный текст: {translated_text}")

        audio_data, sampling_rate = synthesize_speech(translated_text)

        base_filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = select_output_file(f"{base_filename}_translated.wav")

        if output_path:
            write_wav(output_path, sampling_rate, audio_data)
            print(f"Аудио сохранено: {os.path.abspath(output_path)}")
        else:
            print("Сохранение отменено.")