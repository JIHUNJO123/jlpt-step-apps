import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("entail", "Advanced", "verb", "to involve as necessary consequence"),
    ("entangle", "Advanced", "verb", "to cause to become twisted"),
    ("enterprise", "Advanced", "noun", "project or undertaking"),
    ("enthrall", "Advanced", "verb", "to capture fascinated attention"),
    ("enthuse", "Advanced", "verb", "to express eager enjoyment"),
    ("entice", "Advanced", "verb", "to attract by offering pleasure"),
    ("entity", "Advanced", "noun", "thing with distinct existence"),
    ("entrance", "Advanced", "verb", "to fill with wonder"),
    ("entreat", "Advanced", "verb", "to ask earnestly"),
    ("entrepreneur", "Advanced", "noun", "person who sets up business"),
    ("enumerate", "Advanced", "verb", "to mention one by one"),
    ("enunciate", "Advanced", "verb", "to say or pronounce clearly"),
    ("envision", "Advanced", "verb", "to imagine as future possibility"),
    ("ephemeral", "Advanced", "adjective", "lasting for very short time"),
    ("epic", "Advanced", "adjective", "heroic or grand in scale"),
    ("epicure", "Expert", "noun", "person who enjoys fine food"),
    ("epigram", "Expert", "noun", "pithy saying"),
    ("epilogue", "Advanced", "noun", "section at end of book"),
    ("epitome", "Advanced", "noun", "perfect example of quality"),
    ("equable", "Expert", "adjective", "calm and even-tempered"),
    ("equanimity", "Advanced", "noun", "mental calmness"),
    ("equate", "Advanced", "verb", "to consider one thing as equal"),
    ("equilibrium", "Advanced", "noun", "state of physical balance"),
    ("equitable", "Advanced", "adjective", "fair and impartial"),
    ("equivocal", "Advanced", "adjective", "open to more than one interpretation"),
    ("equivocate", "Advanced", "verb", "to use ambiguous language"),
    ("eradicate", "Advanced", "verb", "to destroy completely"),
    ("erode", "Advanced", "verb", "to gradually destroy"),
    ("errant", "Expert", "adjective", "erring or straying"),
    ("erratic", "Advanced", "adjective", "not even or regular"),
    ("erroneous", "Advanced", "adjective", "wrong or incorrect"),
    ("erudite", "Advanced", "adjective", "having great knowledge"),
    ("escalate", "Advanced", "verb", "to increase rapidly"),
    ("eschew", "Advanced", "verb", "to deliberately avoid"),
    ("esoteric", "Advanced", "adjective", "intended for small group"),
    ("espouse", "Advanced", "verb", "to adopt or support"),
    ("essence", "Advanced", "noun", "intrinsic nature of something"),
    ("essential", "Advanced", "adjective", "absolutely necessary"),
    ("esteem", "Advanced", "noun", "respect and admiration"),
    ("estrange", "Advanced", "verb", "to cause to feel alienated"),
    ("ethereal", "Advanced", "adjective", "extremely delicate"),
    ("ethical", "Advanced", "adjective", "relating to moral principles"),
    ("ethos", "Advanced", "noun", "characteristic spirit of culture"),
    ("eulogize", "Advanced", "verb", "to praise highly"),
    ("euphemism", "Advanced", "noun", "mild expression for unpleasant thing"),
    ("euphoria", "Advanced", "noun", "feeling of intense happiness"),
    ("evanescent", "Expert", "adjective", "soon passing out of sight"),
    ("evasive", "Advanced", "adjective", "tending to avoid commitment"),
    ("eventual", "Advanced", "adjective", "occurring at end of period"),
    ("evict", "Advanced", "verb", "to expel from property"),
    ("evince", "Expert", "verb", "to reveal presence of"),
    ("evoke", "Advanced", "verb", "to bring to mind"),
    ("exacerbate", "Advanced", "verb", "to make worse"),
    ("exact", "Advanced", "verb", "to demand and obtain"),
    ("exacting", "Advanced", "adjective", "making great demands"),
    ("exaggerate", "Advanced", "verb", "to represent as greater"),
    ("exalt", "Advanced", "verb", "to hold in high regard"),
    ("exasperate", "Advanced", "verb", "to irritate intensely"),
    ("excavate", "Advanced", "verb", "to make hollow by digging"),
    ("exceed", "Advanced", "verb", "to be greater than"),
    ("exceptional", "Advanced", "adjective", "unusual or outstanding"),
    ("excerpt", "Advanced", "noun", "short extract from film"),
    ("excessive", "Advanced", "adjective", "more than necessary"),
    ("excise", "Advanced", "verb", "to cut out surgically"),
    ("exclaim", "Advanced", "verb", "to cry out suddenly"),
    ("exclude", "Advanced", "verb", "to deny access to"),
    ("excoriate", "Expert", "verb", "to criticize severely"),
    ("exculpate", "Expert", "verb", "to show not guilty"),
    ("excursion", "Advanced", "noun", "short journey"),
    ("execrable", "Expert", "adjective", "extremely bad"),
    ("execute", "Advanced", "verb", "to carry out plan"),
    ("exemplary", "Advanced", "adjective", "serving as desirable model"),
    ("exemplify", "Advanced", "verb", "to be typical example"),
    ("exempt", "Advanced", "adjective", "free from obligation"),
    ("exert", "Advanced", "verb", "to apply or bring to bear"),
    ("exhaust", "Advanced", "verb", "to drain of resources"),
    ("exhaustive", "Advanced", "adjective", "examining all possibilities"),
    ("exhibit", "Advanced", "verb", "to publicly display"),
    ("exhilarate", "Advanced", "verb", "to make feel very happy"),
    ("exhort", "Advanced", "verb", "to strongly encourage"),
    ("exigent", "Expert", "adjective", "pressing or demanding"),
    ("exile", "Advanced", "noun", "state of being barred from country"),
    ("exonerate", "Advanced", "verb", "to absolve from blame"),
    ("exorbitant", "Advanced", "adjective", "unreasonably high"),
    ("exotic", "Advanced", "adjective", "originating in distant country"),
    ("expand", "Advanced", "verb", "to become larger"),
    ("expatiate", "Expert", "verb", "to speak or write at length"),
    ("expatriate", "Advanced", "noun", "person living abroad"),
    ("expedient", "Advanced", "adjective", "convenient and practical"),
    ("expedite", "Advanced", "verb", "to make action happen sooner"),
    ("expel", "Advanced", "verb", "to deprive of membership"),
    ("expertise", "Advanced", "noun", "expert skill or knowledge"),
    ("expiate", "Expert", "verb", "to atone for guilt"),
    ("explicit", "Advanced", "adjective", "stated clearly"),
    ("exploit", "Advanced", "verb", "to make full use of"),
    ("exponential", "Advanced", "adjective", "increasing rapidly"),
    ("expound", "Advanced", "verb", "to present and explain theory"),
    ("expropriate", "Expert", "verb", "to take away from owner"),
    ("expunge", "Advanced", "verb", "to erase or remove completely"),
    ("expurgate", "Expert", "verb", "to remove objectionable matter"),
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
    start_id = 1101
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"{i+1}/{len(GRE_WORDS)}: {word}")
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"The {word} strategy proved effective.",
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch14.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
