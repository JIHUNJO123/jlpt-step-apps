import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("propitiate", "Expert", "verb", "to win favor by doing something"),
    ("prosaic", "Advanced", "adjective", "lacking imagination; dull"),
    ("proscribe", "Advanced", "verb", "to forbid"),
    ("proselytize", "Advanced", "verb", "to convert to different belief"),
    ("provincial", "Advanced", "adjective", "unsophisticated"),
    ("prudent", "Advanced", "adjective", "acting with care"),
    ("prurient", "Expert", "adjective", "having excessive interest"),
    ("punctilious", "Expert", "adjective", "showing great attention to detail"),
    ("pusillanimous", "Expert", "adjective", "showing lack of courage"),
    ("quagmire", "Advanced", "noun", "difficult situation"),
    ("quandary", "Advanced", "noun", "state of uncertainty"),
    ("querulous", "Advanced", "adjective", "complaining in petulant way"),
    ("quiescent", "Expert", "adjective", "in state of inactivity"),
    ("quixotic", "Advanced", "adjective", "unrealistic and impractical"),
    ("quotidian", "Expert", "adjective", "of daily occurrence; ordinary"),
    ("rancorous", "Advanced", "adjective", "showing deep bitterness"),
    ("rapacious", "Expert", "adjective", "aggressively greedy"),
    ("rarefied", "Expert", "adjective", "elevated; exclusive"),
    ("recalcitrant", "Advanced", "adjective", "stubbornly uncooperative"),
    ("recant", "Advanced", "verb", "to withdraw former belief"),
    ("recondite", "Expert", "adjective", "difficult to understand"),
    ("rectitude", "Expert", "noun", "morally correct behavior"),
    ("redoubtable", "Expert", "adjective", "formidable"),
    ("refractory", "Expert", "adjective", "stubbornly disobedient"),
    ("relegate", "Advanced", "verb", "to assign to lower position"),
    ("remonstrate", "Advanced", "verb", "to protest forcefully"),
    ("renege", "Advanced", "verb", "to go back on promise"),
    ("replete", "Advanced", "adjective", "filled or well-supplied"),
    ("reprobate", "Expert", "noun", "unprincipled person"),
    ("repudiate", "Advanced", "verb", "to refuse to accept"),
    ("rescind", "Advanced", "verb", "to revoke or cancel"),
    ("reticent", "Advanced", "adjective", "not revealing thoughts"),
    ("rhetoric", "Advanced", "noun", "art of persuasive speaking"),
    ("ribald", "Expert", "adjective", "humorously vulgar"),
    ("riposte", "Expert", "noun", "quick clever reply"),
    ("rogue", "Advanced", "noun", "dishonest or unprincipled person"),
    ("rudimentary", "Advanced", "adjective", "involving basic principles"),
    ("ruminate", "Advanced", "verb", "to think deeply about"),
    ("sagacious", "Advanced", "adjective", "having keen discernment"),
    ("salient", "Advanced", "adjective", "most noticeable"),
    ("sanctimonious", "Advanced", "adjective", "making show of being moral"),
    ("sanguine", "Advanced", "adjective", "optimistic; cheerful"),
    ("sardonic", "Advanced", "adjective", "grimly mocking"),
    ("scrupulous", "Advanced", "adjective", "diligent and thorough"),
    ("sedulous", "Expert", "adjective", "showing dedication"),
    ("self-effacing", "Advanced", "adjective", "not drawing attention"),
    ("sententious", "Expert", "adjective", "given to moralizing"),
    ("serendipitous", "Advanced", "adjective", "occurring by chance"),
    ("servile", "Advanced", "adjective", "having excessive eagerness"),
    ("skeptical", "Advanced", "adjective", "not easily convinced"),
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
    start_id = 251
    
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch5.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Generated {len(words)} words!")
