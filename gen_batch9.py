import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("cede", "Advanced", "verb", "to give up power or territory"),
    ("censure", "Advanced", "verb", "to express severe disapproval"),
    ("cerebral", "Advanced", "adjective", "intellectual rather than emotional"),
    ("certitude", "Advanced", "noun", "absolute certainty"),
    ("chagrin", "Advanced", "noun", "distress caused by humiliation"),
    ("champion", "Advanced", "verb", "to support cause vigorously"),
    ("chaotic", "Advanced", "adjective", "in state of disorder"),
    ("charlatan", "Advanced", "noun", "person falsely claiming expertise"),
    ("chary", "Expert", "adjective", "cautious about something"),
    ("chastise", "Advanced", "verb", "to rebuke severely"),
    ("chicanery", "Expert", "noun", "use of trickery"),
    ("chide", "Advanced", "verb", "to scold or rebuke"),
    ("chimera", "Expert", "noun", "thing hoped for but illusory"),
    ("choleric", "Expert", "adjective", "bad-tempered or irritable"),
    ("chronicle", "Advanced", "noun", "factual account of events"),
    ("circuitous", "Advanced", "adjective", "longer than most direct way"),
    ("circumlocution", "Expert", "noun", "use of many words"),
    ("circumscribe", "Advanced", "verb", "to restrict or limit"),
    ("circumspect", "Advanced", "adjective", "wary and unwilling to take risks"),
    ("circumvent", "Advanced", "verb", "to find way around"),
    ("citadel", "Advanced", "noun", "fortress protecting city"),
    ("cite", "Advanced", "verb", "to quote as evidence"),
    ("clairvoyant", "Advanced", "noun", "person claiming supernatural insight"),
    ("clamor", "Advanced", "noun", "loud and confused noise"),
    ("clandestine", "Advanced", "adjective", "kept secret"),
    ("clemency", "Advanced", "noun", "mercy or leniency"),
    ("cliche", "Advanced", "noun", "overused phrase"),
    ("clientele", "Advanced", "noun", "clients collectively"),
    ("climactic", "Advanced", "adjective", "relating to climax"),
    ("clique", "Advanced", "noun", "exclusive group of people"),
    ("clout", "Advanced", "noun", "influence or power"),
    ("coalesce", "Advanced", "verb", "to come together to form one"),
    ("codify", "Advanced", "verb", "to arrange into systematic code"),
    ("coerce", "Advanced", "verb", "to persuade by force"),
    ("cogent", "Advanced", "adjective", "clear and convincing"),
    ("cognizant", "Advanced", "adjective", "having knowledge or awareness"),
    ("coherent", "Advanced", "adjective", "logical and consistent"),
    ("cohesive", "Advanced", "adjective", "forming united whole"),
    ("coincide", "Advanced", "verb", "to occur at same time"),
    ("collaborate", "Advanced", "verb", "to work jointly"),
    ("collateral", "Advanced", "adjective", "additional but subordinate"),
    ("colloquial", "Advanced", "adjective", "used in ordinary conversation"),
    ("collusion", "Advanced", "noun", "secret agreement for fraud"),
    ("colossal", "Advanced", "adjective", "extremely large"),
    ("combustible", "Advanced", "adjective", "able to catch fire"),
    ("comely", "Expert", "adjective", "pleasant to look at"),
    ("commend", "Advanced", "verb", "to praise formally"),
    ("commensurate", "Advanced", "adjective", "corresponding in size"),
    ("commodity", "Advanced", "noun", "raw material for trade"),
    ("communal", "Advanced", "adjective", "shared by all members"),
    ("compelling", "Advanced", "adjective", "evoking interest or attention"),
    ("compendium", "Advanced", "noun", "collection of concise information"),
    ("compensate", "Advanced", "verb", "to give something to reduce effect"),
    ("competent", "Advanced", "adjective", "having necessary ability"),
    ("complacent", "Advanced", "adjective", "smugly self-satisfied"),
    ("complement", "Advanced", "verb", "to add to enhance"),
    ("compliance", "Advanced", "noun", "action of complying"),
    ("compliant", "Advanced", "adjective", "inclined to agree"),
    ("complicity", "Advanced", "noun", "state of being involved"),
    ("composed", "Advanced", "adjective", "having feelings in control"),
    ("compound", "Advanced", "verb", "to make worse"),
    ("comprehensive", "Advanced", "adjective", "complete and including all"),
    ("comprise", "Advanced", "verb", "to consist of"),
    ("compromise", "Advanced", "verb", "to settle by mutual concession"),
    ("compunction", "Advanced", "noun", "feeling of guilt"),
    ("concede", "Advanced", "verb", "to admit that something is true"),
    ("conceit", "Advanced", "noun", "excessive pride"),
    ("concerted", "Advanced", "adjective", "jointly arranged"),
    ("conciliatory", "Advanced", "adjective", "intended to placate"),
    ("concise", "Advanced", "adjective", "giving information clearly"),
    ("conclusive", "Advanced", "adjective", "putting end to doubt"),
    ("concoct", "Advanced", "verb", "to create by mixing"),
    ("concomitant", "Expert", "adjective", "naturally accompanying"),
    ("concrete", "Advanced", "adjective", "existing in material form"),
    ("concur", "Advanced", "verb", "to be of same opinion"),
    ("condemn", "Advanced", "verb", "to express disapproval"),
    ("condescend", "Advanced", "verb", "to show superiority"),
    ("condone", "Advanced", "verb", "to accept behavior"),
    ("conducive", "Advanced", "adjective", "making likely to happen"),
    ("confide", "Advanced", "verb", "to tell someone secret"),
    ("configuration", "Advanced", "noun", "arrangement of parts"),
    ("confine", "Advanced", "verb", "to keep within limits"),
    ("conflagration", "Expert", "noun", "extensive fire"),
    ("conflate", "Advanced", "verb", "to combine into one"),
    ("confluence", "Advanced", "noun", "junction of two rivers"),
    ("conform", "Advanced", "verb", "to comply with rules"),
    ("confound", "Advanced", "verb", "to cause surprise"),
    ("congenial", "Advanced", "adjective", "pleasant because of similar interests"),
    ("congenital", "Advanced", "adjective", "present from birth"),
    ("conglomerate", "Advanced", "noun", "corporation formed by merger"),
    ("conjecture", "Advanced", "noun", "opinion based on incomplete information"),
    ("conjure", "Advanced", "verb", "to make appear by magic"),
    ("connive", "Advanced", "verb", "to secretly allow wrongdoing"),
    ("connoisseur", "Advanced", "noun", "expert judge of art"),
    ("conscientious", "Advanced", "adjective", "wishing to do what is right"),
    ("consecrate", "Advanced", "verb", "to make sacred"),
    ("consensus", "Advanced", "noun", "general agreement"),
    ("consequential", "Advanced", "adjective", "important or significant"),
    ("conserve", "Advanced", "verb", "to protect from harm"),
    ("considerable", "Advanced", "adjective", "notably large"),
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
    start_id = 601
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"{i+1}/{len(GRE_WORDS)}: {word}")
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"The expert showed a {word} approach to the problem.",
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch9.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
