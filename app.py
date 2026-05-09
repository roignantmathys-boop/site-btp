import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Gestion BTP",
    page_icon="🏗️",
    layout="wide"
)

# -----------------------------
# FICHIER CSV
# -----------------------------

FICHIER = "chantiers.csv"

# -----------------------------
# CRÉATION FICHIER SI ABSENT
# -----------------------------

if not os.path.exists(FICHIER):

    df_vide = pd.DataFrame(
        columns=[
            "Nom",
            "Responsable",
            "Ville",
            "Avancement",
            "Statut"
        ]
    )

    df_vide.to_csv(FICHIER, index=False)

# -----------------------------
# LECTURE DU CSV
# -----------------------------

df = pd.read_csv(FICHIER)

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
# FORMULAIRE
# -----------------------------

st.header("📁 Gestion des chantiers")

with st.form("formulaire"):

    nom = st.text_input("Nom du chantier")

    responsable = st.text_input("Responsable")

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

    ajouter = st.form_submit_button("Ajouter chantier")

# -----------------------------
# AJOUT CHANTIER
# -----------------------------

if ajouter:

    nouvelle_ligne = pd.DataFrame([{
        "Nom": nom,
        "Responsable": responsable,
        "Ville": ville,
        "Avancement": f"{avancement} %",
        "Statut": statut
    }])

    df = pd.concat(
        [df, nouvelle_ligne],
        ignore_index=True
    )

    df.to_csv(FICHIER, index=False)

    st.success("Chantier enregistré")

# -----------------------------
# AFFICHAGE
# -----------------------------

st.subheader("📋 Liste des chantiers")

st.dataframe(
    df,
    use_container_width=True
)

# -----------------------------
# TÉLÉCHARGEMENT CSV
# -----------------------------

with open(FICHIER, "rb") as fichier:

    st.download_button(
        "⬇️ Télécharger la liste",
        fichier,
        file_name="chantiers.csv"
    )
