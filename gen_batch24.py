import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("negligible", "Advanced", "adjective", "so small as to be meaningless"),
    ("neologism", "Expert", "noun", "newly coined word"),
    ("neophyte", "Advanced", "noun", "person who is new to subject"),
    ("nepotism", "Advanced", "noun", "favoritism shown to relatives"),
    ("nettle", "Advanced", "verb", "to irritate or annoy"),
    ("neutral", "Advanced", "adjective", "not supporting either side"),
    ("nexus", "Advanced", "noun", "connection or series"),
    ("niche", "Advanced", "noun", "specialized segment"),
    ("niggling", "Advanced", "adjective", "causing slight irritation"),
    ("nihilism", "Expert", "noun", "rejection of principles"),
    ("nimble", "Advanced", "adjective", "quick and light"),
    ("nocturnal", "Advanced", "adjective", "done or active at night"),
    ("noisome", "Expert", "adjective", "having offensive smell"),
    ("nomadic", "Advanced", "adjective", "roaming from place to place"),
    ("nominal", "Advanced", "adjective", "in name only"),
    ("nonchalant", "Advanced", "adjective", "feeling calm and relaxed"),
    ("noncommittal", "Advanced", "adjective", "not expressing opinion"),
    ("nonentity", "Advanced", "noun", "person of no importance"),
    ("nonpareil", "Expert", "adjective", "having no match or equal"),
    ("nonplussed", "Advanced", "adjective", "surprised and confused"),
    ("nostalgia", "Advanced", "noun", "longing for the past"),
    ("notable", "Advanced", "adjective", "worthy of attention"),
    ("notoriety", "Advanced", "noun", "fame for something bad"),
    ("notorious", "Advanced", "adjective", "famous for something bad"),
    ("novel", "Advanced", "adjective", "new and original"),
    ("novice", "Advanced", "noun", "person new to field"),
    ("noxious", "Advanced", "adjective", "harmful or poisonous"),
    ("nuance", "Advanced", "noun", "subtle difference"),
    ("nullify", "Advanced", "verb", "to make legally null"),
    ("nurture", "Advanced", "verb", "to care for and encourage"),
    ("obdurate", "Advanced", "adjective", "stubbornly refusing to change"),
    ("obeisance", "Expert", "noun", "deferential respect"),
    ("obfuscate", "Advanced", "verb", "to make obscure"),
    ("objective", "Advanced", "adjective", "not influenced by feelings"),
    ("obligatory", "Advanced", "adjective", "required by law or rules"),
    ("oblique", "Advanced", "adjective", "not explicit or direct"),
    ("obliterate", "Advanced", "verb", "to destroy utterly"),
    ("oblivion", "Advanced", "noun", "state of being unaware"),
    ("oblivious", "Advanced", "adjective", "not aware of"),
    ("obloquy", "Expert", "noun", "strong public criticism"),
    ("obscure", "Advanced", "adjective", "not discovered or known"),
    ("obsequious", "Advanced", "adjective", "excessively compliant"),
    ("observant", "Advanced", "adjective", "quick to notice things"),
    ("obsolete", "Advanced", "adjective", "no longer produced or used"),
    ("obstinate", "Advanced", "adjective", "stubbornly refusing to change"),
    ("obstreperous", "Expert", "adjective", "noisy and difficult to control"),
    ("obstruct", "Advanced", "verb", "to block"),
    ("obtrusive", "Advanced", "adjective", "noticeable in unwelcome way"),
    ("obtuse", "Advanced", "adjective", "annoyingly insensitive"),
    ("obviate", "Advanced", "verb", "to remove need for"),
    ("occlude", "Expert", "verb", "to stop or close up"),
    ("occult", "Advanced", "adjective", "supernatural or mystical"),
    ("odious", "Advanced", "adjective", "extremely unpleasant"),
    ("odyssey", "Advanced", "noun", "long eventful journey"),
    ("officious", "Advanced", "adjective", "asserting authority in domineering way"),
    ("olfactory", "Advanced", "adjective", "relating to sense of smell"),
    ("ominous", "Advanced", "adjective", "giving impression of bad omen"),
    ("omnipotent", "Advanced", "adjective", "having unlimited power"),
    ("omnipresent", "Advanced", "adjective", "present everywhere"),
    ("omniscient", "Advanced", "adjective", "knowing everything"),
    ("onerous", "Advanced", "adjective", "involving heavy obligation"),
    ("opaque", "Advanced", "adjective", "not able to be seen through"),
    ("opportune", "Advanced", "adjective", "well-chosen or favorable time"),
    ("opportunist", "Advanced", "noun", "person who exploits circumstances"),
    ("oppressive", "Advanced", "adjective", "unjustly harsh"),
    ("opprobrious", "Expert", "adjective", "expressing scorn or criticism"),
    ("optimal", "Advanced", "adjective", "best or most favorable"),
    ("optimum", "Advanced", "noun", "most favorable conditions"),
    ("opulent", "Advanced", "adjective", "ostentatiously rich"),
    ("oracle", "Advanced", "noun", "priest through whom god spoke"),
    ("orate", "Advanced", "verb", "to make a speech"),
    ("orchestrate", "Advanced", "verb", "to arrange or direct"),
    ("ordain", "Advanced", "verb", "to order officially"),
    ("ordeal", "Advanced", "noun", "painful or horrific experience"),
    ("orthodox", "Advanced", "adjective", "conforming to established doctrine"),
    ("oscillate", "Advanced", "verb", "to move back and forth"),
    ("ossify", "Expert", "verb", "to turn into bone"),
    ("ostensible", "Advanced", "adjective", "stated or appearing to be true"),
    ("ostentatious", "Advanced", "adjective", "designed to impress"),
    ("ostracize", "Advanced", "verb", "to exclude from society"),
    ("oust", "Advanced", "verb", "to drive out from position"),
    ("outlandish", "Advanced", "adjective", "looking bizarre"),
    ("outmoded", "Advanced", "adjective", "old-fashioned"),
    ("outspoken", "Advanced", "adjective", "frank in stating opinions"),
    ("outstrip", "Advanced", "verb", "to move faster or surpass"),
    ("overbearing", "Advanced", "adjective", "unpleasantly domineering"),
    ("overhaul", "Advanced", "verb", "to take apart and examine"),
    ("overt", "Advanced", "adjective", "done openly"),
    ("overwrought", "Advanced", "adjective", "in highly emotional state"),
    ("pacify", "Advanced", "verb", "to bring peace to"),
    ("painstaking", "Advanced", "adjective", "done with great care"),
    ("palatable", "Advanced", "adjective", "pleasant to taste"),
    ("palatial", "Advanced", "adjective", "resembling a palace"),
    ("palliate", "Advanced", "verb", "to make less severe"),
    ("pallid", "Advanced", "adjective", "pale and unhealthy"),
    ("palpable", "Advanced", "adjective", "able to be touched"),
    ("paltry", "Advanced", "adjective", "small or meager"),
    ("panacea", "Advanced", "noun", "solution for all difficulties"),
    ("panache", "Advanced", "noun", "flamboyant confidence"),
    ("pandemic", "Advanced", "adjective", "prevalent over whole area"),
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
    start_id = 2101
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch24.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
