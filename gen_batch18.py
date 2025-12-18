import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("heedless", "Advanced", "adjective", "showing lack of care"),
    ("hegemony", "Expert", "noun", "leadership or dominance"),
    ("heinous", "Advanced", "adjective", "utterly odious"),
    ("herald", "Advanced", "verb", "to be sign of"),
    ("heresy", "Advanced", "noun", "belief contrary to doctrine"),
    ("heretic", "Advanced", "noun", "person believing in heresy"),
    ("hermetic", "Expert", "adjective", "insulated or protected"),
    ("heterodox", "Expert", "adjective", "not conforming to standard"),
    ("heterogeneous", "Advanced", "adjective", "diverse in character"),
    ("hew", "Expert", "verb", "to chop with axe"),
    ("hiatus", "Advanced", "noun", "pause or gap"),
    ("hidebound", "Expert", "adjective", "unwilling to change"),
    ("hideous", "Advanced", "adjective", "ugly or disgusting"),
    ("hierarchy", "Advanced", "noun", "system of ranking"),
    ("highlight", "Advanced", "verb", "to draw attention to"),
    ("hilarious", "Advanced", "adjective", "extremely amusing"),
    ("hinder", "Advanced", "verb", "to create difficulties for"),
    ("hindrance", "Advanced", "noun", "thing that provides resistance"),
    ("hindsight", "Advanced", "noun", "understanding after event"),
    ("hinge", "Advanced", "verb", "to depend entirely on"),
    ("histrionic", "Expert", "adjective", "overly theatrical"),
    ("hoard", "Advanced", "verb", "to amass and hide"),
    ("hoary", "Expert", "adjective", "grayish white"),
    ("hoax", "Advanced", "noun", "humorous or malicious deception"),
    ("hodgepodge", "Advanced", "noun", "confused mixture"),
    ("hollow", "Advanced", "adjective", "having empty space inside"),
    ("homage", "Advanced", "noun", "special honor or respect"),
    ("homogeneous", "Advanced", "adjective", "of same kind"),
    ("hone", "Advanced", "verb", "to sharpen blade"),
    ("honesty", "Advanced", "noun", "quality of being free from deceit"),
    ("hoodwink", "Advanced", "verb", "to deceive or trick"),
    ("horizontal", "Advanced", "adjective", "parallel to horizon"),
    ("horrific", "Advanced", "adjective", "causing horror"),
    ("hospitable", "Advanced", "adjective", "friendly to strangers"),
    ("hostile", "Advanced", "adjective", "unfriendly and antagonistic"),
    ("hover", "Advanced", "verb", "to remain in one place"),
    ("hubris", "Advanced", "noun", "excessive pride"),
    ("hue", "Advanced", "noun", "color or shade"),
    ("humane", "Advanced", "adjective", "having compassion"),
    ("humble", "Advanced", "adjective", "having modest estimate"),
    ("humdrum", "Advanced", "adjective", "lacking excitement"),
    ("humiliate", "Advanced", "verb", "to make feel ashamed"),
    ("humility", "Advanced", "noun", "modest view of importance"),
    ("humor", "Advanced", "verb", "to comply with wishes"),
    ("hurdle", "Advanced", "noun", "obstacle or difficulty"),
    ("husband", "Advanced", "verb", "to use resources economically"),
    ("husbandry", "Expert", "noun", "management of resources"),
    ("hybrid", "Advanced", "noun", "thing made by combining"),
    ("hyperbole", "Advanced", "noun", "exaggerated statements"),
    ("hypercritical", "Advanced", "adjective", "excessively critical"),
    ("hypocritical", "Advanced", "adjective", "behaving contrary to stated beliefs"),
    ("hypothetical", "Advanced", "adjective", "based on possible situation"),
    ("iconoclast", "Advanced", "noun", "person who attacks beliefs"),
    ("iconoclastic", "Advanced", "adjective", "characterized by attack on beliefs"),
    ("ideology", "Advanced", "noun", "system of ideas"),
    ("idiom", "Advanced", "noun", "group of words with meaning"),
    ("idiosyncrasy", "Advanced", "noun", "mode of behavior peculiar to individual"),
    ("idiosyncratic", "Advanced", "adjective", "relating to idiosyncrasy"),
    ("idle", "Advanced", "adjective", "avoiding work"),
    ("idolize", "Advanced", "verb", "to admire excessively"),
    ("ignoble", "Advanced", "adjective", "not honorable"),
    ("ignominy", "Expert", "noun", "public shame"),
    ("ignorant", "Advanced", "adjective", "lacking knowledge"),
    ("illicit", "Advanced", "adjective", "forbidden by law"),
    ("illuminate", "Advanced", "verb", "to light up"),
    ("illusion", "Advanced", "noun", "false idea or belief"),
    ("illusory", "Advanced", "adjective", "based on illusion"),
    ("illustrate", "Advanced", "verb", "to explain by examples"),
    ("illustrious", "Advanced", "adjective", "well known and esteemed"),
    ("imbibe", "Expert", "verb", "to drink alcohol"),
    ("imbroglio", "Expert", "noun", "extremely confused situation"),
    ("imbue", "Advanced", "verb", "to inspire with feeling"),
    ("immaculate", "Advanced", "adjective", "perfectly clean"),
    ("immaterial", "Advanced", "adjective", "unimportant under circumstances"),
    ("immature", "Advanced", "adjective", "not fully developed"),
    ("immemorial", "Expert", "adjective", "originating in distant past"),
    ("immense", "Advanced", "adjective", "extremely large"),
    ("immerse", "Advanced", "verb", "to dip or submerge"),
    ("imminent", "Advanced", "adjective", "about to happen"),
    ("immobile", "Advanced", "adjective", "not moving"),
    ("immoderate", "Advanced", "adjective", "not sensible"),
    ("immolate", "Expert", "verb", "to kill as sacrifice"),
    ("immortal", "Advanced", "adjective", "living forever"),
    ("immune", "Advanced", "adjective", "resistant to disease"),
    ("immure", "Expert", "verb", "to enclose within walls"),
    ("immutable", "Advanced", "adjective", "unchanging over time"),
    ("impair", "Advanced", "verb", "to weaken or damage"),
    ("impale", "Advanced", "verb", "to transfix with sharp instrument"),
    ("impart", "Advanced", "verb", "to make information known"),
    ("impartial", "Advanced", "adjective", "treating all rivals equally"),
    ("impasse", "Advanced", "noun", "situation with no progress"),
    ("impassioned", "Advanced", "adjective", "filled with passion"),
    ("impassive", "Advanced", "adjective", "not feeling emotion"),
    ("impeach", "Advanced", "verb", "to charge with misconduct"),
    ("impeccable", "Advanced", "adjective", "faultless in conforming to standard"),
    ("impecunious", "Expert", "adjective", "having little money"),
    ("impede", "Advanced", "verb", "to delay or prevent"),
    ("impediment", "Advanced", "noun", "hindrance or obstruction"),
    ("impel", "Advanced", "verb", "to drive or urge forward"),
    ("impending", "Advanced", "adjective", "about to happen"),
]

def translate(text, target_lang):
    url = f"https://translation.googleapis.com/language/translate/v2?key={API_KEY}"
    data = {"q": text, "target": target_lang, "source": "en"}
    try:
        r = requests.post(url, data=data, timeout=10)
        return r.json()["data"]["translations"][0]["translatedText"]
    except:
        return text

def generate_words():
    words = []
    start_id = 1501
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"{i+1}/{len(GRE_WORDS)}: {word}")
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"The {word} character of the decision was notable.",
            "category": "General",
            "translations": {
                "ko": translate(definition, "ko"),
                "zh": translate(definition, "zh-CN"),
                "hi": translate(definition, "hi")
            }
        }
        words.append(word_data)
        time.sleep(0.05)
    return words

if __name__ == "__main__":
    words = generate_words()
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch18.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
