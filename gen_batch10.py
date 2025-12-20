import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("consign", "Advanced", "verb", "to deliver to person's custody"),
    ("consolidate", "Advanced", "verb", "to combine into single unit"),
    ("conspicuous", "Advanced", "adjective", "standing out clearly"),
    ("conspiracy", "Advanced", "noun", "secret plan by group"),
    ("constitute", "Advanced", "verb", "to be component of"),
    ("constrain", "Advanced", "verb", "to compel or force"),
    ("construe", "Advanced", "verb", "to interpret in particular way"),
    ("consummate", "Advanced", "adjective", "showing great skill"),
    ("contagious", "Advanced", "adjective", "spreading by contact"),
    ("contemplate", "Advanced", "verb", "to look at thoughtfully"),
    ("contemporary", "Advanced", "adjective", "belonging to same period"),
    ("contemptuous", "Advanced", "adjective", "showing contempt"),
    ("contend", "Advanced", "verb", "to struggle to surmount"),
    ("contentious", "Advanced", "adjective", "causing disagreement"),
    ("context", "Advanced", "noun", "circumstances forming background"),
    ("contiguous", "Advanced", "adjective", "sharing common border"),
    ("contingent", "Advanced", "adjective", "dependent on"),
    ("contort", "Advanced", "verb", "to twist out of shape"),
    ("contradict", "Advanced", "verb", "to deny truth of"),
    ("contravene", "Advanced", "verb", "to violate or conflict"),
    ("contrite", "Advanced", "adjective", "feeling remorse"),
    ("contrived", "Advanced", "adjective", "deliberately created"),
    ("controversial", "Advanced", "adjective", "giving rise to disagreement"),
    ("controvert", "Expert", "verb", "to deny truth of"),
    ("contumacious", "Expert", "adjective", "stubbornly disobedient"),
    ("conundrum", "Advanced", "noun", "confusing problem"),
    ("convene", "Advanced", "verb", "to come together"),
    ("conventional", "Advanced", "adjective", "based on accepted use"),
    ("converge", "Advanced", "verb", "to come together"),
    ("conversant", "Advanced", "adjective", "familiar with"),
    ("converse", "Advanced", "adjective", "opposite or contrary"),
    ("conviction", "Advanced", "noun", "firmly held belief"),
    ("convivial", "Advanced", "adjective", "friendly and lively"),
    ("convoluted", "Advanced", "adjective", "extremely complex"),
    ("copious", "Advanced", "adjective", "abundant in supply"),
    ("cordial", "Advanced", "adjective", "warm and friendly"),
    ("corollary", "Advanced", "noun", "proposition following from another"),
    ("corroborate", "Advanced", "verb", "to confirm or support"),
    ("cosmopolitan", "Advanced", "adjective", "familiar with many cultures"),
    ("countenance", "Advanced", "noun", "person's face or expression"),
    ("counteract", "Advanced", "verb", "to act against"),
    ("counterfeit", "Advanced", "adjective", "made to imitate"),
    ("countermand", "Expert", "verb", "to revoke order"),
    ("counterpart", "Advanced", "noun", "person corresponding to another"),
    ("coup", "Advanced", "noun", "sudden seizure of power"),
    ("covenant", "Advanced", "noun", "agreement or contract"),
    ("covert", "Advanced", "adjective", "not openly displayed"),
    ("covet", "Advanced", "verb", "to yearn to possess"),
    ("cower", "Advanced", "verb", "to crouch in fear"),
    ("craft", "Advanced", "noun", "activity involving skill"),
    ("crafty", "Advanced", "adjective", "clever at achieving aims"),
    ("crass", "Advanced", "adjective", "lacking sensitivity"),
    ("crave", "Advanced", "verb", "to feel powerful desire"),
    ("credence", "Advanced", "noun", "belief in something"),
    ("credible", "Advanced", "adjective", "able to be believed"),
    ("credulous", "Advanced", "adjective", "having tendency to believe"),
    ("creed", "Advanced", "noun", "system of beliefs"),
    ("crestfallen", "Advanced", "adjective", "sad and disappointed"),
    ("criterion", "Advanced", "noun", "standard for judging"),
    ("critique", "Advanced", "noun", "detailed analysis"),
    ("cronyism", "Advanced", "noun", "favoritism to friends"),
    ("crucial", "Advanced", "adjective", "of great importance"),
    ("cryptic", "Advanced", "adjective", "having hidden meaning"),
    ("culpable", "Advanced", "adjective", "deserving blame"),
    ("cultivate", "Advanced", "verb", "to try to acquire"),
    ("cumbersome", "Advanced", "adjective", "large or heavy"),
    ("cumulative", "Advanced", "adjective", "increasing by addition"),
    ("cunning", "Advanced", "adjective", "having skill in deception"),
    ("cupidity", "Expert", "noun", "greed for money"),
    ("curmudgeon", "Advanced", "noun", "bad-tempered person"),
    ("cursory", "Advanced", "adjective", "hasty and superficial"),
    ("curtail", "Advanced", "verb", "to reduce in extent"),
    ("cynical", "Advanced", "adjective", "distrustful of human sincerity"),
    ("daunt", "Advanced", "verb", "to make feel intimidated"),
    ("dearth", "Advanced", "noun", "scarcity or lack"),
    ("debacle", "Advanced", "noun", "sudden disastrous failure"),
    ("debase", "Advanced", "verb", "to reduce in quality"),
    ("debilitate", "Advanced", "verb", "to make very weak"),
    ("debunk", "Advanced", "verb", "to expose falseness of"),
    ("decadent", "Advanced", "adjective", "characterized by moral decline"),
    ("decimate", "Advanced", "verb", "to kill large proportion"),
    ("decipher", "Advanced", "verb", "to convert into normal language"),
    ("decisive", "Advanced", "adjective", "settling issue conclusively"),
    ("declaim", "Expert", "verb", "to speak in rhetorical way"),
    ("decline", "Advanced", "verb", "to become smaller"),
    ("decorous", "Expert", "adjective", "in keeping with good taste"),
    ("decorum", "Advanced", "noun", "behavior in keeping with good taste"),
    ("decoy", "Advanced", "noun", "thing used to mislead"),
    ("decree", "Advanced", "noun", "official order"),
    ("decrepit", "Advanced", "adjective", "worn out by age"),
    ("decry", "Advanced", "verb", "to publicly denounce"),
    ("deduce", "Advanced", "verb", "to arrive at by reasoning"),
    ("deem", "Advanced", "verb", "to regard as"),
    ("defamatory", "Advanced", "adjective", "damaging to reputation"),
    ("default", "Advanced", "noun", "failure to fulfill obligation"),
    ("defect", "Advanced", "noun", "shortcoming or imperfection"),
    ("defer", "Advanced", "verb", "to put off to later time"),
    ("deference", "Advanced", "noun", "humble submission"),
    ("defiant", "Advanced", "adjective", "showing resistance"),
    ("deficient", "Advanced", "adjective", "not having enough"),
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
    start_id = 701
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"{i+1}/{len(GRE_WORDS)}: {word}")
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"The situation demanded a {word} response.",
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch10.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
