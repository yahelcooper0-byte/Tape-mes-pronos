import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Elite Analyst Pro", layout="centered")

# 6d7a5631b9668010c9842a343394cf1f
API_KEY = "6d7a5631b9668010c9842a343394cf1f" 
HEADERS = {'x-rapidapi-key': API_KEY, 'x-rapidapi-host': 'v3.football.api-sports.io'}

st.title("💎 ELITE ANALYST PRO")

# Menu de sélection
zone = st.selectbox("🌍 ZONE", ["France", "Angleterre", "Espagne", "Allemagne", "Italie", "Afrique"])
compets = {
    "France": {"Ligue 1": 61, "Ligue 2": 62},
    "Angleterre": {"Premier League": 39, "Championship": 40},
    "Espagne": {"LaLiga": 140},
    "Allemagne": {"Bundesliga": 78},
    "Italie": {"Serie A": 135},
    "Afrique": {"CAN": 1}
}
tournoi = st.selectbox("🏆 TOURNOI", list(compets[zone].keys()))
date_match = st.date_input("📅 DATE", datetime.now())

# Logique de sélection d'équipes
id_ligue = compets[zone][tournoi]
date_str = date_match.strftime('%Y-%m-%d')
url = f"https://v3.football.api-sports.io/fixtures?league={id_ligue}&season=2025&date={date_str}"

try:
    res = requests.get(url, headers=HEADERS).json()
    matchs = res.get('response', [])
    
    if matchs:
        # Tu peux enfin CHOISIR ton match ici
        options = {f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}": m for m in matchs}
        choix = st.selectbox("⚽ CHOISIS TON MATCH :", list(options.keys()))
        
        if st.button("🚀 ANALYSER CE MATCH"):
            st.success(f"Analyse en cours pour {choix}...")
            # Ici l'IA affiche les scores ou les prédictions
    else:
        st.warning("Aucun match trouvé à cette date. Change de jour ou de tournoi.")

except Exception:
    st.error("Vérifie ta connexion ou ta clé API.")
