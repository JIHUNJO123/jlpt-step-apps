import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("disconcert", "Advanced", "verb", "to disturb composure"),
    ("discord", "Advanced", "noun", "disagreement between people"),
    ("discordant", "Advanced", "adjective", "disagreeing or incongruous"),
    ("discount", "Advanced", "verb", "to disregard as unimportant"),
    ("discourse", "Advanced", "noun", "written or spoken communication"),
    ("discredit", "Advanced", "verb", "to harm reputation"),
    ("discreet", "Advanced", "adjective", "careful and circumspect"),
    ("discrepancy", "Advanced", "noun", "lack of compatibility"),
    ("discrete", "Advanced", "adjective", "individually separate"),
    ("discretion", "Advanced", "noun", "quality of behaving prudently"),
    ("discriminate", "Advanced", "verb", "to recognize distinction"),
    ("discursive", "Expert", "adjective", "digressing from subject"),
    ("disdain", "Advanced", "noun", "feeling of contempt"),
    ("disenchanted", "Advanced", "adjective", "disappointed"),
    ("disenfranchise", "Advanced", "verb", "to deprive of right"),
    ("disengage", "Advanced", "verb", "to separate or release"),
    ("disfigure", "Advanced", "verb", "to spoil appearance"),
    ("disgorge", "Expert", "verb", "to pour forth"),
    ("disgrace", "Advanced", "noun", "loss of reputation"),
    ("disguise", "Advanced", "verb", "to alter appearance"),
    ("dishearten", "Advanced", "verb", "to cause to lose determination"),
    ("disheveled", "Advanced", "adjective", "untidy in appearance"),
    ("disillusioned", "Advanced", "adjective", "disappointed in someone"),
    ("disinclination", "Advanced", "noun", "reluctance or unwillingness"),
    ("disingenuous", "Advanced", "adjective", "not candid or sincere"),
    ("disintegrate", "Advanced", "verb", "to break into small parts"),
    ("disinterested", "Advanced", "adjective", "not influenced by considerations"),
    ("disjointed", "Advanced", "adjective", "lacking coherent sequence"),
    ("dismiss", "Advanced", "verb", "to order to leave"),
    ("dismissive", "Advanced", "adjective", "feeling that something is unworthy"),
    ("disparage", "Advanced", "verb", "to regard as being of little worth"),
    ("disparate", "Advanced", "adjective", "essentially different"),
    ("disparity", "Advanced", "noun", "great difference"),
    ("dispassionate", "Advanced", "adjective", "not influenced by emotion"),
    ("dispatch", "Advanced", "verb", "to send off to destination"),
    ("dispel", "Advanced", "verb", "to make disappear"),
    ("dispensation", "Advanced", "noun", "exemption from rule"),
    ("dispense", "Advanced", "verb", "to distribute or provide"),
    ("disperse", "Advanced", "verb", "to distribute over wide area"),
    ("displace", "Advanced", "verb", "to take over position"),
    ("disposition", "Advanced", "noun", "person's inherent qualities"),
    ("dispossess", "Advanced", "verb", "to deprive of land"),
    ("disproportionate", "Advanced", "adjective", "too large or small"),
    ("disprove", "Advanced", "verb", "to prove that something is false"),
    ("dispute", "Advanced", "noun", "disagreement or argument"),
    ("disquiet", "Advanced", "noun", "feeling of anxiety"),
    ("disregard", "Advanced", "verb", "to pay no attention to"),
    ("disreputable", "Advanced", "adjective", "not respectable"),
    ("disrepute", "Advanced", "noun", "state of being held in low esteem"),
    ("disrupt", "Advanced", "verb", "to interrupt by causing disturbance"),
    ("dissect", "Advanced", "verb", "to cut up methodically"),
    ("dissemble", "Advanced", "verb", "to conceal one's true motives"),
    ("disseminate", "Advanced", "verb", "to spread widely"),
    ("dissension", "Advanced", "noun", "disagreement that leads to discord"),
    ("dissent", "Advanced", "noun", "holding of different opinion"),
    ("dissertation", "Advanced", "noun", "long essay on subject"),
    ("disservice", "Advanced", "noun", "harmful action"),
    ("dissident", "Advanced", "noun", "person opposing official policy"),
    ("dissipate", "Advanced", "verb", "to dispel or disperse"),
    ("dissociate", "Advanced", "verb", "to disconnect or separate"),
    ("dissolute", "Expert", "adjective", "lacking moral restraint"),
    ("dissolution", "Advanced", "noun", "act of dissolving"),
    ("dissonance", "Advanced", "noun", "lack of harmony"),
    ("dissuade", "Advanced", "verb", "to persuade not to"),
    ("distant", "Advanced", "adjective", "far away in space"),
    ("distend", "Advanced", "verb", "to swell by pressure"),
    ("distill", "Advanced", "verb", "to extract essential meaning"),
    ("distinct", "Advanced", "adjective", "recognizably different"),
    ("distinction", "Advanced", "noun", "difference or contrast"),
    ("distinctive", "Advanced", "adjective", "characteristic of one person"),
    ("distinguish", "Advanced", "verb", "to recognize as different"),
    ("distort", "Advanced", "verb", "to pull out of shape"),
    ("distract", "Advanced", "verb", "to prevent from giving attention"),
    ("distraught", "Advanced", "adjective", "deeply upset and agitated"),
    ("diverge", "Advanced", "verb", "to separate from route"),
    ("divergent", "Advanced", "adjective", "tending to be different"),
    ("diverse", "Advanced", "adjective", "showing variety"),
    ("diversion", "Advanced", "noun", "instance of turning aside"),
    ("divest", "Advanced", "verb", "to deprive of power"),
    ("divine", "Advanced", "adjective", "of or from god"),
    ("divisive", "Advanced", "adjective", "tending to cause disagreement"),
    ("divulge", "Advanced", "verb", "to make known"),
    ("docile", "Advanced", "adjective", "ready to accept control"),
    ("doctrine", "Advanced", "noun", "belief or set of beliefs"),
    ("document", "Advanced", "verb", "to record in written form"),
    ("dodgy", "Advanced", "adjective", "dishonest or unreliable"),
    ("dogma", "Advanced", "noun", "principle laid down by authority"),
    ("dogmatic", "Advanced", "adjective", "inclined to lay down principles"),
    ("doldrums", "Advanced", "noun", "state of inactivity"),
    ("doleful", "Expert", "adjective", "expressing sorrow"),
    ("domain", "Advanced", "noun", "area of territory"),
    ("dominate", "Advanced", "verb", "to have commanding influence"),
    ("domineer", "Advanced", "verb", "to assert one's will"),
    ("dormant", "Advanced", "adjective", "temporarily inactive"),
    ("dote", "Advanced", "verb", "to be extremely fond"),
    ("dour", "Advanced", "adjective", "relentlessly severe"),
    ("draconian", "Advanced", "adjective", "excessively harsh"),
    ("drawback", "Advanced", "noun", "disadvantage or problem"),
    ("dread", "Advanced", "noun", "great fear or apprehension"),
    ("dreary", "Advanced", "adjective", "dull and depressing"),
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
    start_id = 901
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"{i+1}/{len(GRE_WORDS)}: {word}")
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"The {word} approach led to unexpected results.",
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch12.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
