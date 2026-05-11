[![Run Python Tests](https://github.com/BulatBF/English-Russtian_TTS/actions/workflows/ci.yml/badge.svg)](https://github.com/BulatBF/English-Russtian_TTS/actions)
(https://english-russtiantts-ejbg6tll2daxlegbkjtmj4.streamlit.app/)


Проект по дисциплине «Проектный практикум». Интеллектуальный сервис, который переводит текст с английского на русский и мгновенно озвучивает его.

## Основные возможности
1. **Машинный перевод:** Использование модели `Helsinki-NLP/opus-mt-en-ru` для точного перевода.
2. **Синтез речи (TTS):** Преобразование текста в аудио с помощью модели Meta `facebook/mms-tts-rus`.
3. **Web UI:** Интерактивный интерфейс на **Streamlit**.
4. **REST API:** Программный доступ через **FastAPI**.
5. **CI/CD:** Автоматическое тестирование и развертывание.

## Стек технологий
1. **Язык:** Python 3.10+
2. **ML Frameworks:** PyTorch, Transformers (Hugging Face)
3. **Web/API:** Streamlit, FastAPI, Uvicorn
4. **Тестирование:** Pytest
5. **DevOps:** GitHub Actions (CI), Streamlit Cloud (CD)

## Локальная установка и запуск

1. **Клонируйте репозиторий:**
git clone https://github.com/BulatBF/English-Russtian_TTS.git
cd English-Russtian_TTS

2. **Настройте виртуальное окружение**
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install -r requirements.txt

3. **Запуск Web-интерфейса**
streamlit run src/app.py

4. **Запуск API**
uvicorn src.main:app --reload

## Тестирование
Для запуска автоматических тестов используйте:
PYTHONPATH=. pytest

