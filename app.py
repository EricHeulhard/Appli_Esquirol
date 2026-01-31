import streamlit as st
from indice_in_text import mots_,indices_
st.set_page_config(
    page_title="La maison Esquiol",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 La maison Esquirol ")

# CSS pour le fond
page_bg_img = '''
<style>
body {
background-image: url("https://fr.wikipedia.org/wiki/Rue_Esquirol#/media/Fichier:F4457_Paris_XIII_rue_Esquirol.jpg");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
}
</style>
'''

st.write("Bienvenue sur l'application de la maison Esquiol.")

st.write("Vous allez devoir résoudre quelques énigmes et faire quelques jeux"
         " afin de pouvoir manger le gateau")

st.write("Les indices ne se trouve que dans le salon")

# --- Définir les indices et mots attendus ---
quiz_steps = [
    (indices_[0], mots_[0]),
    (indices_[1], mots_[1]),
    (indices_[2], mots_[2]),
    (indices_[3], mots_[3]),
    (indices_[4], mots_[4])
]

# --- Initialisation de l'état ---
if "current_step" not in st.session_state:
    st.session_state.current_step = 0
if "completed" not in st.session_state:
    st.session_state.completed = False
if "answers" not in st.session_state:
    st.session_state.answers = [""] * len(quiz_steps)  # mots saisis

# --- Fonction pour valider le mot ---
def submit_answer():
    step = st.session_state.current_step
    user_input = st.session_state["input_current"].strip().lower()
    expected = quiz_steps[step][1].lower()
    if user_input == expected:
        st.session_state.answers[step] = quiz_steps[step][1]  # garder le mot
        st.session_state.current_step += 1
        if st.session_state.current_step >= len(quiz_steps):
            st.session_state.completed = True
        st.success("Correct !")
    else:
        st.error("Ce n'est pas le bon mot. Réessayez.")

# --- Affichage des étapes ---
for i, (indice, mot) in enumerate(quiz_steps):
    with st.container():
        st.subheader(indice)
        if i < st.session_state.current_step:
            # Étape déjà validée
            st.success(f"Mot trouvé : {st.session_state.answers[i]}")
        elif i == st.session_state.current_step and not st.session_state.completed:
            # Étape actuelle : seul input actif
            st.text_input("Mot attendu :", key="input_current")
            st.button("Submit", on_click=submit_answer)


audio_file_path_la = "assets/316903__jaz_the_man_2__la-stretched.wav"  # ton fichier mp3 dans le même dossier que le script
audio_file_path_do = "assets/316899__jaz_the_man_2__do-stretched.wav"
audio_file_path_mi = "assets/316907__jaz_the_man_2__mi-stretched.wav"
# Créer un bouton
st.subheader('Je suis sur la guitare')
if st.button("Ecoutez moi", key = "do_buton"):
    # Lire le fichier audio
    with open(audio_file_path_do, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/wav")


st.subheader('G')
if st.button("---", key = "la_buton_1"):
    # Lire le fichier audio
    with open(audio_file_path_la, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/wav")
st.subheader('T')
if st.button("---", key = "mi_buton"):
    # Lire le fichier audio
    with open(audio_file_path_la, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/wav")
if st.button("---", key = "la_buton_2"):
    # Lire le fichier audio
    with open(audio_file_path_mi, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/wav")
st.subheader('U')

# --- Félicitations à la fin ---
if st.session_state.completed:
    st.balloons()
    st.success("🎉 Félicitations ! On peut manger le gateau !!!!")