import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("panegyric", "Expert", "noun", "public speech of praise"),
    ("panoramic", "Advanced", "adjective", "with wide view"),
    ("paradigm", "Advanced", "noun", "typical example or pattern"),
    ("paradox", "Advanced", "noun", "seemingly contradictory statement"),
    ("paragon", "Advanced", "noun", "model of excellence"),
    ("parallel", "Advanced", "adjective", "side by side"),
    ("paramount", "Advanced", "adjective", "more important than anything"),
    ("paranoid", "Advanced", "adjective", "unreasonably anxious"),
    ("paraphrase", "Advanced", "verb", "to express meaning differently"),
    ("parasite", "Advanced", "noun", "organism living on another"),
    ("parched", "Advanced", "adjective", "dried out with heat"),
    ("pariah", "Advanced", "noun", "outcast"),
    ("parity", "Advanced", "noun", "state of being equal"),
    ("parlance", "Advanced", "noun", "particular way of speaking"),
    ("parochial", "Advanced", "adjective", "having limited outlook"),
    ("parody", "Advanced", "noun", "imitation for comic effect"),
    ("paroxysm", "Expert", "noun", "sudden attack or outburst"),
    ("parry", "Advanced", "verb", "to ward off weapon"),
    ("parsimonious", "Expert", "adjective", "unwilling to spend money"),
    ("partial", "Advanced", "adjective", "existing only in part"),
    ("partisan", "Advanced", "adjective", "prejudiced in favor of cause"),
    ("passive", "Advanced", "adjective", "accepting what happens"),
    ("pastoral", "Advanced", "adjective", "associated with countryside"),
    ("patent", "Advanced", "adjective", "easily recognizable"),
    ("pathetic", "Advanced", "adjective", "arousing pity"),
    ("pathological", "Advanced", "adjective", "relating to disease"),
    ("pathos", "Advanced", "noun", "quality that evokes pity"),
    ("patriarch", "Advanced", "noun", "male head of family"),
    ("patrician", "Expert", "noun", "person of high social rank"),
    ("patrimony", "Expert", "noun", "property inherited from father"),
    ("patronize", "Advanced", "verb", "to treat condescendingly"),
    ("paucity", "Advanced", "noun", "presence of something in small quantity"),
    ("pauper", "Advanced", "noun", "very poor person"),
    ("pedestrian", "Advanced", "adjective", "lacking inspiration"),
    ("pedantic", "Advanced", "adjective", "excessively concerned with details"),
    ("pejorative", "Advanced", "adjective", "expressing contempt"),
    ("penchant", "Advanced", "noun", "strong liking for something"),
    ("penitent", "Advanced", "adjective", "feeling sorrow for wrongdoing"),
    ("pensive", "Advanced", "adjective", "engaged in deep thought"),
    ("penury", "Expert", "noun", "extreme poverty"),
    ("perceptive", "Advanced", "adjective", "having keen insight"),
    ("percipient", "Expert", "adjective", "having good insight"),
    ("peremptory", "Expert", "adjective", "insisting on immediate attention"),
    ("perennial", "Advanced", "adjective", "lasting indefinitely"),
    ("perfidious", "Expert", "adjective", "deceitful and untrustworthy"),
    ("perfunctory", "Advanced", "adjective", "carried out with minimum effort"),
    ("perilous", "Advanced", "adjective", "full of danger"),
    ("peripheral", "Advanced", "adjective", "of secondary importance"),
    ("perjury", "Advanced", "noun", "offense of lying under oath"),
    ("permeate", "Advanced", "verb", "to spread throughout"),
    ("pernicious", "Advanced", "adjective", "having harmful effect"),
    ("perpetual", "Advanced", "adjective", "never ending"),
    ("perpetuate", "Advanced", "verb", "to make continue indefinitely"),
    ("perplexing", "Advanced", "adjective", "completely baffling"),
    ("persevere", "Advanced", "verb", "to continue despite difficulty"),
    ("persistent", "Advanced", "adjective", "continuing firmly"),
    ("personable", "Advanced", "adjective", "having pleasant manner"),
    ("perspicacious", "Expert", "adjective", "having keen mental perception"),
    ("pertinacious", "Expert", "adjective", "holding firmly to opinion"),
    ("pertinent", "Advanced", "adjective", "relevant to matter"),
    ("perturb", "Advanced", "verb", "to make anxious"),
    ("peruse", "Advanced", "verb", "to read thoroughly"),
    ("pervasive", "Advanced", "adjective", "spreading widely"),
    ("pessimist", "Advanced", "noun", "person who expects worst"),
    ("petty", "Advanced", "adjective", "of little importance"),
    ("petulant", "Advanced", "adjective", "childishly sulky"),
    ("philanthropic", "Advanced", "adjective", "seeking to promote welfare"),
    ("philistine", "Expert", "noun", "person hostile to culture"),
    ("phlegmatic", "Expert", "adjective", "having unemotional disposition"),
    ("pinnacle", "Advanced", "noun", "highest point"),
    ("pious", "Advanced", "adjective", "devoutly religious"),
    ("pique", "Advanced", "verb", "to stimulate interest"),
    ("pithy", "Advanced", "adjective", "concise and forceful"),
    ("pittance", "Advanced", "noun", "very small amount"),
    ("pivotal", "Advanced", "adjective", "of crucial importance"),
    ("placate", "Advanced", "verb", "to make less angry"),
    ("placid", "Advanced", "adjective", "not easily upset"),
    ("plagiarize", "Advanced", "verb", "to take another's work"),
    ("plaintiff", "Advanced", "noun", "person who brings case"),
    ("plaintive", "Advanced", "adjective", "sounding sad"),
    ("plastic", "Advanced", "adjective", "easily shaped or molded"),
    ("platitude", "Advanced", "noun", "remark used too often"),
    ("plausible", "Advanced", "adjective", "seeming reasonable"),
    ("plebeian", "Expert", "adjective", "of lower social classes"),
    ("plenary", "Expert", "adjective", "unqualified or absolute"),
    ("plethora", "Advanced", "noun", "excess of something"),
    ("pliable", "Advanced", "adjective", "easily bent"),
    ("pliant", "Advanced", "adjective", "easily influenced"),
    ("plight", "Advanced", "noun", "dangerous situation"),
    ("plodding", "Advanced", "adjective", "slow-moving and unexciting"),
    ("ploy", "Advanced", "noun", "cunning plan"),
    ("pluck", "Advanced", "noun", "spirited courage"),
    ("plummet", "Advanced", "verb", "to fall sharply"),
    ("plunder", "Advanced", "verb", "to steal goods"),
    ("pluralistic", "Advanced", "adjective", "of system allowing diversity"),
    ("poignant", "Advanced", "adjective", "evoking sadness"),
    ("poised", "Advanced", "adjective", "having composed manner"),
    ("polemic", "Advanced", "noun", "strong verbal attack"),
    ("polished", "Advanced", "adjective", "accomplished and skillful"),
    ("pompous", "Advanced", "adjective", "affectedly grand"),
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
    start_id = 2201
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch25.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
