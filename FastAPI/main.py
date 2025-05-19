from fastapi import FastAPI, Query
import random

app = FastAPI()

# Base de frases en dos idiomas
frases = {
    "es": [
        "Confía en el plan divino, todo está en su lugar perfecto.",
        "Tu luz interior es más fuerte que cualquier sombra.",
        "Eres guiada y protegida en cada paso que das.",
        "El amor infinito siempre está a tu alrededor.",
        "Cada instante es una oportunidad para renacer.",
        "La gratitud abre las puertas de la abundancia.",
        "Todo lo que buscas ya está dentro de ti.",
        "La vida te sostiene con amor y propósito.",
        "Eres parte del universo, y el universo es parte de ti.",
        "Suelta el miedo y abraza la certeza de que todo es perfecto."
    ],
    "en": [
        "Trust the divine plan, everything is in its perfect place.",
        "Your inner light is stronger than any shadow.",
        "You are guided and protected in every step you take.",
        "Infinite love is always around you.",
        "Every moment is an opportunity to be reborn.",
        "Gratitude opens the doors to abundance.",
        "Everything you seek is already within you.",
        "Life supports you with love and purpose.",
        "You are part of the universe, and the universe is part of you.",
        "Let go of fear and embrace the certainty that everything is perfect."
    ]
}

@app.get("/frase")
def obtener_frase(lang: str = Query("es", description="Elige 'es' para español/ choose 'en' for English")):
    if lang not in frases:
        return {"error": "Idioma no soportado. Usa 'es' o 'en'./Not supported language, please select 'es' or 'en'."}
    return {"mensaje": random.choice(frases[lang])}
