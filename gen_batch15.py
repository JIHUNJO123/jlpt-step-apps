import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("exquisite", "Advanced", "adjective", "extremely beautiful"),
    ("extant", "Expert", "adjective", "still in existence"),
    ("extemporaneous", "Expert", "adjective", "spoken without preparation"),
    ("extend", "Advanced", "verb", "to cause to cover larger area"),
    ("extensive", "Advanced", "adjective", "covering large area"),
    ("extenuate", "Expert", "verb", "to make offense seem less serious"),
    ("exterior", "Advanced", "adjective", "forming outer surface"),
    ("exterminate", "Advanced", "verb", "to destroy completely"),
    ("external", "Advanced", "adjective", "belonging to outside"),
    ("extinct", "Advanced", "adjective", "no longer in existence"),
    ("extinguish", "Advanced", "verb", "to cause to cease burning"),
    ("extirpate", "Expert", "verb", "to root out and destroy"),
    ("extol", "Advanced", "verb", "to praise enthusiastically"),
    ("extort", "Advanced", "verb", "to obtain by force or threats"),
    ("extract", "Advanced", "verb", "to remove or take out"),
    ("extraneous", "Advanced", "adjective", "irrelevant or unrelated"),
    ("extraordinary", "Advanced", "adjective", "very unusual or remarkable"),
    ("extrapolate", "Advanced", "verb", "to extend application"),
    ("extravagant", "Advanced", "adjective", "lacking restraint in spending"),
    ("extremist", "Advanced", "noun", "person with extreme views"),
    ("extricate", "Advanced", "verb", "to free from constraint"),
    ("extrinsic", "Advanced", "adjective", "not part of essential nature"),
    ("extrovert", "Advanced", "noun", "outgoing person"),
    ("exuberant", "Advanced", "adjective", "filled with energy"),
    ("exude", "Advanced", "verb", "to discharge slowly"),
    ("exult", "Advanced", "verb", "to show triumph"),
    ("fabricate", "Advanced", "verb", "to invent to deceive"),
    ("facade", "Advanced", "noun", "outward appearance"),
    ("facet", "Advanced", "noun", "one side of something"),
    ("facetious", "Advanced", "adjective", "treating serious issues lightly"),
    ("facilitate", "Advanced", "verb", "to make easier"),
    ("faction", "Advanced", "noun", "small dissenting group"),
    ("factious", "Expert", "adjective", "relating to faction"),
    ("fallacious", "Advanced", "adjective", "based on mistaken belief"),
    ("fallacy", "Advanced", "noun", "mistaken belief"),
    ("fallible", "Advanced", "adjective", "capable of making mistakes"),
    ("fallow", "Expert", "adjective", "plowed but left unsown"),
    ("falter", "Advanced", "verb", "to start to lose strength"),
    ("fanatical", "Advanced", "adjective", "filled with excessive zeal"),
    ("fanciful", "Advanced", "adjective", "overimaginative"),
    ("farce", "Advanced", "noun", "absurd event"),
    ("fastidious", "Advanced", "adjective", "very attentive to detail"),
    ("fatal", "Advanced", "adjective", "causing death"),
    ("fatalistic", "Advanced", "adjective", "believing events are predetermined"),
    ("fathom", "Advanced", "verb", "to understand after thought"),
    ("fatigue", "Advanced", "noun", "extreme tiredness"),
    ("fatuous", "Expert", "adjective", "silly and pointless"),
    ("fault", "Advanced", "noun", "responsibility for wrongdoing"),
    ("fawn", "Advanced", "verb", "to give slavish flattery"),
    ("faze", "Advanced", "verb", "to disturb or disconcert"),
    ("feasible", "Advanced", "adjective", "possible to do easily"),
    ("feat", "Advanced", "noun", "achievement requiring skill"),
    ("feckless", "Expert", "adjective", "lacking initiative"),
    ("fecund", "Expert", "adjective", "producing offspring"),
    ("feign", "Advanced", "verb", "to pretend to be affected"),
    ("feint", "Advanced", "noun", "deceptive movement"),
    ("felicitous", "Expert", "adjective", "well chosen or apt"),
    ("fell", "Advanced", "adjective", "of terrible evil"),
    ("felon", "Advanced", "noun", "person convicted of crime"),
    ("ferment", "Advanced", "noun", "agitation and excitement"),
    ("ferocious", "Advanced", "adjective", "savagely fierce"),
    ("ferret", "Advanced", "verb", "to search tenaciously"),
    ("fertile", "Advanced", "adjective", "producing abundant vegetation"),
    ("fervent", "Advanced", "adjective", "having passionate intensity"),
    ("fervid", "Expert", "adjective", "intensely enthusiastic"),
    ("fervor", "Advanced", "noun", "intense feeling"),
    ("fester", "Advanced", "verb", "to become worse"),
    ("festive", "Advanced", "adjective", "relating to festival"),
    ("fetter", "Advanced", "verb", "to restrain with chains"),
    ("feud", "Advanced", "noun", "prolonged quarrel"),
    ("fickle", "Advanced", "adjective", "changing frequently"),
    ("fictitious", "Advanced", "adjective", "not real or true"),
    ("fidelity", "Advanced", "noun", "faithfulness to person"),
    ("fiery", "Advanced", "adjective", "consisting of fire"),
    ("figment", "Advanced", "noun", "thing believed to be real"),
    ("figurative", "Advanced", "adjective", "departing from literal use"),
    ("filch", "Advanced", "verb", "to pilfer or steal"),
    ("filibuster", "Expert", "noun", "action of obstructing progress"),
    ("finale", "Advanced", "noun", "last part of performance"),
    ("finesse", "Advanced", "noun", "impressive skill"),
    ("finite", "Advanced", "adjective", "limited in size"),
    ("fissure", "Advanced", "noun", "long narrow crack"),
    ("fitful", "Advanced", "adjective", "active or occurring intermittently"),
    ("flagrant", "Advanced", "adjective", "conspicuously offensive"),
    ("flair", "Advanced", "noun", "natural ability"),
    ("flamboyant", "Advanced", "adjective", "attracting attention"),
    ("flaunt", "Advanced", "verb", "to display ostentatiously"),
    ("flaw", "Advanced", "noun", "mark or imperfection"),
    ("fledgling", "Advanced", "noun", "person or organization that is new"),
    ("fleeting", "Advanced", "adjective", "lasting very short time"),
    ("flimsy", "Advanced", "adjective", "insubstantial and weak"),
    ("flinch", "Advanced", "verb", "to make quick movement"),
    ("flippant", "Advanced", "adjective", "not showing serious attitude"),
    ("flit", "Advanced", "verb", "to move swiftly"),
    ("florid", "Advanced", "adjective", "having red complexion"),
    ("flourish", "Advanced", "verb", "to grow vigorously"),
    ("flout", "Advanced", "verb", "to openly disregard"),
    ("fluctuate", "Advanced", "verb", "to rise and fall irregularly"),
    ("fluent", "Advanced", "adjective", "able to express easily"),
    ("flux", "Advanced", "noun", "continuous change"),
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
    start_id = 1201
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"{i+1}/{len(GRE_WORDS)}: {word}")
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"The {word} condition was immediately apparent.",
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch15.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
