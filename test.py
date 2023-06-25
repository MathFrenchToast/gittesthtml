import requests

# Informations d'identification de compte TikTok
username = "youtubevid.ontiktok"
password = "JrF6RcEbdNdMBKf&"

def upload_video_to_tiktok(video_path):
    # URL de l'endpoint d'upload de TikTok
    upload_url = "https://www.tiktok.com/api/upload/video"

    # Lecture du fichier vidéo en mode binaire
    with open(video_path, "rb") as file:
        video_data = file.read()

    # Paramètres de la requête d'upload
    params = {
        "username": username,
        "password": password,
        # Autres paramètres facultatifs comme le titre, la description, les hashtags, etc.
    }

    # En-têtes de la requête
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.tiktok.com/upload/",
    }

    # En-têtes de la requête d'upload
    upload_headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.tiktok.com/upload/",
        "Content-Type": "multipart/form-data",
    }

    # Envoi de la requête d'upload
    response = requests.post(upload_url, params=params, headers=upload_headers, files={"video": video_data})

    # Vérification de la réponse
    if response.status_code == 200:
        print("Vidéo téléchargée sur TikTok avec succès.")
    else:
        print("Erreur lors du téléchargement de la vidéo sur TikTok.")

# Chemin de la vidéo à uploader
video_path = "C:\Users\galaa\OneDrive\Documents\vidéotest\Atoms As Big As Mountains — Neutron Stars Explained_part_1.mp4"

# Appel de la fonction pour uploader la vidéo sur TikTok
upload_video_to_tiktok(video_path)
