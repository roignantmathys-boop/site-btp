import streamlit as st
import pandas as pd
import os

st.title("📊 Dashboard BTP")

# -----------------------------
# LECTURE CHANTIERS
# -----------------------------

if os.path.exists("chantiers.csv"):
    df_chantiers = pd.read_csv("chantiers.csv")
else:
    df_chantiers = pd.DataFrame()

# -----------------------------
# LECTURE DECHETS
# -----------------------------

if os.path.exists("dechets.csv"):
    df_dechets = pd.read_csv("dechets.csv")
else:
    df_dechets = pd.DataFrame()

# -----------------------------
# KPIs
# -----------------------------

nb_chantiers = len(df_chantiers)

nb_bsd = len(df_dechets)

if not df_dechets.empty:
    tonnage_total = df_dechets["Quantité"].sum()
else:
    tonnage_total = 0

# -----------------------------
# AFFICHAGE KPI
# -----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📁 Chantiers",
        nb_chantiers
    )

with col2:
    st.metric(
        "♻️ BSD enregistrés",
        nb_bsd
    )

with col3:
    st.metric(
        "🚛 Quantité totale",
        f"{tonnage_total} T"
    )

st.divider()

# -----------------------------
# GRAPHIQUE DECHETS
# -----------------------------

if not df_dechets.empty:

    st.subheader("📊 Répartition des déchets")

    repartition = (
        df_dechets.groupby("Type déchet")
        ["Quantité"]
        .sum()
    )

    st.bar_chart(repartition)

else:

    st.info("Aucune donnée déchets")
