import subprocess
import time

url = "https://www.youtube.com/watch?v=2FspwOKfGPY"
max_time = 5  
liczba_testow = 3
save_path = "./test_out/%(title)s.%(ext)s"

def bestvideo_test():
    start = time.time()
    try:
        subprocess.run(["youtube-dl", url, "-o", save_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode())
        assert False
    end = time.time()
    dl_time = end - start
    print("Czas pobierania: " + str(dl_time) + " sekund")
    return dl_time

def worstvideo_test():
    start = time.time()
    try:
        subprocess.run(["youtube-dl", url, "-f", "worstvideo", "-o", save_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode())
        assert False
    end = time.time()
    dl_time = end - start
    print("Czas pobierania (MP4): " + str(dl_time) + " sekund")
    return dl_time

def testy_bestvideo():
    sum = 0
    for i in range(liczba_testow):
        print("Test Best Video " + str(i))
        sum += bestvideo_test()
    avg = sum / liczba_testow
    print("Sredni czas pobierania (Best Video): " + str(avg) + " sekund")
    assert avg < max_time, "Za dlugi czas pobierania Best Video: " + str(avg) + " sekund"

def testy_worstvideo():
    sum = 0
    for i in range(liczba_testow):
        print("Test Worst Video " + str(i))
        sum += worstvideo_test()
    avg = sum / liczba_testow
    print("Sredni czas pobierania (Worst Video): " + str(avg) + " sekund")
    assert avg < max_time, "Za dlugi czas pobierania Worst Video: " + str(avg) + " sekund"


testy_bestvideo()
testy_worstvideo()