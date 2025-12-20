import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("paragon", "Advanced", "noun", "model of excellence"),
    ("pariah", "Advanced", "noun", "outcast"),
    ("parochial", "Advanced", "adjective", "having a limited outlook"),
    ("parsimonious", "Advanced", "adjective", "extremely unwilling to spend"),
    ("partisan", "Advanced", "noun", "strong supporter of a party"),
    ("patent", "Advanced", "adjective", "easily recognizable; obvious"),
    ("pathological", "Advanced", "adjective", "involving mental illness"),
    ("paucity", "Advanced", "noun", "scarcity"),
    ("pedantic", "Advanced", "adjective", "excessively concerned with details"),
    ("pellucid", "Expert", "adjective", "easily understood; clear"),
    ("penchant", "Advanced", "noun", "strong liking for something"),
    ("penurious", "Expert", "adjective", "extremely poor"),
    ("peremptory", "Advanced", "adjective", "expecting immediate obedience"),
    ("perfidy", "Expert", "noun", "deceitfulness; untrustworthiness"),
    ("perfunctory", "Advanced", "adjective", "done without care"),
    ("peripatetic", "Expert", "adjective", "traveling from place to place"),
    ("pernicious", "Advanced", "adjective", "having harmful effect"),
    ("perspicacious", "Expert", "adjective", "having keen insight"),
    ("pertinacious", "Expert", "adjective", "stubbornly persistent"),
    ("pervasive", "Advanced", "adjective", "spreading throughout"),
    ("petulant", "Advanced", "adjective", "childishly bad-tempered"),
    ("phlegmatic", "Expert", "adjective", "calm and unemotional"),
    ("pithy", "Advanced", "adjective", "concise and meaningful"),
    ("placate", "Advanced", "verb", "to make less angry"),
    ("plaintive", "Advanced", "adjective", "sounding sad"),
    ("platitude", "Advanced", "noun", "remark used too often"),
    ("plethora", "Advanced", "noun", "excess of something"),
    ("polarize", "Advanced", "verb", "to divide into opposing groups"),
    ("polemic", "Advanced", "noun", "strong verbal attack"),
    ("ponderous", "Advanced", "adjective", "slow and clumsy"),
    ("pragmatic", "Advanced", "adjective", "dealing with matters practically"),
    ("precarious", "Advanced", "adjective", "not securely held"),
    ("precipitate", "Advanced", "verb", "to cause to happen suddenly"),
    ("preclude", "Advanced", "verb", "to prevent from happening"),
    ("precocious", "Advanced", "adjective", "developed earlier than usual"),
    ("predilection", "Advanced", "noun", "preference or liking"),
    ("prescient", "Expert", "adjective", "having knowledge of future"),
    ("presumptuous", "Advanced", "adjective", "overstepping due bounds"),
    ("prevaricate", "Advanced", "verb", "to speak evasively"),
    ("pristine", "Advanced", "adjective", "in original condition"),
    ("probity", "Expert", "noun", "integrity and honesty"),
    ("proclivity", "Advanced", "noun", "tendency toward something"),
    ("prodigal", "Advanced", "adjective", "wastefully extravagant"),
    ("prodigious", "Advanced", "adjective", "remarkably great"),
    ("profligate", "Advanced", "adjective", "recklessly wasteful"),
    ("profound", "Advanced", "adjective", "very deep or intense"),
    ("profuse", "Advanced", "adjective", "plentiful; abundant"),
    ("proliferate", "Advanced", "verb", "to increase rapidly"),
    ("prolific", "Advanced", "adjective", "producing many works"),
    ("propensity", "Advanced", "noun", "natural tendency"),
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
    start_id = 201
    
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch4.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Generated {len(words)} words!")
