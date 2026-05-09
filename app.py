import streamlit as st

st.set_page_config(
    page_title="Gestion BTP",
    page_icon="🏗️",
    layout="wide"
)

st.title("🏗️ Gestion Chantier BTP")
st.subheader("Bienvenue")

st.write("Cliquez sur un module pour l’ouvrir :")

col1, col2 = st.columns(2)

with col1:
    if st.button("📁 Chantiers", use_container_width=True):
        st.switch_page("pages/1_📁_Chantiers.py")

with col2:
    if st.button("♻️ Registre Déchets", use_container_width=True):
        st.switch_page("pages/2_♻️_Registre_Déchets.py")

st.divider()

st.info("Les autres modules seront ajoutés ensuite : FDS, Devis, Vérifications, Dashboard.")
