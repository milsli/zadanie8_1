import streamlit as st
from openai import OpenAI
from dotenv import dotenv_values
import os
import pathlib

from pydub import AudioSegment

st.title("Generator streszczeń do wykładów z fizyki")
env = dotenv_values(".env")

@st.cache_resource
def get_openai_client():
    return OpenAI(api_key=env["OPENAI_API_KEY"])


subfolder = "../"
def processing():
    st.write("Wybrano folder : " + subfolder)

    try:
        filenames = os.listdir(subfolder)
    except:
        st.text("Brakuje katalogu lub plików")
        st.text("należy w pierwszej kolejności uruchomić: python downloading.py")
        st.text("a w następnej kolejności: streamlit run summarize.py")
        return

    f_number = len(filenames)
    if f_number > 0:
        Exception("Brak plików")

    audiofolder = subfolder + "/audio"
    textfolder = subfolder + "/text"
    summaryfolder = subfolder + "/summary"
    try:
        os.mkdir(audiofolder)        
    except FileExistsError:
        st.text("audio folder already exists")
    try:
        os.mkdir(textfolder)        
    except FileExistsError:
        st.text("text folder already exists")
    try:
        os.mkdir(summaryfolder)        
    except FileExistsError:
        st.text("summary folder already exists")
    
    file_progress_bar = st.progress(0)

    counter = 0
    for filename in filenames:
        if os.path.isdir(subfolder + "/" + filename):
            f_number = f_number - 1
            continue

        counter = counter + 1        
        ddv = counter / f_number
        st.text("Wydzielanie ścieżki dźwiękowej ...")
        sound = AudioSegment.from_file(subfolder + "/" + filename)
        
        start_point = len(sound) / 10
        stop_point = len(sound) / 2
        useful_part = sound[start_point:stop_point]

        mp3FileName = audiofolder + "/" + pathlib.Path(filename).stem + ".mp3"
        st.text("Zapisywanie w formacie .mp3 ...")
        useful_part.export(mp3FileName, format="mp3")
        st.text("Transkrypcja do formatu tekstowego ..    " + mp3FileName)

        # sprawdzenie rozmiaru pliku mp3
        mp3FileSize = os.path.getsize(mp3FileName)
        if mp3FileSize > 25 * 1024 * 1024:
            st.text("Plik mp3 ma zbyt duży rozmiar  - pominięcie przetwarzania")
            st.text("W kolejnej wersji zostanie zaimplementowana redukcja rozmiaru")
            continue

        with open(mp3FileName, "rb") as f:
            transcript = get_openai_client().audio.transcriptions.create(
            file=f,
            model="whisper-1",
        )
            
        st.text("Zapisywanie tekstu ...")
        textFileName = textfolder + "/" + pathlib.Path(filename).stem + ".txt"
        with open(textFileName, "w") as f:
            f.write(transcript.text)

        st.text("Generowanie streszczenia ...")
        summary = get_openai_client().chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Streszczaj teksty w sposób jasny i rzeczowy."},
                {"role": "user", "content": f"Podsumuj ten tekst:\n\n{transcript.text}"}
            ],
            temperature=0.5,      
        )

        st.text("Zapisywanie streszczenia ...")
        summaryFileName = summaryfolder + "/" + pathlib.Path(filename).stem + ".txt"
        with open(summaryFileName, "w") as f:
            f.write(summary.choices[0].message.content)

        file_progress_bar.progress(int(100 * ddv))

with st.sidebar:
    st.subheader("Podaj rok")
    option = st.selectbox(
        "Rok wykładów", 
        ("2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"))
    st.write("Wybrałeś wykłady z roku ", option)

    subfolder = "lectures" + option

    st.button("Generuj", on_click=processing)

