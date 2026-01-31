import streamlit as st

st.set_page_config(
    page_title="La maison Esquiol",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 La maison Esquirol ")
st.write("Bienvenue sur l'application de la maison Esquiol.")

st.write("Vous allez devoir résoudre quelques énigmes afin de pouvoir manger le gateau")

st.write("Les indices ne se trouve que dans le salon")

# --- Définir les indices et mots attendus ---
quiz_steps = [
    ("Indice 1", "maison"),
    ("Indice 2", "esquirol"),
    ("Indice 3", "ville"),   # tu peux ajouter d'autres étapes ici
    ("Indice 4", "histoire")
]

# --- Initialisation de l'état ---
if "current_step" not in st.session_state:
    st.session_state.current_step = 0
if "completed" not in st.session_state:
    st.session_state.completed = False

# --- Fonction pour valider le mot ---
def submit_answer():
    user_input = st.session_state[f"input_{st.session_state.current_step}"].strip().lower()
    expected = quiz_steps[st.session_state.current_step][1].lower()
    if user_input == expected:
        st.session_state.current_step += 1
        if st.session_state.current_step >= len(quiz_steps):
            st.session_state.completed = True
        st.success("Correct !")
    else:
        st.error("Ce n'est pas le bon mot. Réessayez.")

# --- Affichage de l'étape actuelle ---
if not st.session_state.completed:
    step = st.session_state.current_step
    st.subheader(quiz_steps[step][0])
    st.text_input("Mot attendu :", key=f"input_{step}", on_change=submit_answer)
    st.button("Submit", on_click=submit_answer, key=f"button_{step}")
else:
    st.balloons()
    st.success("🎉 Félicitations ! Vous avez terminé le quiz.")