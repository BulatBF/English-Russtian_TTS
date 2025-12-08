import numpy as np
from src.processing import translate_text, synthesize_speech


def test_translation_and_synthesis():
    """
    Тестирует полный цикл: перевод и синтез речи.
    Проверяет типы возвращаемых данных и их непустое значение.
    """
    # Входные данные
    original_text = "This is a test."

    # 1. Тестируем перевод
    translated_text = translate_text(original_text)

    # Проверяем, что результат - это непустая строка
    assert isinstance(translated_text, str)
    assert len(translated_text) > 0

    # 2. Тестируем синтез
    audio_data, sampling_rate = synthesize_speech(translated_text)

    # Проверяем, что аудио - это массив numpy, а частота - число
    assert isinstance(audio_data, np.ndarray)
    assert isinstance(sampling_rate, int)
    assert audio_data.size > 0
    assert sampling_rate > 0