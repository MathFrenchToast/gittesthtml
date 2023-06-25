import yt_dlp as youtube_dl
from moviepy.editor import VideoFileClip

def download_and_cut_video(url, output_path, duration):
    ydl_opts = {
        'outtmpl': output_path + '/%(title)s.%(ext)s',
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', None)
            video_filename = output_path + '/' + video_title + '.mp4'
            ydl.download([url])
            print("Téléchargement terminé !")
            
            cut_video_into_parts(video_filename, duration)
    except Exception as e:
        print("Une erreur s'est produite lors du téléchargement de la vidéo :", str(e))

def cut_video_into_parts(input_file, duration):
    video = VideoFileClip(input_file)
    output_file = input_file[:-4] + "_part"

    start_time = 0
    end_time = duration
    
    part_number = 1
    while end_time <= video.duration:
        output = output_file + f"_{part_number}.mp4"
        video.subclip(start_time, end_time).write_videofile(output, codec="libx264")
        start_time = end_time
        end_time += duration
        part_number += 1
    
    output = output_file + f"_{part_number}.mp4"
    video.subclip(start_time, video.duration).write_videofile(output, codec="libx264")

video_url = input("Veuillez entrer l'URL de la vidéo YouTube à télécharger : ")

output_path = input("Veuillez entrer le chemin de destination pour le téléchargement : ")

duration = 61
 
download_and_cut_video(video_url, output_path, duration)
