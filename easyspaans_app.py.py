import random
import streamlit as st
st.set_page_config(page_title="EasySpaans", page_icon="🇪🇸", layout="centered")

st.title("🇪🇸 EasySpaans – Werkwoordentrainer")
st.write "Train je Spaanse werkwoorden op een rustige, overzichtelijke manier."

# EASY-werkwoorden (33 stuks)
verbs = [
    "viajar", "visitar", "limpiar", "cocinar", "bailar", "cantar",
    "ayudar", "saltar", "enseñar", "explicar", "lanzar", "empujar",
    "ganar", "enviar", "tocar", "golpear", "esconder", "brillar",
    "caminar", "hablar", "estudiar", "trabajar", "llamar", "esperar",
    "terminar", "comer", "beber", "vivir", "escribir", "abrir",
    "pagar", "comprar", "tomar"
]

persons = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos"]
tenses = ["presente", "perfecto", "imperfecto", "gerundio"]

# REGELMATIGE vervoegingen generator
def conjugate(verb, person, tense):
    stem = verb[:-2]
    ending = verb[-2:]

    # Presente
    if tense == "presente":
        if ending == "ar":
            endings = {
                "yo": "o", "tú": "as", "él/ella": "a",
                "nosotros": "amos", "vosotros": "áis", "ellos": "an"
            }
        elif ending == "er":
            endings = {
                "yo": "o", "tú": "es", "él/ella": "e",
                "nosotros": "emos", "vosotros": "éis", "ellos": "en"
            }
        else:  # ir
            endings = {
                "yo": "o", "tú": "es", "él/ella": "e",
                "nosotros": "imos", "vosotros": "ís", "ellos": "en"
            }
        return f"{person} {stem}{endings[person]}"

    # Perfecto
    if tense == "perfecto":
        aux = {
            "yo": "he", "tú": "has", "él/ella": "ha",
            "nosotros": "hemos", "vosotros": "habéis", "ellos": "han"
        }
        participio = stem + ("ado" if ending == "ar" else "ido")
        return f"{person} {aux[person]} {participio}"

    # Imperfecto
    if tense == "imperfecto":
        if ending == "ar":
            endings = {
                "yo": "aba", "tú": "abas", "él/ella": "aba",
                "nosotros": "ábamos", "vosotros": "abais", "ellos": "aban"
            }
        else:
            endings = {
                "yo": "ía", "tú": "ías", "él/ella": "ía",
                "nosotros": "íamos", "vosotros": "íais", "ellos": "ían"
            }
        return f"{person} {stem}{endings[person]}"

    # Gerundio
    if tense == "gerundio":
        ger = stem + ("ando" if ending == "ar" else "iendo")
        return f"{person} {ger}"


print("=== EASY TRAINER — PILOT v3 ===")

while True:
    verb = random.choice(verbs)
    person = random.choice(persons)
    tense = random.choice(tenses)

    print("\n----------------------------------")
    print(f"Infinitief: {verb}")
    print(f"Persoon: {person}")
    print(f"Tijd: {tense}")
    print("----------------------------------")

    correct = conjugate(verb, person, tense)

    user_form = input("Typ de juiste vorm: ").strip().lower()

    if user_form == correct.lower():
        print("✔ Correct!")
    else:
        print(f"✖ Fout. Correct is: {correct}")

    input("Spreek het hardop uit en druk op Enter...")

    print("\nMaak nu een zin met deze vorm.")
    user_sentence = input("Jouw zin: ").lower()

    if correct.split()[1] in user_sentence or correct in user_sentence:
        print("✔ Zin lijkt correct!")
    else:
        print("⚠ Ik zie de vorm niet terug in je zin.")

    input("Spreek de zin hardop uit en druk op Enter...")

    input("\nDruk op Enter voor de volgende opdracht...")
