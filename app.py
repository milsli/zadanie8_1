import streamlit as st
import boto3
from pydub import AudioSegment
import os
import pathlib
import subprocess
from openai import OpenAI
from dotenv import dotenv_values

def compress_mp3(file_path, bitrate="64k"):
    temp_path = file_path + ".temp.mp3"
    subprocess.run([
        "ffmpeg", "-y", "-i", file_path, "-b:a", bitrate, temp_path
    ], check=True)

    os.replace(temp_path, file_path)

@st.cache_resource
def get_openai_client():
    return OpenAI(api_key=env["OPENAI_API_KEY"])

def createDirectory(dir_name = ""):
    dir_exists = os.path.isdir(dir_name)
    if not dir_exists:
        os.makedirs(dir_name, exist_ok=True)


st.title("Generator streszczeń do wykładów z fizyki")
env = dotenv_values(".env")

if 'OPENAI_API_KEY' in st.secrets:
    env["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]    
if 'AWS_ENDPOINT_URL_S3' in st.secrets:
    env["AWS_ENDPOINT_URL_S3"] = st.secrets["AWS_ENDPOINT_URL_S3"]
if 'AWS_ACCESS_KEY_ID' in st.secrets:
    env["AWS_ACCESS_KEY_ID"] = st.secrets["AWS_ACCESS_KEY_ID"]
if 'AWS_SECRET_ACCESS_KEY' in st.secrets:
    env["AWS_SECRET_ACCESS_KEY"] = st.secrets["AWS_SECRET_ACCESS_KEY"]    

def download(rok):  
    s3 = boto3.client('s3', endpoint_url=env["AWS_ENDPOINT_URL_S3"], aws_access_key_id=env["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=env["AWS_SECRET_ACCESS_KEY"])

    BUCKET_NAME = "phisicsvideo"  

    main_dir = "download/" + rok + "/"
    film_dir = main_dir + "film/"
    audio_dir = main_dir + "audio/"
    summary_dir = main_dir + "summary/"
    text_dir = main_dir + "text/"

    createDirectory(main_dir)
    createDirectory(film_dir)
    createDirectory(audio_dir)
    createDirectory(summary_dir)
    createDirectory(text_dir)

    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=rok)
    filmsNumber = response['KeyCount']
    filmsCounter = 0
    download_progress = st.progress(0)
    download_progress.text("Trwa pobieranie wykładów z roku: " + rok)
    
        
    for obj in response["Contents"]: 
        if "mp4" in obj["Key"]:
            film = obj["Key"].replace(rok + '/','')  
            print(film)
            film_path = film_dir + film
            if not os.path.exists(film_path):
                s3.download_file(BUCKET_NAME, obj["Key"],film_path)
            
        filmsCounter += 1
        download_progress.text("Trwa pobieranie wykładu nr " + str(filmsCounter))
        download_progress.progress(int(100 * filmsCounter / filmsNumber))
    st.text('Zakończono pobieranie za rok ' + rok)

    return film_dir, audio_dir, summary_dir, text_dir, filmsNumber






def processing(rok):
    st.write("Wybrano rok wykładów : " + rok)
    film_dir, audio_dir, summary_dir, text_dir, filmsNumber = download(rok)

    
    processing_progress = st.progress(0)
    processing_progress.text("Trwa przetwarzanie plików ...")
    filmsNumber = filmsNumber * 5
    processedCounter = 0
    filenames = os.listdir(film_dir)
    for name in filenames:
        processing_progress.text("Wydobywanie audio z pliku " + name)
        sound = AudioSegment.from_file(film_dir + "/" + name)

        processedCounter += 1
        processing_progress.progress(int(100 * processedCounter / filmsNumber))

        start_point = len(sound) / 10
        stop_point = len(sound) / 2
        useful_part = sound[start_point:stop_point]
        mp3FileName = audio_dir + "/" + pathlib.Path(name).stem + ".mp3"
        useful_part.export(mp3FileName, format="mp3")

        processedCounter += 1
        processing_progress.progress(int(100 * processedCounter / filmsNumber))

        mp3FileSize = os.path.getsize(mp3FileName)
        if mp3FileSize > 25 * 1024 * 1024:
            processing_progress.text("Kompresja pliku mp3 ...")
            print("Plik mp3 jest zbyt duży, kompresja ...")
            compress_mp3(file_path = mp3FileName, bitrate="64k")
        
        processedCounter += 1
        processing_progress.progress(int(100 * processedCounter / filmsNumber))

        mp3FileSize = os.path.getsize(mp3FileName)
        if mp3FileSize > 25 * 1024 * 1024:
            print("Plik mp3 jest zbyt duży, nawet po kompresji. ")
            print("W następnej wersji programu ten problem zostanie rozwiązany.")
            processedCounter += 2
            continue

        processing_progress.text("Transkrypcja do formatu tekstowego ...")
        with open(mp3FileName, "rb") as f:
            transcript = get_openai_client().audio.transcriptions.create(file=f,model="whisper-1")

        textFileName = text_dir + "/" + pathlib.Path(name).stem + ".txt"
        with open(textFileName, "w") as f:
            f.write(transcript.text)

        processedCounter += 1
        processing_progress.progress(int(100 * processedCounter / filmsNumber))
    
        processing_progress.text("Generowanie i zapisywanie streszczenia ...")
        summary = get_openai_client().chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Streszczaj teksty w sposób jasny i rzeczowy."},
                {"role": "user", "content": f"Podsumuj ten tekst:\n\n{transcript.text}"}
            ],
            temperature=0.5,      
        )

        # zapisywanie streszczenia
        summaryFileName = summary_dir + "/" + pathlib.Path(name).stem + ".txt"
        with open(summaryFileName, "w") as f:
                f.write(summary.choices[0].message.content)

        processedCounter += 1
        processing_progress.progress(int(100 * processedCounter / filmsNumber))
    processing_progress.text("Zakończono przetwarzanie plików.")
    processing_progress.progress(100)

with st.sidebar:
    st.subheader("Podaj rok")
    option = st.selectbox(
        "Rok wykładów", 
        ("2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"))
    
    st.write("Wybrałeś wykłady z roku ", option)

    subfolder = f"lectures{option}"
    st.button("Generuj", on_click=processing, kwargs={"rok": option})