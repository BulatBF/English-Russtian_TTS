import streamlit as st
from processing import translate_text, synthesize_speech
import io

st.set_page_config(layout="wide")

st.title("Сервис для перевода и озвучивания текста")

st.write("Введите текст на английском языке, чтобы перевести его на русский и получить аудиодорожку.")

input_text = st.text_area("Текст для перевода:",
                          "Hello, this is a demonstration of the English-to-Russian translation model.", height=150)

if st.button("Перевести и озвучить"):
    if not input_text.strip():
        st.warning("Пожалуйста, введите текст.")
    else:
        with st.spinner("Идет перевод..."):
            translated_text = translate_text(input_text)

        st.success(f"**Переведенный текст:** {translated_text}")

        with st.spinner("Идет синтез речи... Это может занять некоторое время."):
            audio_data, sampling_rate = synthesize_speech(translated_text)

            audio_bytes = io.BytesIO()
            st.audio(audio_data, sample_rate=sampling_rate)

        st.success("Аудио сгенерировано!")