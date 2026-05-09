import streamlit as st

st.set_page_config(
    page_title="Gestion BTP",
    page_icon="🏗️",
    layout="wide"
)

st.title("🏗️ Gestion Chantier BTP")

st.subheader("Bienvenue")

st.write("""
Utilisez le menu à gauche pour accéder aux modules :

- 📁 Chantiers
- ♻️ Déchets
- 📄 FDS
- 💰 Devis
- 🪝 Vérifications
- 📊 Dashboard
""")
