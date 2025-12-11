from fastapi import FastAPI, Response
from pydantic import BaseModel
from processing import translate_text, synthesize_speech
from scipy.io.wavfile import write as write_wav
import io

# Создаем приложение FastAPI
app = FastAPI(
    title="English-Russian TTS API",
    description="API для перевода текста и синтеза речи.",
    version="1.0.0"
)


# Pydantic модель для валидации входящего запроса
class TextToTranslate(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the English-Russian TTS API. Please go to /docs to test the endpoints."}

@app.post("/synthesize")
async def synthesize(item: TextToTranslate):
    """
    Принимает текст на английском, переводит на русский и возвращает аудиофайл.
    """
    try:
        # Шаг 1: Перевод текста
        translated_text = translate_text(item.text)

        # Шаг 2: Синтез речи
        audio_data, sampling_rate = synthesize_speech(translated_text)

        # Шаг 3: Преобразование аудио в байты для отправки по сети
        buffer = io.BytesIO()
        write_wav(buffer, sampling_rate, audio_data)
        buffer.seek(0)

        # Шаг 4: Возврат аудиофайла в ответе
        return Response(content=buffer.getvalue(), media_type="audio/wav")

    except Exception as e:
        return {"error": str(e)}


# Команда для запуска
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)