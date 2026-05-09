import streamlit as st

st.set_page_config(
    page_title="Gestion BTP",
    page_icon="🏗️",
    layout="wide"
)

st.title("🏗️ Gestion Chantier BTP")

profil = st.selectbox(
    "Choisir votre profil",
    ["Conducteur de travaux", "Chef de chantier", "Administratif", "Direction"]
)

st.write("Profil sélectionné :", profil)

st.subheader("Menu principal")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📁 Chantiers"):
        st.success("Module Chantiers")

with col2:
    if st.button("♻️ Registre déchets"):
        st.success("Module Registre déchets")

with col3:
    if st.button("📄 FDS Produits"):
        st.success("Module FDS")

col4, col5 = st.columns(2)

with col4:
    if st.button("💰 Devis / Commandes"):
        st.success("Module Devis / Commandes")

with col5:
    if st.button("🪝 Vérifications matériel"):
        st.success("Module Vérifications")
