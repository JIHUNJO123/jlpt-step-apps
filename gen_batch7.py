import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("abstemious", "Expert", "adjective", "not self-indulgent in eating"),
    ("accede", "Advanced", "verb", "to agree to a demand"),
    ("accolade", "Advanced", "noun", "award or privilege"),
    ("accost", "Advanced", "verb", "to approach and address boldly"),
    ("accretion", "Expert", "noun", "growth by gradual accumulation"),
    ("acumen", "Advanced", "noun", "ability to make good judgments"),
    ("adjudicate", "Advanced", "verb", "to make formal judgment"),
    ("admonish", "Advanced", "verb", "to warn or reprimand"),
    ("adroit", "Advanced", "adjective", "clever or skillful"),
    ("adulation", "Advanced", "noun", "excessive admiration"),
    ("adversarial", "Advanced", "adjective", "involving conflict"),
    ("advocate", "Advanced", "verb", "to publicly support"),
    ("aesthetic", "Advanced", "adjective", "concerned with beauty"),
    ("affable", "Advanced", "adjective", "friendly and good-natured"),
    ("affected", "Advanced", "adjective", "artificial and pretentious"),
    ("affinity", "Advanced", "noun", "natural liking for something"),
    ("affluent", "Advanced", "adjective", "having great wealth"),
    ("aggrandize", "Advanced", "verb", "to increase power or status"),
    ("aggregate", "Advanced", "noun", "whole formed by combining"),
    ("aggrieved", "Advanced", "adjective", "feeling resentment"),
    ("agnostic", "Advanced", "noun", "person uncertain about existence"),
    ("alacrity", "Advanced", "noun", "brisk and cheerful readiness"),
    ("albeit", "Advanced", "conjunction", "although"),
    ("alchemy", "Advanced", "noun", "seemingly magical transformation"),
    ("alienate", "Advanced", "verb", "to cause to feel isolated"),
    ("allay", "Advanced", "verb", "to diminish fear or concern"),
    ("allege", "Advanced", "verb", "to claim without proof"),
    ("allocate", "Advanced", "verb", "to distribute for purpose"),
    ("allure", "Advanced", "noun", "quality of being attractive"),
    ("aloof", "Advanced", "adjective", "not friendly or forthcoming"),
    ("altruistic", "Advanced", "adjective", "showing unselfish concern"),
    ("amalgamate", "Advanced", "verb", "to combine into unified whole"),
    ("ambiguous", "Advanced", "adjective", "open to more than one interpretation"),
    ("ambivalent", "Advanced", "adjective", "having mixed feelings"),
    ("ameliorate", "Advanced", "verb", "to make something better"),
    ("amenable", "Advanced", "adjective", "open to suggestion"),
    ("amiable", "Advanced", "adjective", "friendly and pleasant"),
    ("amicable", "Advanced", "adjective", "characterized by friendliness"),
    ("amorphous", "Advanced", "adjective", "without clear shape"),
    ("ample", "Advanced", "adjective", "enough or more than enough"),
    ("anachronistic", "Advanced", "adjective", "belonging to different period"),
    ("analogous", "Advanced", "adjective", "comparable in certain respects"),
    ("anarchy", "Advanced", "noun", "state of disorder"),
    ("anathema", "Advanced", "noun", "something greatly disliked"),
    ("ancillary", "Advanced", "adjective", "providing support"),
    ("animosity", "Advanced", "noun", "strong hostility"),
    ("annotate", "Advanced", "verb", "to add notes of explanation"),
    ("anomalous", "Advanced", "adjective", "deviating from standard"),
    ("antagonize", "Advanced", "verb", "to cause hostility"),
    ("antecedent", "Advanced", "noun", "thing that existed before"),
    ("anthology", "Advanced", "noun", "collection of literary works"),
    ("anthropomorphic", "Expert", "adjective", "attributing human form"),
    ("anticipate", "Advanced", "verb", "to regard as probable"),
    ("antidote", "Advanced", "noun", "medicine to counteract poison"),
    ("antiquated", "Advanced", "adjective", "old-fashioned or outdated"),
    ("antithesis", "Advanced", "noun", "direct opposite"),
    ("apathetic", "Advanced", "adjective", "showing no interest"),
    ("apex", "Advanced", "noun", "highest point"),
    ("aplomb", "Advanced", "noun", "self-confidence in difficult situation"),
    ("apocalyptic", "Advanced", "adjective", "describing total destruction"),
    ("apologist", "Advanced", "noun", "person who defends something"),
    ("apostate", "Expert", "noun", "person who renounces belief"),
    ("appease", "Advanced", "verb", "to pacify by giving in"),
    ("apprehensive", "Advanced", "adjective", "anxious about future"),
    ("apprise", "Advanced", "verb", "to inform or tell"),
    ("approbation", "Advanced", "noun", "approval or praise"),
    ("appropriate", "Advanced", "verb", "to take for one's own use"),
    ("arbiter", "Advanced", "noun", "person with power to decide"),
    ("arbitrary", "Advanced", "adjective", "based on random choice"),
    ("arcane", "Advanced", "adjective", "understood by few"),
    ("archaic", "Advanced", "adjective", "very old or old-fashioned"),
    ("archetype", "Advanced", "noun", "very typical example"),
    ("ardent", "Advanced", "adjective", "enthusiastic or passionate"),
    ("arduous", "Advanced", "adjective", "involving strenuous effort"),
    ("articulate", "Advanced", "adjective", "fluent and coherent"),
    ("artifact", "Advanced", "noun", "object made by human being"),
    ("artifice", "Advanced", "noun", "clever device or expedient"),
    ("ascendancy", "Advanced", "noun", "occupation of dominant position"),
    ("ascertain", "Advanced", "verb", "to find out for certain"),
    ("ascetic", "Advanced", "adjective", "characterized by self-discipline"),
    ("aspersion", "Expert", "noun", "attack on reputation"),
    ("assail", "Advanced", "verb", "to make concerted attack"),
    ("assert", "Advanced", "verb", "to state fact confidently"),
    ("assessment", "Advanced", "noun", "evaluation or estimation"),
    ("assiduous", "Advanced", "adjective", "showing great care"),
    ("assuage", "Advanced", "verb", "to make unpleasant feeling less"),
    ("astute", "Advanced", "adjective", "having sharp judgment"),
    ("atrophy", "Advanced", "verb", "to gradually decline"),
    ("attenuate", "Advanced", "verb", "to reduce in force"),
    ("attribute", "Advanced", "verb", "to regard as caused by"),
    ("audacious", "Advanced", "adjective", "showing willingness to take risks"),
    ("augment", "Advanced", "verb", "to make greater"),
    ("auspicious", "Advanced", "adjective", "favorable or promising"),
    ("austere", "Advanced", "adjective", "severe or strict"),
    ("authenticate", "Advanced", "verb", "to prove or validate"),
    ("authoritative", "Advanced", "adjective", "commanding and confident"),
    ("autocratic", "Advanced", "adjective", "taking no account of others"),
    ("autonomous", "Advanced", "adjective", "having self-government"),
    ("avarice", "Advanced", "noun", "extreme greed for wealth"),
    ("averse", "Advanced", "adjective", "having strong dislike"),
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
    start_id = 401
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"{i+1}/{len(GRE_WORDS)}: {word}")
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"The scholar demonstrated {word} behavior in the research.",
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch7.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
