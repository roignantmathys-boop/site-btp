import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Gestion BTP",
    page_icon="🏗️",
    layout="wide"
)

# -----------------------------
# TITRE
# -----------------------------

st.title("🏗️ Gestion Chantier BTP")

profil = st.selectbox(
    "Choisir votre profil",
    [
        "Conducteur de travaux",
        "Chef de chantier",
        "Administratif",
        "Direction"
    ]
)

st.write("Profil sélectionné :", profil)

st.divider()

# -----------------------------
# AJOUT CHANTIER
# -----------------------------

st.header("📁 Gestion des chantiers")

with st.form("form_chantier"):

    nom = st.text_input("Nom du chantier")

    responsable = st.text_input("Responsable chantier")

    ville = st.text_input("Ville")

    avancement = st.slider(
        "Avancement (%)",
        0,
        100,
        0
    )

    statut = st.selectbox(
        "Statut",
        [
            "Préparation",
            "En cours",
            "Terminé",
            "Suspendu"
        ]
    )

    bouton = st.form_submit_button("Ajouter le chantier")

# -----------------------------
# BASE DE DONNÉES TEMPORAIRE
# -----------------------------

if "chantiers" not in st.session_state:
    st.session_state.chantiers = []

# -----------------------------
# AJOUT DANS LE TABLEAU
# -----------------------------

if bouton:

    nouveau = {
        "Nom": nom,
        "Responsable": responsable,
        "Ville": ville,
        "Avancement": f"{avancement} %",
        "Statut": statut
    }

    st.session_state.chantiers.append(nouveau)

    st.success("Chantier ajouté avec succès")

# -----------------------------
# AFFICHAGE TABLEAU
# -----------------------------

st.subheader("📋 Liste des chantiers")

if len(st.session_state.chantiers) > 0:

    df = pd.DataFrame(st.session_state.chantiers)

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.info("Aucun chantier enregistré")
