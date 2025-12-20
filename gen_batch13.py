import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("drivel", "Advanced", "noun", "silly nonsense"),
    ("droll", "Expert", "adjective", "amusing in odd way"),
    ("drought", "Advanced", "noun", "prolonged period of dry weather"),
    ("drudgery", "Advanced", "noun", "hard menial work"),
    ("dubious", "Advanced", "adjective", "hesitating or doubting"),
    ("dupe", "Advanced", "noun", "person who is deceived"),
    ("duplicity", "Advanced", "noun", "deceitfulness"),
    ("durable", "Advanced", "adjective", "able to withstand wear"),
    ("duress", "Advanced", "noun", "threats or violence"),
    ("dynamic", "Advanced", "adjective", "characterized by constant change"),
    ("earnest", "Advanced", "adjective", "resulting from serious intent"),
    ("ebb", "Advanced", "verb", "to move away from land"),
    ("ebullient", "Advanced", "adjective", "cheerful and full of energy"),
    ("eccentric", "Advanced", "adjective", "unconventional and strange"),
    ("eclectic", "Advanced", "adjective", "deriving from various sources"),
    ("eclipse", "Advanced", "verb", "to deprive of significance"),
    ("economical", "Advanced", "adjective", "giving good value"),
    ("ecstatic", "Advanced", "adjective", "feeling overwhelming happiness"),
    ("edify", "Advanced", "verb", "to instruct and improve morally"),
    ("edifice", "Expert", "noun", "large imposing building"),
    ("efface", "Advanced", "verb", "to erase or remove"),
    ("effectuate", "Expert", "verb", "to put into force"),
    ("effervescent", "Advanced", "adjective", "vivacious and enthusiastic"),
    ("effete", "Expert", "adjective", "affected or overrefined"),
    ("efficacious", "Advanced", "adjective", "successful in producing result"),
    ("effrontery", "Expert", "noun", "insolent boldness"),
    ("effulgent", "Expert", "adjective", "shining brightly"),
    ("effusive", "Advanced", "adjective", "expressing gratitude excessively"),
    ("egalitarian", "Advanced", "adjective", "relating to equal rights"),
    ("egocentric", "Advanced", "adjective", "thinking only of oneself"),
    ("egregious", "Advanced", "adjective", "outstandingly bad"),
    ("elaborate", "Advanced", "adjective", "involving many details"),
    ("elated", "Advanced", "adjective", "ecstatically happy"),
    ("elation", "Advanced", "noun", "great happiness"),
    ("elegy", "Advanced", "noun", "poem of serious reflection"),
    ("elicit", "Advanced", "verb", "to evoke or draw out"),
    ("elite", "Advanced", "noun", "group regarded as superior"),
    ("elocution", "Expert", "noun", "skill of clear speech"),
    ("eloquent", "Advanced", "adjective", "fluent or persuasive"),
    ("elucidate", "Advanced", "verb", "to make clear"),
    ("elude", "Advanced", "verb", "to evade or escape from"),
    ("elusive", "Advanced", "adjective", "difficult to find"),
    ("emaciated", "Advanced", "adjective", "abnormally thin"),
    ("emanate", "Advanced", "verb", "to issue or spread out"),
    ("emancipate", "Advanced", "verb", "to set free"),
    ("embargo", "Advanced", "noun", "official ban on trade"),
    ("embark", "Advanced", "verb", "to begin course of action"),
    ("embarrass", "Advanced", "verb", "to cause to feel awkward"),
    ("embed", "Advanced", "verb", "to fix firmly"),
    ("embellish", "Advanced", "verb", "to make more attractive"),
    ("embezzle", "Advanced", "verb", "to steal entrusted funds"),
    ("embitter", "Advanced", "verb", "to cause to feel bitter"),
    ("embody", "Advanced", "verb", "to give body to"),
    ("embolden", "Advanced", "verb", "to give courage to"),
    ("embrace", "Advanced", "verb", "to accept willingly"),
    ("embroil", "Advanced", "verb", "to involve in conflict"),
    ("embryonic", "Advanced", "adjective", "in early stage"),
    ("emend", "Expert", "verb", "to make corrections to"),
    ("emerge", "Advanced", "verb", "to move out of"),
    ("eminence", "Advanced", "noun", "fame or superiority"),
    ("eminent", "Advanced", "adjective", "famous and respected"),
    ("emit", "Advanced", "verb", "to produce and discharge"),
    ("emollient", "Expert", "adjective", "having softening effect"),
    ("empathy", "Advanced", "noun", "ability to understand feelings"),
    ("emphatic", "Advanced", "adjective", "showing emphasis"),
    ("empirical", "Advanced", "adjective", "based on observation"),
    ("empower", "Advanced", "verb", "to give power or authority"),
    ("emulate", "Advanced", "verb", "to match or surpass"),
    ("enamored", "Advanced", "adjective", "filled with love"),
    ("encapsulate", "Advanced", "verb", "to express essential features"),
    ("enchant", "Advanced", "verb", "to fill with delight"),
    ("encircle", "Advanced", "verb", "to form circle around"),
    ("enclave", "Advanced", "noun", "portion of territory"),
    ("encompass", "Advanced", "verb", "to surround and have within"),
    ("encroach", "Advanced", "verb", "to intrude on territory"),
    ("encumber", "Advanced", "verb", "to restrict or burden"),
    ("endemic", "Advanced", "adjective", "native or restricted to place"),
    ("endorse", "Advanced", "verb", "to declare approval of"),
    ("endow", "Advanced", "verb", "to provide with quality"),
    ("endure", "Advanced", "verb", "to suffer patiently"),
    ("enervate", "Advanced", "verb", "to cause to feel drained"),
    ("enfeeble", "Expert", "verb", "to make weak"),
    ("enforce", "Advanced", "verb", "to compel observance of"),
    ("enfranchise", "Advanced", "verb", "to give right to vote"),
    ("engage", "Advanced", "verb", "to occupy attention of"),
    ("engender", "Advanced", "verb", "to cause or give rise to"),
    ("engross", "Advanced", "verb", "to absorb attention of"),
    ("engulf", "Advanced", "verb", "to sweep over and surround"),
    ("enhance", "Advanced", "verb", "to intensify or increase"),
    ("enigma", "Advanced", "noun", "person or thing that is mysterious"),
    ("enigmatic", "Advanced", "adjective", "difficult to interpret"),
    ("enjoin", "Advanced", "verb", "to instruct or urge"),
    ("enlighten", "Advanced", "verb", "to give spiritual insight"),
    ("enmity", "Advanced", "noun", "state of being enemy"),
    ("ennui", "Expert", "noun", "feeling of listlessness"),
    ("enormity", "Advanced", "noun", "great size or extent"),
    ("enrage", "Advanced", "verb", "to make very angry"),
    ("enrapture", "Advanced", "verb", "to give intense pleasure"),
    ("enrich", "Advanced", "verb", "to improve quality of"),
    ("ensue", "Advanced", "verb", "to happen afterward"),
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
    start_id = 1001
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"{i+1}/{len(GRE_WORDS)}: {word}")
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"Her {word} demeanor impressed everyone.",
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch13.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
