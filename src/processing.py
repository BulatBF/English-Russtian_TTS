from transformers import pipeline, MarianMTModel, MarianTokenizer


def translate_text(text_to_translate: str) -> str:
    """Переводит текст с английского на русский."""
    print("Загрузка модели для перевода (Helsinki-NLP)...")
    model_name = "Helsinki-NLP/opus-mt-en-ru"

    # Явная загрузка помогает избежать KeyError в некоторых окружениях
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    translator = pipeline("translation", model=model, tokenizer=tokenizer)

    print("Перевод текста...")
    translated_text_list = translator(text_to_translate)
    return translated_text_list[0]['translation_text']