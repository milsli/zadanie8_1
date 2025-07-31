import streamlit as st
from openai import OpenAI
from dotenv import dotenv_values
import os
import pathlib
from pytubefix  import YouTube
from pytubefix.cli import on_progress
from pydub import AudioSegment
import subprocess

st.title("Generator streszczeń do wykładów z fizyki")
env = dotenv_values(".env")

@st.cache_resource
def get_openai_client():
    return OpenAI(api_key=env["OPENAI_API_KEY"])

subfolder = ""

def downloading(rok):
    urls = []
    if(rok == '2015'):
        urls = ['https://youtu.be/yMbpOZ9uJ-U', 'https://youtu.be/lryDr9TFa3c', 'https://youtu.be/lyv-5dd3hhU', 'https://youtu.be/YeuMI80YbvA'
           ,'https://youtu.be/Oujcs7qVQKg', 'https://youtu.be/_iPGJ2Yfe-U', 'https://youtu.be/WmRfNrEgOxg', 'https://youtu.be/QgB3GeFoMQc']
    elif(rok == '2016'):
        urls = ['https://youtu.be/2eR2n_v2hLA', 'https://youtu.be/PexDbIvDVy0', 'https://youtu.be/PeIprWcETD8', 'https://youtu.be/xFSbncszCI8',
        'https://youtu.be/fQwB-OQlwgE', 'https://youtu.be/e_GjIY2YhPc', 'https://youtu.be/mLzlF8ky3fk']
    elif(rok == '2017'):
        urls = ['https://youtu.be/_mK1Jryaq_Y', 'https://youtu.be/hl3sMFAuTSE', 'https://youtu.be/f6pBzjg5jiQ', 'https://youtu.be/I0tu5_BeeyI','https://youtu.be/LfZIUH8KJiA', 'https://youtu.be/S1SdE6Um5VM',
        'https://youtu.be/YMq8Diu5608', 'https://youtu.be/6r0fMl9aU-8', 'https://youtu.be/qg2H-B3sLJQ']
    elif(rok == '2018'):
        urls = ['https://youtu.be/MHwn2LUmiBE', 'https://youtu.be/YeLLuwYMibA', 'https://youtu.be/AuqMiJOaO5Q', 'https://youtu.be/KurhWg3X8cU',
        'https://youtu.be/UzCk2edqLbc', 'https://youtu.be/2qL51Acy-Co', 'https://youtu.be/XjXtuaIdBA8']
    elif(rok == '2019'):
        urls = ['https://youtu.be/7dQuOupLlF0', 'https://youtu.be/noGWUikakW8', 'https://youtu.be/jKpZrjb0gjE', 'https://youtu.be/2e3JM4_7b0Y',
        'https://youtu.be/f4OjAaeB0c8', 'https://youtu.be/xhmkPJTNt9E', 'https://youtu.be/X0PsQ4eCt5Q']
    elif(rok == '2020'):
        urls =  ['https://youtu.be/qA6BdCuV1i8', 'https://youtu.be/w1NUzKk30GE', 'https://youtu.be/vZ3J6VnOCV4', 'https://youtu.be/KcUANfasozs']
    elif(rok == '2021'):
        urls = ['https://youtu.be/r9cGfm6rzJI', 'https://youtu.be/FvAlsOFYk84', 'https://youtu.be/4yKAmwIyjPU',
        'https://youtu.be/dsf-Lqx4gRc', 'https://youtu.be/MS0x83n73Mc', 'https://youtu.be/MsVky0uTwKU']
    elif(rok == '2022'):
        urls = ['https://youtu.be/uqQuvMMmvic', 'https://youtu.be/DxDxKYgQG7c', 'https://youtu.be/ZxT0jNzYEko','https://youtu.be/IWNsx4Zj8f0', 'https://youtu.be/foYERTxPr5c', 'https://youtu.be/pp-Ltw7Cf2w',
        'https://youtu.be/RVi4btOi-mQ', 'https://youtu.be/w_LeTGf7VnY', 'https://youtu.be/eQpRf1nHHOY']
    elif(rok == '2023'):
        urls = ['https://youtu.be/Xi2g_hwAAeI', 'https://youtu.be/nqYGzezfb54', 'https://youtu.be/EYEaa4kqiI0', 'https://youtu.be/rbR4SCblF44', 'https://youtu.be/H6PhB-UcwUA', 
        'https://youtu.be/2S7cTMF9x4s', 'https://youtu.be/p9jgKRfXme8', 'https://youtu.be/67aJ79FRstc', 'https://youtu.be/RNNUdMkvgbU']
    elif(rok == '2024'):
        urls = ['https://youtu.be/6R2ASA7-g-c', 'https://youtu.be/cbo9wK86hjQ', 'https://youtu.be/RgTBW77aofA', 'https://youtu.be/Y8nUI0VY7eg', 
        'https://youtu.be/BIzQE4zteg0', 'https://youtu.be/-0wlsxjazj0', 'https://youtu.be/Rj3b_WIp258', 'https://youtu.be/fLHHkGfnRPo']
    elif(rok == '2025'):
        ['https://youtu.be/9Iwav_9Vqtc', 'https://youtu.be/6CUWGxUPwxY', 'https://youtu.be/fTcFsZ8p55g']

    st.text("Trwa pobieranie wykładów z roku: " + rok)
    
    download_progress = st.progress(0)
    
    counter = 0
    f_number = len(urls)
    for url in urls:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(yt.title)
        ys = yt.streams.get_lowest_resolution()
        subfolder
        ys.download(output_path=subfolder)
        counter += 1
                
        if f_number > 0:
            ddv = counter / f_number
            # download_progress = st.progress(ddv)
            download_progress.progress(int(100 * ddv))
        else:
            print("Brak plików do pobrania")

    # print()
    st.text('Zakończono pobieranie za rok ' + rok)
    st.text("Przetwarzanie plików ...")
    processing()

def compress_mp3(file_path, bitrate="64k"):
    temp_path = file_path + ".temp.mp3"
    subprocess.run([
        "ffmpeg", "-y", "-i", file_path, "-b:a", bitrate, temp_path
    ], check=True)

    os.replace(temp_path, file_path)

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
    if f_number < 1:
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
            st.text("Plik mp3 jest zbyt duży, kompresja ...")
            compress_mp3(file_path = mp3FileName, bitrate="64k")

        mp3FileSize = os.path.getsize(mp3FileName)
        if mp3FileSize > 25 * 1024 * 1024:
            st.text("Plik mp3 jest zbyt duży, nawet po kompresji. ")
            st.text("W następnej wersji programu ten problem zostanie rozwiązany.")
            continue

        st.text("Transkrypcja do formatu tekstowego ...")
        # transkrypcja pliku mp3 do tekstu  
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
    st.button("Generuj", on_click=downloading, kwargs={"rok": option})

