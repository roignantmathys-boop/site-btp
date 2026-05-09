import streamlit as st
import pandas as pd
import os

st.title("♻️ Registre Déchets")

FICHIER = "dechets.csv"

# -----------------------------
# CREATION FICHIER
# -----------------------------

if not os.path.exists(FICHIER):

    df_vide = pd.DataFrame(
        columns=[
            "Date",
            "Chantier",
            "Type déchet",
            "Quantité",
            "Transporteur",
            "Installation",
            "BSD"
        ]
    )

    df_vide.to_csv(FICHIER, index=False)

# -----------------------------
# LECTURE CSV
# -----------------------------

df = pd.read_csv(FICHIER)

# -----------------------------
# FORMULAIRE
# -----------------------------

with st.form("formulaire_dechets"):

    date = st.date_input("Date")

    chantier = st.text_input("Chantier")

    type_dechet = st.selectbox(
        "Type de déchet",
        [
            "Gravats",
            "Bois",
            "Métaux",
            "Plastique",
            "Carton",
            "DIB",
            "Amiante"
        ]
    )

    quantite = st.number_input(
        "Quantité",
        min_value=0.0,
        step=0.1
    )

    transporteur = st.text_input("Transporteur")

    installation = st.text_input("Installation destinataire")

    bsd = st.text_input("Numéro BSD")

    ajouter = st.form_submit_button("Ajouter BSD")

# -----------------------------
# AJOUT
# -----------------------------

if ajouter:

    nouvelle_ligne = pd.DataFrame([{
        "Date": date,
        "Chantier": chantier,
        "Type déchet": type_dechet,
        "Quantité": quantite,
        "Transporteur": transporteur,
        "Installation": installation,
        "BSD": bsd
    }])

    df = pd.concat(
        [df, nouvelle_ligne],
        ignore_index=True
    )

    df.to_csv(FICHIER, index=False)

    st.success("BSD enregistré")

# -----------------------------
# TABLEAU
# -----------------------------

st.subheader("📋 Historique des déchets")

st.dataframe(
    df,
    use_container_width=True
)

# -----------------------------
# TELECHARGEMENT
# -----------------------------

with open(FICHIER, "rb") as fichier:

    st.download_button(
        "⬇️ Télécharger registre déchets",
        fichier,
        file_name="registre_dechets.csv"
    )
