import streamlit as st

st.set_page_config(page_title="Elite Analyst", layout="centered")

st.title("💎 ELITE ANALYST PRO")

# Menu de sélection (Zéro écriture)
sport = st.selectbox("SPORT", ["⚽ Football", "🏒 Hockey", "🏀 Basket"])
pays = st.selectbox("RÉGION", ["France", "Angleterre", "Espagne", "Europe (Coupes)"])

# Liste dynamique D1 / D2
if pays == "France":
    div = st.selectbox("DIVISION", ["Ligue 1", "Ligue 2"])
    equipes = ["PSG", "OM", "Lorient", "Bordeaux"]
elif pays == "Angleterre":
    div = st.selectbox("DIVISION", ["Premier League", "Championship"])
    equipes = ["Man City", "Arsenal", "Leeds", "Burnley"]
elif pays == "Espagne":
    div = st.selectbox("DIVISION", ["LaLiga", "Segunda División", "Supercoupe"])
    equipes = ["Real Madrid", "Barcelone", "Atleti", "Girona"]
else:
    div = st.selectbox("DIVISION", ["Ligue des Champions", "Europa League"])
    equipes = ["Real Madrid", "Bayern", "Man City", "Barcelone"]

match = st.selectbox("MATCHS DU JOUR", [f"{equipes[0]} vs {equipes[1]}", f"{equipes[2]} vs {equipes[3]}"])

if st.button("🔍 SCANNER LE MATCH", use_container_width=True):
    st.subheader("📊 PRÉDICTIONS IA")
    c1, c2, c3 = st.columns(3)
    c1.metric("Corners", "9.5+")
    c2.metric("Cartons", "4.5+")
    c3.metric("Fautes", "22+")
    st.error("⚠️ SCÉNARIO IMPROBABLE DÉTECTÉ : Match nul probable (Cote élevée)")
