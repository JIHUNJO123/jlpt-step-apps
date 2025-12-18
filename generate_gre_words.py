import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("efficacious", "Advanced", "adjective", "effective; producing desired result"),
    ("effrontery", "Expert", "noun", "shameless boldness"),
    ("egregious", "Advanced", "adjective", "outstandingly bad"),
    ("elegy", "Advanced", "noun", "a mournful poem for the dead"),
    ("elucidate", "Advanced", "verb", "to make clear; explain"),
    ("emollient", "Expert", "adjective", "softening or soothing"),
    ("encomium", "Expert", "noun", "formal expression of praise"),
    ("endemic", "Advanced", "adjective", "native to a particular region"),
    ("enervate", "Advanced", "verb", "to weaken or drain energy"),
    ("engender", "Advanced", "verb", "to cause or give rise to"),
    ("ephemeral", "Advanced", "adjective", "lasting a very short time"),
    ("equanimity", "Advanced", "noun", "calmness of mind"),
    ("equivocate", "Advanced", "verb", "to use ambiguous language"),
    ("erudite", "Advanced", "adjective", "having great knowledge"),
    ("eschew", "Advanced", "verb", "to deliberately avoid"),
    ("esoteric", "Advanced", "adjective", "understood by few"),
    ("exacerbate", "Advanced", "verb", "to make worse"),
    ("excoriate", "Expert", "verb", "to criticize severely"),
    ("exculpate", "Advanced", "verb", "to clear from blame"),
    ("exigent", "Expert", "adjective", "requiring immediate action"),
    ("exonerate", "Advanced", "verb", "to clear of blame"),
    ("expatiate", "Expert", "verb", "to speak or write at length"),
    ("expiate", "Expert", "verb", "to make amends for"),
    ("extirpate", "Expert", "verb", "to destroy completely"),
    ("facetious", "Advanced", "adjective", "treating serious issues with humor"),
    ("fallacious", "Advanced", "adjective", "based on false reasoning"),
    ("fastidious", "Advanced", "adjective", "very attentive to detail"),
    ("fatuous", "Expert", "adjective", "silly and pointless"),
    ("fecund", "Expert", "adjective", "fertile; intellectually productive"),
    ("felicitous", "Advanced", "adjective", "well-suited; apt"),
    ("fervent", "Advanced", "adjective", "showing passionate intensity"),
    ("fetter", "Advanced", "verb", "to restrain or restrict"),
    ("flag", "Advanced", "verb", "to become tired or weak"),
    ("florid", "Advanced", "adjective", "elaborate; ruddy complexion"),
    ("foment", "Advanced", "verb", "to instigate or stir up"),
    ("forestall", "Advanced", "verb", "to prevent by taking action"),
    ("fortuitous", "Advanced", "adjective", "happening by chance"),
    ("fractious", "Advanced", "adjective", "irritable and quarrelsome"),
    ("fulminate", "Expert", "verb", "to protest strongly"),
    ("furtive", "Advanced", "adjective", "attempting to avoid notice"),
    ("gainsay", "Expert", "verb", "to deny or contradict"),
    ("garrulous", "Advanced", "adjective", "excessively talkative"),
    ("germane", "Advanced", "adjective", "relevant to the subject"),
    ("glib", "Advanced", "adjective", "fluent but insincere"),
    ("gossamer", "Expert", "adjective", "light, delicate, insubstantial"),
    ("grandiloquent", "Expert", "adjective", "pompous in speech"),
    ("gratuitous", "Advanced", "adjective", "uncalled for; unwarranted"),
    ("gregarious", "Advanced", "adjective", "fond of company"),
    ("hackneyed", "Advanced", "adjective", "overused and unoriginal"),
    ("halcyon", "Expert", "adjective", "happy, golden, peaceful"),
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
    start_id = 51
    
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"Processing {i+1}/{len(GRE_WORDS)}: {word}")
        
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"The professor used the word {word} in context.",
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch1.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Generated {len(words)} words!")
