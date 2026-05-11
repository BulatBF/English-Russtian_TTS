import torch
from transformers import pipeline, VitsModel, AutoTokenizer, MarianMTModel, MarianTokenizer


def translate_text(text_to_translate: str) -> str:
    """Переводит текст с английского на русский."""
    print("Загрузка модели для перевода (Helsinki-NLP)...")
    model_name = "Helsinki-NLP/opus-mt-en-ru"

    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    translator = pipeline("translation", model=model, tokenizer=tokenizer)

    print("Перевод текста...")
    translated_text_list = translator(text_to_translate)
    return translated_text_list[0]['translation_text']


def synthesize_speech(text_to_synthesize: str):
    """Синтезирует речь из текста на русском языке."""
    print("Загрузка модели для синтеза речи...")
    model_name = "facebook/mms-tts-rus"

    tts_model = VitsModel.from_pretrained(model_name)
    tts_tokenizer = AutoTokenizer.from_pretrained(model_name)

    print("Генерация аудио...")
    inputs = tts_tokenizer(text_to_synthesize, return_tensors="pt")
    with torch.no_grad():
        output = tts_model(**inputs).waveform

    sampling_rate = tts_model.config.sampling_rate
    return output.squeeze().numpy(), sampling_rate