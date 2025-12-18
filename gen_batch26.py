import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("ponderous", "Advanced", "adjective", "slow and clumsy"),
    ("pontificate", "Advanced", "verb", "to express opinions dogmatically"),
    ("portend", "Advanced", "verb", "to be a sign of"),
    ("portent", "Advanced", "noun", "sign of something to come"),
    ("portentous", "Advanced", "adjective", "of great significance"),
    ("posit", "Advanced", "verb", "to assume as fact"),
    ("posterity", "Advanced", "noun", "all future generations"),
    ("posthumous", "Advanced", "adjective", "occurring after death"),
    ("postulate", "Advanced", "verb", "to suggest as basis"),
    ("potable", "Advanced", "adjective", "safe to drink"),
    ("potent", "Advanced", "adjective", "having great power"),
    ("potentate", "Expert", "noun", "monarch or ruler"),
    ("pragmatic", "Advanced", "adjective", "dealing with matters practically"),
    ("prate", "Expert", "verb", "to talk foolishly"),
    ("prattle", "Advanced", "verb", "to talk at length foolishly"),
    ("precarious", "Advanced", "adjective", "not securely held"),
    ("precedent", "Advanced", "noun", "earlier event taken as example"),
    ("precept", "Advanced", "noun", "general rule of conduct"),
    ("precipitate", "Advanced", "verb", "to cause to happen suddenly"),
    ("precipitous", "Advanced", "adjective", "dangerously high or steep"),
    ("precise", "Advanced", "adjective", "marked by exactness"),
    ("preclude", "Advanced", "verb", "to prevent from happening"),
    ("precocious", "Advanced", "adjective", "having developed early"),
    ("precursor", "Advanced", "noun", "person or thing that comes before"),
    ("predatory", "Advanced", "adjective", "seeking to exploit others"),
    ("predecessor", "Advanced", "noun", "person who held position before"),
    ("predicament", "Advanced", "noun", "difficult situation"),
    ("predicate", "Advanced", "verb", "to state as consequence"),
    ("predilection", "Advanced", "noun", "preference or special liking"),
    ("predispose", "Advanced", "verb", "to make susceptible"),
    ("predominant", "Advanced", "adjective", "present as strongest element"),
    ("preeminent", "Advanced", "adjective", "surpassing all others"),
    ("preempt", "Advanced", "verb", "to take action to prevent"),
    ("preen", "Advanced", "verb", "to groom with beak"),
    ("prejudice", "Advanced", "noun", "preconceived opinion"),
    ("preliminary", "Advanced", "adjective", "denoting action before main event"),
    ("prelude", "Advanced", "noun", "action serving as introduction"),
    ("premature", "Advanced", "adjective", "occurring before proper time"),
    ("premeditate", "Advanced", "verb", "to think out beforehand"),
    ("premise", "Advanced", "noun", "previous statement as basis"),
    ("premonition", "Advanced", "noun", "strong feeling about future"),
    ("preoccupied", "Advanced", "adjective", "absorbed in thought"),
    ("preponderance", "Advanced", "noun", "quality of being greater"),
    ("preposterous", "Advanced", "adjective", "contrary to reason"),
    ("prerogative", "Advanced", "noun", "right or privilege"),
    ("prescient", "Expert", "adjective", "having knowledge of events"),
    ("prescribe", "Advanced", "verb", "to recommend with authority"),
    ("presentiment", "Advanced", "noun", "intuitive feeling about future"),
    ("presumptuous", "Advanced", "adjective", "failing to observe limits"),
    ("pretentious", "Advanced", "adjective", "attempting to impress"),
    ("preternatural", "Expert", "adjective", "beyond what is normal"),
    ("pretext", "Advanced", "noun", "reason given to hide real intention"),
    ("prevail", "Advanced", "verb", "to prove superior"),
    ("prevalent", "Advanced", "adjective", "widespread in area"),
    ("prevaricate", "Advanced", "verb", "to speak evasively"),
    ("prim", "Advanced", "adjective", "stiffly formal"),
    ("pristine", "Advanced", "adjective", "in original condition"),
    ("privation", "Advanced", "noun", "state of being deprived"),
    ("probity", "Expert", "noun", "quality of having strong principles"),
    ("problematic", "Advanced", "adjective", "constituting a problem"),
    ("proclivity", "Advanced", "noun", "inclination or predisposition"),
    ("procrastinate", "Advanced", "verb", "to delay or postpone"),
    ("procure", "Advanced", "verb", "to obtain with care"),
    ("prod", "Advanced", "verb", "to poke with finger"),
    ("prodigal", "Advanced", "adjective", "spending money wastefully"),
    ("prodigious", "Advanced", "adjective", "remarkably great"),
    ("prodigy", "Advanced", "noun", "young person with exceptional abilities"),
    ("profane", "Advanced", "adjective", "not respectful of religious practice"),
    ("profess", "Advanced", "verb", "to claim openly"),
    ("proficient", "Advanced", "adjective", "competent or skilled"),
    ("profound", "Advanced", "adjective", "very great or intense"),
    ("profuse", "Advanced", "adjective", "exuberantly plentiful"),
    ("progenitor", "Expert", "noun", "person who originates movement"),
    ("progeny", "Advanced", "noun", "descendant or offspring"),
    ("prognosis", "Advanced", "noun", "forecast of disease outcome"),
    ("prohibitive", "Advanced", "adjective", "excessively high"),
    ("proliferate", "Advanced", "verb", "to increase rapidly"),
    ("prolific", "Advanced", "adjective", "producing much fruit"),
    ("prolix", "Expert", "adjective", "using too many words"),
    ("prolong", "Advanced", "verb", "to extend duration"),
    ("prominent", "Advanced", "adjective", "important or famous"),
    ("promiscuous", "Advanced", "adjective", "having many partners"),
    ("promote", "Advanced", "verb", "to further progress of"),
    ("prompt", "Advanced", "adjective", "done without delay"),
    ("promulgate", "Advanced", "verb", "to make widely known"),
    ("prone", "Advanced", "adjective", "likely to suffer"),
    ("pronounced", "Advanced", "adjective", "very noticeable"),
    ("propensity", "Advanced", "noun", "inclination or tendency"),
    ("prophetic", "Advanced", "adjective", "accurately describing future"),
    ("propitious", "Expert", "adjective", "giving favorable conditions"),
    ("proponent", "Advanced", "noun", "person who advocates"),
    ("propriety", "Advanced", "noun", "state of being correct"),
    ("prosaic", "Advanced", "adjective", "having commonplace quality"),
    ("proscribe", "Advanced", "verb", "to forbid by law"),
    ("prose", "Advanced", "noun", "written or spoken language"),
    ("proselytize", "Expert", "verb", "to convert to religion"),
    ("prospect", "Advanced", "noun", "possibility of future success"),
    ("prosperous", "Advanced", "adjective", "successful in material terms"),
    ("prostrate", "Advanced", "adjective", "lying stretched out"),
    ("protagonist", "Advanced", "noun", "leading character"),
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
    start_id = 2301
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"{i+1}/{len(GRE_WORDS)}: {word}")
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"The {word} quality defined the entire project.",
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch26.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
