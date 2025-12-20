import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("defile", "Advanced", "verb", "to damage purity of"),
    ("definitive", "Advanced", "adjective", "decisive and unconditional"),
    ("deflect", "Advanced", "verb", "to cause to change direction"),
    ("deft", "Advanced", "adjective", "neatly skillful"),
    ("defunct", "Advanced", "adjective", "no longer existing"),
    ("degrade", "Advanced", "verb", "to treat with disrespect"),
    ("deify", "Expert", "verb", "to worship as god"),
    ("deign", "Advanced", "verb", "to do something reluctantly"),
    ("dejected", "Advanced", "adjective", "sad and depressed"),
    ("deleterious", "Expert", "adjective", "causing harm"),
    ("deliberate", "Advanced", "adjective", "done consciously"),
    ("delineate", "Advanced", "verb", "to describe precisely"),
    ("delude", "Advanced", "verb", "to impose false belief"),
    ("deluge", "Advanced", "noun", "severe flood"),
    ("delusion", "Advanced", "noun", "false belief"),
    ("demagogue", "Advanced", "noun", "political leader appealing to desires"),
    ("demean", "Advanced", "verb", "to cause loss of dignity"),
    ("demeanor", "Advanced", "noun", "outward behavior"),
    ("demise", "Advanced", "noun", "person's death"),
    ("demographic", "Advanced", "adjective", "relating to population"),
    ("demolish", "Advanced", "verb", "to pull down building"),
    ("demonize", "Advanced", "verb", "to portray as wicked"),
    ("demote", "Advanced", "verb", "to give lower rank"),
    ("demur", "Advanced", "verb", "to raise doubts"),
    ("demure", "Advanced", "adjective", "reserved and modest"),
    ("denigrate", "Advanced", "verb", "to criticize unfairly"),
    ("denizen", "Expert", "noun", "inhabitant or occupant"),
    ("denomination", "Advanced", "noun", "recognized branch of church"),
    ("denote", "Advanced", "verb", "to be sign of"),
    ("denounce", "Advanced", "verb", "to publicly declare wrong"),
    ("denunciation", "Advanced", "noun", "public condemnation"),
    ("depict", "Advanced", "verb", "to show in picture"),
    ("deplete", "Advanced", "verb", "to use up supply"),
    ("deplore", "Advanced", "verb", "to feel strong disapproval"),
    ("deploy", "Advanced", "verb", "to move into position"),
    ("depose", "Advanced", "verb", "to remove from office"),
    ("depravity", "Advanced", "noun", "moral corruption"),
    ("deprecate", "Advanced", "verb", "to express disapproval"),
    ("depress", "Advanced", "verb", "to make sad"),
    ("deprive", "Advanced", "verb", "to deny possession"),
    ("derelict", "Advanced", "adjective", "in very poor condition"),
    ("deride", "Advanced", "verb", "to express contempt for"),
    ("derivative", "Advanced", "adjective", "imitative of another's work"),
    ("derogate", "Expert", "verb", "to detract from"),
    ("derogatory", "Advanced", "adjective", "showing disrespect"),
    ("descend", "Advanced", "verb", "to move downward"),
    ("desecrate", "Advanced", "verb", "to treat sacred place with disrespect"),
    ("designate", "Advanced", "verb", "to appoint to position"),
    ("desist", "Advanced", "verb", "to cease doing something"),
    ("desolate", "Advanced", "adjective", "bleakly empty"),
    ("despicable", "Advanced", "adjective", "deserving hatred"),
    ("despise", "Advanced", "verb", "to feel contempt for"),
    ("despondent", "Advanced", "adjective", "in low spirits"),
    ("despot", "Advanced", "noun", "ruler with absolute power"),
    ("destitute", "Advanced", "adjective", "without basic necessities"),
    ("desultory", "Expert", "adjective", "lacking plan or purpose"),
    ("detached", "Advanced", "adjective", "separate or disconnected"),
    ("detain", "Advanced", "verb", "to keep in official custody"),
    ("deter", "Advanced", "verb", "to discourage from action"),
    ("detract", "Advanced", "verb", "to reduce value of"),
    ("detrimental", "Advanced", "adjective", "tending to cause harm"),
    ("deviate", "Advanced", "verb", "to depart from norm"),
    ("devious", "Advanced", "adjective", "showing cunning"),
    ("devoid", "Advanced", "adjective", "entirely lacking"),
    ("devolve", "Advanced", "verb", "to transfer to lower level"),
    ("devout", "Advanced", "adjective", "deeply religious"),
    ("dexterous", "Advanced", "adjective", "showing skill"),
    ("diabolical", "Advanced", "adjective", "characteristic of devil"),
    ("diagnose", "Advanced", "verb", "to identify nature of problem"),
    ("dialectic", "Expert", "noun", "art of investigating truth"),
    ("dichotomy", "Advanced", "noun", "division into two parts"),
    ("dictate", "Advanced", "verb", "to lay down authoritatively"),
    ("didactic", "Advanced", "adjective", "intended to teach"),
    ("differentiate", "Advanced", "verb", "to recognize as different"),
    ("diffident", "Advanced", "adjective", "modest or shy"),
    ("diffuse", "Advanced", "adjective", "spread over wide area"),
    ("digress", "Advanced", "verb", "to leave main subject"),
    ("dilapidated", "Advanced", "adjective", "in state of disrepair"),
    ("dilate", "Advanced", "verb", "to make wider"),
    ("dilatory", "Expert", "adjective", "slow to act"),
    ("dilemma", "Advanced", "noun", "situation requiring difficult choice"),
    ("diligent", "Advanced", "adjective", "having careful effort"),
    ("dilute", "Advanced", "verb", "to make thinner or weaker"),
    ("diminish", "Advanced", "verb", "to make smaller"),
    ("diminutive", "Advanced", "adjective", "extremely small"),
    ("din", "Advanced", "noun", "loud unpleasant noise"),
    ("dire", "Advanced", "adjective", "extremely serious"),
    ("dirge", "Expert", "noun", "mournful song"),
    ("disabuse", "Advanced", "verb", "to persuade that idea is false"),
    ("disaffected", "Advanced", "adjective", "dissatisfied with authority"),
    ("disambiguate", "Advanced", "verb", "to remove uncertainty"),
    ("disapprobation", "Expert", "noun", "strong disapproval"),
    ("disarray", "Advanced", "noun", "state of disorganization"),
    ("disavow", "Advanced", "verb", "to deny responsibility"),
    ("discern", "Advanced", "verb", "to perceive or recognize"),
    ("discerning", "Advanced", "adjective", "having good judgment"),
    ("disclaim", "Advanced", "verb", "to refuse to acknowledge"),
    ("disclose", "Advanced", "verb", "to make known"),
    ("discombobulate", "Expert", "verb", "to confuse or disconcert"),
    ("discomfit", "Expert", "verb", "to make uneasy"),
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
    start_id = 801
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"{i+1}/{len(GRE_WORDS)}: {word}")
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"The analysis revealed a {word} pattern.",
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch11.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
