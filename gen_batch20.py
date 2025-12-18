import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("indignant", "Advanced", "adjective", "feeling or showing anger"),
    ("indignity", "Advanced", "noun", "treatment causing shame"),
    ("indiscriminate", "Advanced", "adjective", "done at random"),
    ("indispensable", "Advanced", "adjective", "absolutely necessary"),
    ("indisputable", "Advanced", "adjective", "unable to be challenged"),
    ("indistinct", "Advanced", "adjective", "not clear or sharply defined"),
    ("indoctrinate", "Advanced", "verb", "to teach to accept beliefs"),
    ("indolent", "Advanced", "adjective", "wanting to avoid activity"),
    ("indomitable", "Advanced", "adjective", "impossible to subdue"),
    ("induce", "Advanced", "verb", "to succeed in persuading"),
    ("indulge", "Advanced", "verb", "to allow oneself to enjoy"),
    ("industrious", "Advanced", "adjective", "diligent and hardworking"),
    ("ineffable", "Expert", "adjective", "too great to be expressed"),
    ("ineffectual", "Advanced", "adjective", "not producing desired effect"),
    ("ineluctable", "Expert", "adjective", "unable to be resisted"),
    ("inept", "Advanced", "adjective", "having no skill"),
    ("inequity", "Advanced", "noun", "lack of fairness"),
    ("inert", "Advanced", "adjective", "lacking ability to move"),
    ("inertia", "Advanced", "noun", "tendency to do nothing"),
    ("inevitable", "Advanced", "adjective", "certain to happen"),
    ("inexorable", "Expert", "adjective", "impossible to stop"),
    ("inexplicable", "Advanced", "adjective", "unable to be explained"),
    ("inextricable", "Advanced", "adjective", "impossible to disentangle"),
    ("infallible", "Advanced", "adjective", "incapable of making mistakes"),
    ("infamous", "Advanced", "adjective", "well known for bad quality"),
    ("infantile", "Advanced", "adjective", "of or occurring among babies"),
    ("infatuated", "Advanced", "adjective", "possessed with intense passion"),
    ("infer", "Advanced", "verb", "to deduce from evidence"),
    ("inferior", "Advanced", "adjective", "lower in rank or quality"),
    ("infernal", "Advanced", "adjective", "relating to hell"),
    ("infest", "Advanced", "verb", "to be present in large numbers"),
    ("infiltrate", "Advanced", "verb", "to enter or gain access"),
    ("infinite", "Advanced", "adjective", "limitless or endless"),
    ("infinitesimal", "Advanced", "adjective", "extremely small"),
    ("infirm", "Advanced", "adjective", "not physically strong"),
    ("inflame", "Advanced", "verb", "to provoke strong feelings"),
    ("inflated", "Advanced", "adjective", "excessively increased"),
    ("inflexible", "Advanced", "adjective", "unwilling to change"),
    ("inflict", "Advanced", "verb", "to cause to be suffered"),
    ("influential", "Advanced", "adjective", "having great influence"),
    ("influx", "Advanced", "noun", "arrival of large numbers"),
    ("infraction", "Advanced", "noun", "violation of law or rule"),
    ("infringe", "Advanced", "verb", "to actively break terms"),
    ("infuriate", "Advanced", "verb", "to make extremely angry"),
    ("infuse", "Advanced", "verb", "to fill with quality"),
    ("ingenious", "Advanced", "adjective", "clever and inventive"),
    ("ingenuity", "Advanced", "noun", "quality of being clever"),
    ("ingenuous", "Advanced", "adjective", "innocent and unsuspecting"),
    ("inglorious", "Expert", "adjective", "causing shame"),
    ("ingrained", "Advanced", "adjective", "firmly fixed"),
    ("ingratiate", "Advanced", "verb", "to gain favor with"),
    ("inherent", "Advanced", "adjective", "existing in something as permanent"),
    ("inhibit", "Advanced", "verb", "to hinder or restrain"),
    ("inimical", "Advanced", "adjective", "tending to obstruct"),
    ("inimitable", "Advanced", "adjective", "so good as to be impossible to imitate"),
    ("iniquitous", "Expert", "adjective", "grossly unfair"),
    ("initiate", "Advanced", "verb", "to cause to begin"),
    ("injunction", "Advanced", "noun", "authoritative warning"),
    ("innate", "Advanced", "adjective", "inborn or natural"),
    ("innocuous", "Advanced", "adjective", "not harmful or offensive"),
    ("innovate", "Advanced", "verb", "to make changes in something"),
    ("innuendo", "Advanced", "noun", "allusive or oblique remark"),
    ("inordinate", "Advanced", "adjective", "unusually or disproportionately large"),
    ("inquest", "Advanced", "noun", "judicial inquiry"),
    ("inquire", "Advanced", "verb", "to ask for information"),
    ("inquisitive", "Advanced", "adjective", "curious or inquiring"),
    ("insatiable", "Advanced", "adjective", "impossible to satisfy"),
    ("inscribe", "Advanced", "verb", "to write or carve"),
    ("inscrutable", "Advanced", "adjective", "impossible to understand"),
    ("insensible", "Advanced", "adjective", "without physical sensation"),
    ("insidious", "Advanced", "adjective", "proceeding in gradual way"),
    ("insight", "Advanced", "noun", "accurate understanding"),
    ("insightful", "Advanced", "adjective", "having deep understanding"),
    ("insinuate", "Advanced", "verb", "to suggest or hint"),
    ("insipid", "Advanced", "adjective", "lacking flavor or interest"),
    ("insistent", "Advanced", "adjective", "demanding attention"),
    ("insolent", "Advanced", "adjective", "showing rude disrespect"),
    ("insolvent", "Advanced", "adjective", "unable to pay debts"),
    ("insomnia", "Advanced", "noun", "habitual sleeplessness"),
    ("insouciance", "Expert", "noun", "casual lack of concern"),
    ("inspire", "Advanced", "verb", "to fill with urge to do"),
    ("instability", "Advanced", "noun", "lack of stability"),
    ("instigate", "Advanced", "verb", "to bring about"),
    ("instill", "Advanced", "verb", "to gradually establish idea"),
    ("instinctive", "Advanced", "adjective", "relating to innate behavior"),
    ("institute", "Advanced", "verb", "to set in motion"),
    ("instrumental", "Advanced", "adjective", "serving as means"),
    ("insubordinate", "Advanced", "adjective", "defiant of authority"),
    ("insubstantial", "Advanced", "adjective", "lacking strength and solidity"),
    ("insufferable", "Advanced", "adjective", "too extreme to bear"),
    ("insular", "Advanced", "adjective", "ignorant of outside world"),
    ("insulate", "Advanced", "verb", "to protect from unpleasant influences"),
    ("insurgent", "Advanced", "noun", "rebel or revolutionary"),
    ("insurmountable", "Advanced", "adjective", "too great to be overcome"),
    ("insurrection", "Advanced", "noun", "violent uprising"),
    ("intact", "Advanced", "adjective", "not damaged in any way"),
    ("integral", "Advanced", "adjective", "necessary for completeness"),
    ("integrate", "Advanced", "verb", "to combine to form whole"),
    ("integrity", "Advanced", "noun", "quality of being honest"),
    ("intellect", "Advanced", "noun", "faculty of reasoning"),
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
    start_id = 1701
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"{i+1}/{len(GRE_WORDS)}: {word}")
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"The {word} aspect was crucial to the argument.",
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch20.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
