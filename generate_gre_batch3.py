import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("lethargic", "Advanced", "adjective", "sluggish and apathetic"),
    ("levity", "Advanced", "noun", "humor or lack of seriousness"),
    ("limpid", "Expert", "adjective", "clear and transparent"),
    ("lissome", "Expert", "adjective", "thin and graceful"),
    ("litigious", "Advanced", "adjective", "prone to engage in lawsuits"),
    ("loquacious", "Advanced", "adjective", "tending to talk a great deal"),
    ("lucid", "Advanced", "adjective", "expressed clearly"),
    ("lugubrious", "Expert", "adjective", "looking sad and dismal"),
    ("magnanimous", "Advanced", "adjective", "generous or forgiving"),
    ("maladroit", "Expert", "adjective", "ineffective or bungling"),
    ("malinger", "Advanced", "verb", "to pretend to be ill"),
    ("malleable", "Advanced", "adjective", "easily influenced"),
    ("maverick", "Advanced", "noun", "independent-minded person"),
    ("mendacious", "Advanced", "adjective", "not telling the truth"),
    ("mercurial", "Advanced", "adjective", "subject to sudden changes"),
    ("meretricious", "Expert", "adjective", "attractive but valueless"),
    ("meticulous", "Advanced", "adjective", "very careful about details"),
    ("milieu", "Advanced", "noun", "social environment"),
    ("misanthrope", "Advanced", "noun", "person who dislikes mankind"),
    ("mitigate", "Advanced", "verb", "to make less severe"),
    ("mollify", "Advanced", "verb", "to calm someone's anger"),
    ("moribund", "Expert", "adjective", "at point of death"),
    ("multifarious", "Expert", "adjective", "many and various"),
    ("mundane", "Advanced", "adjective", "lacking interest; ordinary"),
    ("munificent", "Expert", "adjective", "very generous"),
    ("nascent", "Advanced", "adjective", "just beginning to develop"),
    ("nefarious", "Advanced", "adjective", "wicked or criminal"),
    ("neophyte", "Advanced", "noun", "beginner or novice"),
    ("nettlesome", "Expert", "adjective", "causing annoyance"),
    ("noisome", "Expert", "adjective", "having offensive smell"),
    ("nonchalant", "Advanced", "adjective", "calm and relaxed"),
    ("nonplussed", "Advanced", "adjective", "surprised and confused"),
    ("notorious", "Advanced", "adjective", "famous for something bad"),
    ("obdurate", "Advanced", "adjective", "stubbornly refusing to change"),
    ("obfuscate", "Advanced", "verb", "to make unclear"),
    ("obsequious", "Advanced", "adjective", "excessively compliant"),
    ("obstinate", "Advanced", "adjective", "stubbornly refusing to change"),
    ("obviate", "Advanced", "verb", "to remove a need or difficulty"),
    ("occlude", "Expert", "verb", "to stop or close up"),
    ("odious", "Advanced", "adjective", "extremely unpleasant"),
    ("officious", "Advanced", "adjective", "assertive in interfering"),
    ("onerous", "Advanced", "adjective", "involving heavy obligation"),
    ("opaque", "Advanced", "adjective", "not transparent; unclear"),
    ("opprobrious", "Expert", "adjective", "expressing contempt"),
    ("oscillate", "Advanced", "verb", "to swing back and forth"),
    ("ossified", "Expert", "adjective", "rigid; unable to change"),
    ("ostentatious", "Advanced", "adjective", "showy and pretentious"),
    ("palliate", "Expert", "verb", "to make less severe"),
    ("panacea", "Advanced", "noun", "solution for all problems"),
    ("paradigm", "Advanced", "noun", "typical example or pattern"),
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
    start_id = 151
    
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch3.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Generated {len(words)} words!")
