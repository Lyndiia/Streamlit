import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# === Données des comptes utilisateurs ===
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,
    "cookie_name",
    "cookie_key",
    30  # Durée de session en minutes
)

authenticator.login()
def accueil():

    with st.sidebar:
        authenticator.logout("Déconnexion")
        st.write(f"Bienvenue *{st.session_state['name']}*")

        selection = option_menu(
            menu_title=None,
            options=["🏠Accueil", "📖Mes Livres Lus"],
            icons=["arrow"],
            menu_icon="list",
            default_index=0
        )

    if selection == "🏠Accueil":
        st.title("Bienvenue sur ma page 🎉")
        st.image("https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif", caption="Applaudissements 👏", use_container_width=True)
    
    elif selection == "📖Mes Livres Lus" :
        st.title("Vous retrouverez ici tous les livres que j'ai lu 📖")

        img = [
            "https://cdn.pixabay.com/photo/2018/10/04/14/22/reading-3723751_1280.jpg",  
            "https://cdn.pixabay.com/photo/2015/10/22/17/28/stack-of-books-1001655_1280.jpg",  
            "https://cdn.pixabay.com/photo/2022/03/28/18/41/spring-7098130_960_720.jpg",  
            "https://cdn.pixabay.com/photo/2018/05/10/08/59/book-3387071_1280.jpg",  
            "https://cdn.pixabay.com/photo/2017/03/17/10/29/coffee-2151200_1280.jpg"  
        ]
        images_par_page = 12

        total_images = len(img)
        num_pages = (total_images // images_par_page) + (1 if total_images % images_par_page != 0 else 0)
        page = st.number_input('Page', min_value=1, max_value=num_pages, value=1)

        # Sélectionner les images à afficher pour la page courante
        start_idx = (page - 1) * images_par_page
        end_idx = min(page * images_par_page, total_images)
        images_to_display = img[start_idx:end_idx]



        # Affichage des images par ligne de 3 images
        cols = st.columns(3)
        for i, img_url in enumerate(images_to_display):
            cols[i % 3].image(img_url, use_container_width=True)


if st.session_state["authentication_status"]:
  accueil()

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')