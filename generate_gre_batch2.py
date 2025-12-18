import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("harangue", "Advanced", "noun", "lengthy aggressive speech"),
    ("hegemony", "Expert", "noun", "dominance of one group over another"),
    ("heresy", "Advanced", "noun", "belief contrary to accepted doctrine"),
    ("heterodox", "Expert", "adjective", "not conforming to accepted beliefs"),
    ("histrionic", "Advanced", "adjective", "overly theatrical or dramatic"),
    ("homogeneous", "Advanced", "adjective", "of the same kind; uniform"),
    ("hubris", "Advanced", "noun", "excessive pride or arrogance"),
    ("iconoclast", "Advanced", "noun", "one who attacks established beliefs"),
    ("idiosyncratic", "Advanced", "adjective", "peculiar to an individual"),
    ("ignominious", "Expert", "adjective", "deserving public disgrace"),
    ("immutable", "Advanced", "adjective", "unchanging over time"),
    ("impassive", "Advanced", "adjective", "not feeling or showing emotion"),
    ("impecunious", "Expert", "adjective", "having little or no money"),
    ("imperious", "Advanced", "adjective", "arrogantly domineering"),
    ("imperturbable", "Advanced", "adjective", "unable to be upset"),
    ("impervious", "Advanced", "adjective", "not affected by"),
    ("implacable", "Advanced", "adjective", "unable to be appeased"),
    ("impugn", "Advanced", "verb", "to challenge as false"),
    ("inchoate", "Expert", "adjective", "just begun; not fully formed"),
    ("incongruous", "Advanced", "adjective", "not in harmony; inappropriate"),
    ("incorrigible", "Advanced", "adjective", "not able to be reformed"),
    ("indefatigable", "Expert", "adjective", "persisting tirelessly"),
    ("indigent", "Advanced", "adjective", "poor; needy"),
    ("indolent", "Advanced", "adjective", "wanting to avoid activity"),
    ("ineffable", "Expert", "adjective", "too great to be expressed"),
    ("ineluctable", "Expert", "adjective", "impossible to avoid"),
    ("ingenuous", "Advanced", "adjective", "innocent and unsuspecting"),
    ("inimical", "Advanced", "adjective", "hostile; unfriendly"),
    ("innate", "Advanced", "adjective", "inborn; natural"),
    ("innocuous", "Advanced", "adjective", "not harmful or offensive"),
    ("inscrutable", "Advanced", "adjective", "impossible to understand"),
    ("insidious", "Advanced", "adjective", "gradually harmful"),
    ("insipid", "Advanced", "adjective", "lacking flavor or interest"),
    ("intractable", "Advanced", "adjective", "hard to control or deal with"),
    ("intransigent", "Advanced", "adjective", "unwilling to compromise"),
    ("inundate", "Advanced", "verb", "to overwhelm with things"),
    ("inure", "Expert", "verb", "to accustom to something unpleasant"),
    ("invective", "Expert", "noun", "insulting abusive language"),
    ("inveterate", "Advanced", "adjective", "long-established; habitual"),
    ("irascible", "Advanced", "adjective", "easily angered"),
    ("irresolute", "Advanced", "adjective", "showing hesitancy"),
    ("itinerant", "Advanced", "adjective", "traveling from place to place"),
    ("jaundiced", "Advanced", "adjective", "affected by bitterness"),
    ("jejune", "Expert", "adjective", "naive, simplistic, dull"),
    ("juxtapose", "Advanced", "verb", "to place side by side"),
    ("laconic", "Advanced", "adjective", "using few words"),
    ("languid", "Advanced", "adjective", "lacking energy"),
    ("lassitude", "Expert", "noun", "physical or mental weariness"),
    ("latent", "Advanced", "adjective", "existing but not yet developed"),
    ("laudable", "Advanced", "adjective", "deserving praise"),
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
    start_id = 101
    
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"Processing {i+1}/{len(GRE_WORDS)}: {word}")
        
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"The {word} situation required immediate attention.",
            "category": "General",
            "translations": {
                "ko": translate(definition, "ko"),
                "zh": translate(definition, "zh-CN"),
                "hi": translate(definition, "hi")
            }
        }
        words.append(word_data)
        time.sleep(0.1)
    
    return words

if __name__ == "__main__":
    words = generate_words()
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch2.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Generated {len(words)} words!")
