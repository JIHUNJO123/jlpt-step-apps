import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("impenetrable", "Advanced", "adjective", "impossible to pass through"),
    ("impenitent", "Expert", "adjective", "not feeling shame"),
    ("imperative", "Advanced", "adjective", "of vital importance"),
    ("imperceptible", "Advanced", "adjective", "impossible to perceive"),
    ("imperial", "Advanced", "adjective", "relating to empire"),
    ("imperious", "Advanced", "adjective", "assuming power"),
    ("impermeable", "Advanced", "adjective", "not allowing fluid to pass"),
    ("impersonal", "Advanced", "adjective", "not influenced by feelings"),
    ("impersonate", "Advanced", "verb", "to pretend to be another"),
    ("impertinent", "Advanced", "adjective", "not showing proper respect"),
    ("imperturbable", "Advanced", "adjective", "unable to be upset"),
    ("impervious", "Advanced", "adjective", "not allowing entrance"),
    ("impetuous", "Advanced", "adjective", "acting quickly without thought"),
    ("impetus", "Advanced", "noun", "force that makes something happen"),
    ("impiety", "Expert", "noun", "lack of piety"),
    ("impinge", "Advanced", "verb", "to have effect on"),
    ("impious", "Expert", "adjective", "not showing respect for god"),
    ("implacable", "Advanced", "adjective", "unable to be placated"),
    ("implausible", "Advanced", "adjective", "not seeming reasonable"),
    ("implement", "Advanced", "verb", "to put into effect"),
    ("implicate", "Advanced", "verb", "to show to be involved"),
    ("implication", "Advanced", "noun", "conclusion that can be drawn"),
    ("implicit", "Advanced", "adjective", "implied though not stated"),
    ("implore", "Advanced", "verb", "to beg earnestly"),
    ("imply", "Advanced", "verb", "to strongly suggest"),
    ("impolitic", "Expert", "adjective", "failing to be wise"),
    ("import", "Advanced", "noun", "meaning or significance"),
    ("importune", "Expert", "verb", "to harass with requests"),
    ("impose", "Advanced", "verb", "to force to be accepted"),
    ("imposing", "Advanced", "adjective", "grand and impressive"),
    ("impotent", "Advanced", "adjective", "unable to take effective action"),
    ("impoverish", "Advanced", "verb", "to make poor"),
    ("impractical", "Advanced", "adjective", "not adapted for use"),
    ("imprecise", "Advanced", "adjective", "lacking exactness"),
    ("impregnable", "Advanced", "adjective", "unable to be captured"),
    ("impress", "Advanced", "verb", "to make feel admiration"),
    ("impressionable", "Advanced", "adjective", "easily influenced"),
    ("impromptu", "Advanced", "adjective", "done without preparation"),
    ("improper", "Advanced", "adjective", "not in accordance with rules"),
    ("improvident", "Expert", "adjective", "not providing for future"),
    ("improvise", "Advanced", "verb", "to create without preparation"),
    ("imprudent", "Advanced", "adjective", "not showing care"),
    ("impudent", "Advanced", "adjective", "not showing due respect"),
    ("impugn", "Advanced", "verb", "to dispute validity of"),
    ("impulsive", "Advanced", "adjective", "acting without forethought"),
    ("impunity", "Advanced", "noun", "exemption from punishment"),
    ("impute", "Advanced", "verb", "to attribute to cause"),
    ("inadvertent", "Advanced", "adjective", "not resulting from attention"),
    ("inalienable", "Advanced", "adjective", "unable to be taken away"),
    ("inane", "Advanced", "adjective", "silly and pointless"),
    ("inanimate", "Advanced", "adjective", "not alive"),
    ("inarticulate", "Advanced", "adjective", "unable to speak distinctly"),
    ("inaugurate", "Advanced", "verb", "to begin or introduce"),
    ("incandescent", "Advanced", "adjective", "emitting light when heated"),
    ("incantation", "Advanced", "noun", "series of words said as spell"),
    ("incapacitate", "Advanced", "verb", "to prevent from functioning"),
    ("incarcerate", "Advanced", "verb", "to imprison"),
    ("incarnate", "Advanced", "adjective", "embodied in flesh"),
    ("incendiary", "Advanced", "adjective", "tending to cause fires"),
    ("incense", "Advanced", "verb", "to make very angry"),
    ("incentive", "Advanced", "noun", "thing that motivates"),
    ("inception", "Advanced", "noun", "establishment or starting point"),
    ("incessant", "Advanced", "adjective", "continuing without pause"),
    ("inchoate", "Expert", "adjective", "just begun and undeveloped"),
    ("incidence", "Advanced", "noun", "occurrence or rate of occurrence"),
    ("incidental", "Advanced", "adjective", "accompanying but not major part"),
    ("incipient", "Expert", "adjective", "in initial stage"),
    ("incisive", "Advanced", "adjective", "intelligently analytical"),
    ("incite", "Advanced", "verb", "to encourage unlawful behavior"),
    ("inclement", "Advanced", "adjective", "unpleasantly cold or wet"),
    ("inclination", "Advanced", "noun", "tendency to act in particular way"),
    ("inclusive", "Advanced", "adjective", "including all services"),
    ("incoherent", "Advanced", "adjective", "expressed in incomprehensible way"),
    ("incompatible", "Advanced", "adjective", "unable to exist together"),
    ("incompetent", "Advanced", "adjective", "not having necessary skills"),
    ("inconclusive", "Advanced", "adjective", "not leading to firm conclusion"),
    ("incongruous", "Advanced", "adjective", "not in harmony"),
    ("inconsequential", "Advanced", "adjective", "not important"),
    ("inconsistent", "Advanced", "adjective", "not staying the same"),
    ("incontrovertible", "Advanced", "adjective", "not able to be denied"),
    ("incorporate", "Advanced", "verb", "to take in or contain"),
    ("incorrigible", "Advanced", "adjective", "not able to be corrected"),
    ("incredulous", "Advanced", "adjective", "unwilling to believe"),
    ("increment", "Advanced", "noun", "increase or addition"),
    ("incriminate", "Advanced", "verb", "to make appear guilty"),
    ("incumbent", "Advanced", "adjective", "necessary as duty"),
    ("incur", "Advanced", "verb", "to become subject to"),
    ("incursion", "Advanced", "noun", "invasion or attack"),
    ("indebted", "Advanced", "adjective", "owing gratitude"),
    ("indecipherable", "Advanced", "adjective", "not able to be read"),
    ("indecorous", "Expert", "adjective", "not in keeping with standards"),
    ("indefatigable", "Expert", "adjective", "persisting tirelessly"),
    ("indelible", "Advanced", "adjective", "not able to be forgotten"),
    ("indemnify", "Advanced", "verb", "to compensate for harm"),
    ("indeterminate", "Advanced", "adjective", "not exactly known"),
    ("indicative", "Advanced", "adjective", "serving as sign"),
    ("indict", "Advanced", "verb", "to formally accuse of crime"),
    ("indifferent", "Advanced", "adjective", "having no interest"),
    ("indigenous", "Advanced", "adjective", "originating naturally in place"),
    ("indigent", "Advanced", "adjective", "poor and needy"),
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
    start_id = 1601
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"{i+1}/{len(GRE_WORDS)}: {word}")
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"The outcome was {word} given the circumstances.",
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch19.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
