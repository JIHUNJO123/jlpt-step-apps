import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("protean", "Expert", "adjective", "tending to change frequently"),
    ("protocol", "Advanced", "noun", "official procedure"),
    ("prototype", "Advanced", "noun", "first model of something"),
    ("protract", "Advanced", "verb", "to prolong"),
    ("protrude", "Advanced", "verb", "to extend beyond"),
    ("provenance", "Advanced", "noun", "place of origin"),
    ("provident", "Expert", "adjective", "making provision for future"),
    ("provincial", "Advanced", "adjective", "of a province"),
    ("provisional", "Advanced", "adjective", "arranged temporarily"),
    ("proviso", "Advanced", "noun", "condition attached to agreement"),
    ("provocative", "Advanced", "adjective", "causing annoyance"),
    ("prowess", "Advanced", "noun", "skill or expertise"),
    ("proximity", "Advanced", "noun", "nearness in space"),
    ("proxy", "Advanced", "noun", "authority to represent another"),
    ("prudent", "Advanced", "adjective", "acting with care"),
    ("prune", "Advanced", "verb", "to trim by cutting"),
    ("puerile", "Expert", "adjective", "childishly silly"),
    ("pugnacious", "Advanced", "adjective", "eager to argue"),
    ("pulverize", "Advanced", "verb", "to reduce to fine particles"),
    ("punctilious", "Expert", "adjective", "showing great attention to detail"),
    ("pundit", "Advanced", "noun", "expert in particular subject"),
    ("pungent", "Advanced", "adjective", "having sharp taste"),
    ("punitive", "Advanced", "adjective", "inflicting punishment"),
    ("purge", "Advanced", "verb", "to rid of unwanted quality"),
    ("puritanical", "Advanced", "adjective", "having strict moral beliefs"),
    ("purport", "Advanced", "verb", "to appear to be"),
    ("pursuant", "Advanced", "adjective", "in accordance with"),
    ("pusillanimous", "Expert", "adjective", "showing lack of courage"),
    ("quagmire", "Advanced", "noun", "soft boggy area"),
    ("quaint", "Advanced", "adjective", "attractively unusual"),
    ("qualify", "Advanced", "verb", "to make less absolute"),
    ("qualm", "Advanced", "noun", "uneasy feeling of doubt"),
    ("quandary", "Advanced", "noun", "state of perplexity"),
    ("quarantine", "Advanced", "noun", "state of isolation"),
    ("quarrelsome", "Advanced", "adjective", "given to quarreling"),
    ("quash", "Advanced", "verb", "to reject as invalid"),
    ("quell", "Advanced", "verb", "to put end to"),
    ("querulous", "Expert", "adjective", "complaining in petulant way"),
    ("query", "Advanced", "noun", "question about something"),
    ("quest", "Advanced", "noun", "long search for something"),
    ("quibble", "Advanced", "verb", "to argue about trivial matter"),
    ("quiescent", "Expert", "adjective", "in state of inactivity"),
    ("quintessential", "Advanced", "adjective", "representing perfect example"),
    ("quip", "Advanced", "noun", "witty remark"),
    ("quirky", "Advanced", "adjective", "characterized by peculiar traits"),
    ("quixotic", "Expert", "adjective", "exceedingly idealistic"),
    ("quotidian", "Expert", "adjective", "of or occurring every day"),
    ("rabid", "Advanced", "adjective", "having fanatical belief"),
    ("radical", "Advanced", "adjective", "relating to fundamental nature"),
    ("raffle", "Advanced", "noun", "means of raising money"),
    ("rampant", "Advanced", "adjective", "flourishing without check"),
    ("ramshackle", "Advanced", "adjective", "in severe state of disrepair"),
    ("rancor", "Advanced", "noun", "bitterness or resentfulness"),
    ("random", "Advanced", "adjective", "made without method"),
    ("rankle", "Advanced", "verb", "to cause annoyance"),
    ("rant", "Advanced", "verb", "to speak at length angrily"),
    ("rapacious", "Expert", "adjective", "aggressively greedy"),
    ("rapport", "Advanced", "noun", "close harmonious relationship"),
    ("rapt", "Advanced", "adjective", "completely fascinated"),
    ("rapture", "Advanced", "noun", "feeling of intense pleasure"),
    ("rarefied", "Advanced", "adjective", "distant from ordinary people"),
    ("rash", "Advanced", "adjective", "acting without thinking"),
    ("ratify", "Advanced", "verb", "to give formal consent"),
    ("ratiocination", "Expert", "noun", "process of logical reasoning"),
    ("rational", "Advanced", "adjective", "based on reason"),
    ("rationale", "Advanced", "noun", "set of reasons"),
    ("raucous", "Advanced", "adjective", "making harsh sound"),
    ("ravage", "Advanced", "verb", "to cause severe damage"),
    ("ravenous", "Advanced", "adjective", "extremely hungry"),
    ("raze", "Advanced", "verb", "to completely destroy"),
    ("reactionary", "Advanced", "adjective", "opposing political change"),
    ("realm", "Advanced", "noun", "kingdom or field"),
    ("rebuff", "Advanced", "verb", "to reject ungraciously"),
    ("rebuke", "Advanced", "verb", "to express sharp disapproval"),
    ("rebut", "Advanced", "verb", "to claim to be false"),
    ("recalcitrant", "Advanced", "adjective", "stubbornly uncooperative"),
    ("recant", "Advanced", "verb", "to say that former belief was wrong"),
    ("recapitulate", "Advanced", "verb", "to summarize main points"),
    ("recede", "Advanced", "verb", "to go back or away"),
    ("receptive", "Advanced", "adjective", "willing to consider ideas"),
    ("recession", "Advanced", "noun", "period of economic decline"),
    ("recidivism", "Expert", "noun", "tendency to relapse"),
    ("reciprocate", "Advanced", "verb", "to respond with similar action"),
    ("reclusive", "Advanced", "adjective", "avoiding company"),
    ("reconcile", "Advanced", "verb", "to restore friendly relations"),
    ("recondite", "Expert", "adjective", "obscure"),
    ("reconnaissance", "Advanced", "noun", "military observation"),
    ("rectify", "Advanced", "verb", "to put right"),
    ("rectitude", "Expert", "noun", "morally correct behavior"),
    ("recumbent", "Expert", "adjective", "lying down"),
    ("recuperate", "Advanced", "verb", "to recover from illness"),
    ("recurrent", "Advanced", "adjective", "occurring often"),
    ("redolent", "Expert", "adjective", "strongly reminiscent"),
    ("redoubtable", "Expert", "adjective", "formidable"),
    ("redress", "Advanced", "verb", "to remedy or set right"),
    ("redundant", "Advanced", "adjective", "not needed"),
    ("refine", "Advanced", "verb", "to remove impurities"),
    ("reflect", "Advanced", "verb", "to think deeply"),
    ("refractory", "Expert", "adjective", "stubborn or unmanageable"),
    ("refute", "Advanced", "verb", "to prove to be wrong"),
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
    start_id = 2401
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch27.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
