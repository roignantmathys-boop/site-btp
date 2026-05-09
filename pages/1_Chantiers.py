import streamlit as st
import pandas as pd
import os

st.title("📁 Gestion des chantiers")

FICHIER = "chantiers.csv"

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

df = pd.read_csv(FICHIER)

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

    st.success("Chantier ajouté")

st.subheader("📋 Liste des chantiers")

st.dataframe(
    df,
    use_container_width=True
)
