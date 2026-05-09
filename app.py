import streamlit as st

st.set_page_config(
    page_title="Gestion BTP",
    page_icon="🏗️",
    layout="wide"
)

st.title("🏗️ Gestion Chantier BTP")

st.subheader("Bienvenue")

st.write("Cliquez sur un module :")

col1, col2 = st.columns(2)

with col1:

    if st.button("📁 Chantiers", use_container_width=True):
        st.switch_page("pages/1_Chantiers.py")

with col2:

    if st.button("♻️ Registre Déchets", use_container_width=True):
        st.switch_page("pages/2_Registre_Dechets.py")

with col3:

if st.button("📊 Dashboard", use_container_width=True):
    st.switch_page("pages/3_Dashboard.py")
