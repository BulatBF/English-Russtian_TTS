import torch
from transformers import pipeline, VitsModel, AutoTokenizer

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