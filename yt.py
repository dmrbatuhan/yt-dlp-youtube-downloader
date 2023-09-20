# -*- coding: utf-8 -*-
import os
import ctypes

def set_window_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

# Yeni başlık
new_title = "yt-dlp İndirici"

# Pencere başlığını ayarla
set_window_title(new_title)



def main():
    while True:
        print("Yapmak istediğiniz işlemi seçin:")
        print("1. Tek İndirme")
        print("2. Çalma Listesi İndirme")
        print("3. Kanal İndirme")
        print("4. Stream linki alma")
        print("5. yt-dlp'yi güncelle")
        print("6. Çıkış")
        
        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            download_single_media()
        elif choice == "2":
            download_playlist()
        elif choice == "3":
            download_channel()
        elif choice == "4":
            get_stream_url()
        elif choice == "5":
            update_ytdlp()
        elif choice == "6":
            break
        else:
            input("Hatalı bir seçim yaptınız. Ana menüye dönmek için Enter tuşuna basın.")

            

def download_single_media():
    url = input("Link:\n")
    format_choice = input("1. Ses olarak indir\n2. Video olarak indir\nSeçiminizi yapın (1/2): ")

    if format_choice == "1":
        os.system(f'yt-dlp -x --audio-format mp3 -o "mp3/%(title)s.%(ext)s" {url}')
    elif format_choice == "2":
        os.system(f'yt-dlp -S "ext" -o "mp4/%(title)s.%(ext)s" {url}')
    else:
        print("Geçersiz seçenek. Tekrar deneyin.")


def download_playlist():
    url = input("Link:\n")
    format_choice = input("1. Ses olarak indir\n2. Video olarak indir\nSeçiminizi yapın (1/2): ")

    if format_choice == "1":
        os.system(f'yt-dlp -x --audio-format mp3 -o "%(playlist)s/%(title)s.%(ext)s" {url}')
    elif format_choice == "2":
        os.system(f'yt-dlp -S "ext" -o "%(playlist)s/%(title)s.%(ext)s" {url}')
    else:
        print("Geçersiz seçenek. Tekrar deneyin.")


def download_channel():
    url = input("Link:\n")
    folder_choice = input("Kanal içeriğini nasıl indirmek istersiniz?\n1. Her çalma listesi için ayrı klasörler oluşturulsun\n2. Tüm içerik tek klasörde olsun\nSeçiminizi yapın (1/2): ")
    format_choice = input("İndirilen içeriğin formatını seçin:\n1. Ses olarak indir\n2. Video olarak indir\nSeçiminizi yapın (1/2): ")

    if folder_choice == "1":
        url = f"{url}/playlists"
    
    if format_choice == "1":
        os.system(f'yt-dlp -x --audio-format mp3 -o "%(uploader)s/%(playlist)s/%(title)s.%(ext)s" {url}')
    elif format_choice == "2":
        os.system(f'yt-dlp -S "ext" -o "%(uploader)s/%(playlist)s/%(title)s.%(ext)s" {url}')
    else:
        print("Geçersiz seçenek. Tekrar deneyin.")


def get_stream_url():
    url = input("Link:\n")
    stream_url = os.popen(f'yt-dlp --get-url -f b {url}').read()
    os.system(f'echo {stream_url.strip()} | clip')
    input("Stream linki panoya kopyalandı. Ana menüye dönmek için Enter tuşuna basın.")



def update_ytdlp():
    os.system("yt-dlp -U")
    print("yt-dlp güncellendi.")
    input("Devam etmek için bir tuşa basın.")


if __name__ == "__main__":
    main()
