from pytubefix  import YouTube
from pytubefix.cli import on_progress


# 2015
urls = ['https://youtu.be/yMbpOZ9uJ-U', 'https://youtu.be/lryDr9TFa3c', 'https://youtu.be/lyv-5dd3hhU', 'https://youtu.be/YeuMI80YbvA',
        'https://youtu.be/Oujcs7qVQKg', 'https://youtu.be/_iPGJ2Yfe-U', 'https://youtu.be/WmRfNrEgOxg', 'https://youtu.be/QgB3GeFoMQc']

for url in urls:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    ys = yt.streams.get_lowest_resolution()
    ys.download(output_path="lectures2015")
print('Zakończono pobieranie za 2015')

# 2016
urls = ['https://youtu.be/2eR2n_v2hLA', 'https://youtu.be/PexDbIvDVy0', 'https://youtu.be/PeIprWcETD8', 'https://youtu.be/xFSbncszCI8',
        'https://youtu.be/fQwB-OQlwgE', 'https://youtu.be/e_GjIY2YhPc', 'https://youtu.be/mLzlF8ky3fk']

for url in urls:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    ys = yt.streams.get_lowest_resolution()
    ys.download(output_path="lectures2016")
print('Zakończono pobieranie za 2016')

# 2017
urls = ['https://youtu.be/_mK1Jryaq_Y', 'https://youtu.be/hl3sMFAuTSE', 'https://youtu.be/f6pBzjg5jiQ', 'https://youtu.be/I0tu5_BeeyI','https://youtu.be/LfZIUH8KJiA', 'https://youtu.be/S1SdE6Um5VM',
        'https://youtu.be/YMq8Diu5608', 'https://youtu.be/6r0fMl9aU-8', 'https://youtu.be/qg2H-B3sLJQ']

for url in urls:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    ys = yt.streams.get_lowest_resolution()
    ys.download(output_path="lectures2017")
print('Zakończono pobieranie za 2017')

# 2018
urls = ['https://youtu.be/MHwn2LUmiBE', 'https://youtu.be/YeLLuwYMibA', 'https://youtu.be/AuqMiJOaO5Q', 'https://youtu.be/KurhWg3X8cU',
        'https://youtu.be/UzCk2edqLbc', 'https://youtu.be/2qL51Acy-Co', 'https://youtu.be/XjXtuaIdBA8']

for url in urls:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    ys = yt.streams.get_lowest_resolution()
    ys.download(output_path="lectures2018")
print('Zakończono pobieranie za 2018')

# 2019
urls = ['https://youtu.be/7dQuOupLlF0', 'https://youtu.be/noGWUikakW8', 'https://youtu.be/jKpZrjb0gjE', 'https://youtu.be/2e3JM4_7b0Y',
        'https://youtu.be/f4OjAaeB0c8', 'https://youtu.be/xhmkPJTNt9E', 'https://youtu.be/X0PsQ4eCt5Q']

for url in urls:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    ys = yt.streams.get_lowest_resolution()
    ys.download(output_path="lectures2019")
print('Zakończono pobieranie za 2019')

# 2020
urls = ['https://youtu.be/qA6BdCuV1i8', 'https://youtu.be/w1NUzKk30GE', 'https://youtu.be/vZ3J6VnOCV4', 'https://youtu.be/KcUANfasozs']        

for url in urls:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    ys = yt.streams.get_lowest_resolution()
    ys.download(output_path="lectures2020")
print('Zakończono pobieranie za 2020')

# 2021
urls = ['https://youtu.be/r9cGfm6rzJI', 'https://youtu.be/FvAlsOFYk84', 'https://youtu.be/4yKAmwIyjPU',
        'https://youtu.be/dsf-Lqx4gRc', 'https://youtu.be/MS0x83n73Mc', 'https://youtu.be/MsVky0uTwKU']

for url in urls:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    ys = yt.streams.get_lowest_resolution()
    ys.download(output_path="lectures2021")
print('Zakończono pobieranie za 2021')

# 2022
urls = ['https://youtu.be/uqQuvMMmvic', 'https://youtu.be/DxDxKYgQG7c', 'https://youtu.be/ZxT0jNzYEko','https://youtu.be/IWNsx4Zj8f0', 'https://youtu.be/foYERTxPr5c', 'https://youtu.be/pp-Ltw7Cf2w',
        'https://youtu.be/RVi4btOi-mQ', 'https://youtu.be/w_LeTGf7VnY', 'https://youtu.be/eQpRf1nHHOY']

for url in urls:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    ys = yt.streams.get_lowest_resolution()
    ys.download(output_path="lectures2022")
print('Zakończono pobieranie za 2022')

# 2023
urls = ['https://youtu.be/Xi2g_hwAAeI', 'https://youtu.be/nqYGzezfb54', 'https://youtu.be/EYEaa4kqiI0', 'https://youtu.be/rbR4SCblF44', 'https://youtu.be/H6PhB-UcwUA', 
        'https://youtu.be/2S7cTMF9x4s', 'https://youtu.be/p9jgKRfXme8', 'https://youtu.be/67aJ79FRstc', 'https://youtu.be/RNNUdMkvgbU']

for url in urls:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    ys = yt.streams.get_lowest_resolution()
    ys.download(output_path="lectures2023")
print('Zakończono pobieranie za 2023')

# # 2024
urls = ['https://youtu.be/6R2ASA7-g-c', 'https://youtu.be/cbo9wK86hjQ', 'https://youtu.be/RgTBW77aofA', 'https://youtu.be/Y8nUI0VY7eg', 
        'https://youtu.be/BIzQE4zteg0', 'https://youtu.be/-0wlsxjazj0', 'https://youtu.be/Rj3b_WIp258', 'https://youtu.be/fLHHkGfnRPo']

for url in urls:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    ys = yt.streams.get_lowest_resolution()
    ys.download(output_path="lectures2024")
print('Zakończono pobieranie za 2024')

# # 2025
urls = ['https://youtu.be/9Iwav_9Vqtc', 'https://youtu.be/6CUWGxUPwxY', 'https://youtu.be/fTcFsZ8p55g']

for url in urls:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    ys = yt.streams.get_lowest_resolution()
    ys.download(output_path="lectures2025")
print('Zakończono pobieranie za 2025')
print(" K O N I E C ")