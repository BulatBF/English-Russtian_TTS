import torch
from transformers import pipeline, VitsModel, AutoTokenizer
from scipy.io.wavfile import write as write_wav
import os
import tkinter as tk
from tkinter import filedialog


# --- Функции для работы с моделями ---

def translate_text(text_to_translate):
    """Переводит текст с английского на русский."""
    print("Загрузка модели для перевода (может занять время при первом запуске)...")
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ru")
    print("Перевод текста...")
    translated_text_list = translator(text_to_translate)
    return translated_text_list[0]['translation_text']


def synthesize_speech(text_to_synthesize):
    """Синтезирует речь из текста на русском языке."""
    print("Загрузка модели для синтеза речи...")
    tts_model = VitsModel.from_pretrained("facebook/mms-tts-rus")
    tts_tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-rus")

    print("Генерация аудио...")
    inputs = tts_tokenizer(text_to_synthesize, return_tensors="pt")
    with torch.no_grad():
        output = tts_model(**inputs).waveform

    sampling_rate = tts_model.config.sampling_rate
    return output.squeeze().numpy(), sampling_rate


# --- Функции для интерактивного выбора файлов ---

def select_input_file():
    """Открывает диалоговое окно для выбора текстового файла."""
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно tkinter
    filepath = filedialog.askopenfilename(
        title="Выберите текстовый файл для перевода",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    return filepath


def select_output_file(initial_filename):
    """Открывает диалоговое окно для сохранения аудиофайла."""
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.asksaveasfilename(
        title="Куда сохранить аудиофайл?",
        initialfile=initial_filename,
        defaultextension=".wav",
        filetypes=(("WAV files", "*.wav"), ("All files", "*.*"))
    )
    return filepath


# --- Основной процесс ---

if __name__ == "__main__":
    # 1. Выбрать исходный файл и прочитать текст
    input_path = select_input_file()
    if not input_path:
        print("Файл не выбран. Программа завершена.")
    else:
        with open(input_path, 'r', encoding='utf-8') as f:
            original_text = f.read()
        print(f"Оригинальный текст из файла: {original_text}")
        print("-" * 30)

        # 2. Перевести текст
        translated_text = translate_text(original_text)
        print(f"Переведенный текст: {translated_text}")
        print("-" * 30)

        # 3. Синтезировать речь
        audio_data, sampling_rate = synthesize_speech(translated_text)

        # 4. Предложить, куда сохранить результат
        base_filename = os.path.splitext(os.path.basename(input_path))[0]
        suggested_filename = f"{base_filename}_translated.wav"

        output_path = select_output_file(suggested_filename)

        if not output_path:
            print("Место для сохранения не выбрано. Программа завершена.")
        else:
            # 5. Сохранить аудиофайл
            write_wav(output_path, sampling_rate, audio_data)
            print(f"Аудио успешно сохранено в файл: {os.path.abspath(output_path)}")