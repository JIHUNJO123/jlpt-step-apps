import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("intellectual", "Advanced", "adjective", "relating to intellect"),
    ("intelligible", "Advanced", "adjective", "able to be understood"),
    ("intemperate", "Expert", "adjective", "having no self-control"),
    ("intensify", "Advanced", "verb", "to become more intense"),
    ("intent", "Advanced", "adjective", "resolved to do something"),
    ("intercede", "Advanced", "verb", "to intervene on behalf"),
    ("interdict", "Expert", "verb", "to prohibit or forbid"),
    ("interim", "Advanced", "noun", "intervening time"),
    ("interject", "Advanced", "verb", "to say abruptly"),
    ("interlocutor", "Expert", "noun", "person who takes part in dialogue"),
    ("interloper", "Expert", "noun", "person who intrudes"),
    ("interlude", "Advanced", "noun", "intervening period"),
    ("intermediary", "Advanced", "noun", "person who acts as link"),
    ("interminable", "Advanced", "adjective", "endless or tedious"),
    ("intermittent", "Advanced", "adjective", "occurring at irregular intervals"),
    ("internalize", "Advanced", "verb", "to make attitudes part of nature"),
    ("interpolate", "Expert", "verb", "to insert between parts"),
    ("interpose", "Advanced", "verb", "to place between"),
    ("interpret", "Advanced", "verb", "to explain meaning"),
    ("interrogate", "Advanced", "verb", "to ask questions closely"),
    ("intersect", "Advanced", "verb", "to divide by passing through"),
    ("intersperse", "Advanced", "verb", "to scatter among or between"),
    ("intertwine", "Advanced", "verb", "to twist or twine together"),
    ("intervene", "Advanced", "verb", "to come between"),
    ("intimate", "Advanced", "verb", "to imply or hint"),
    ("intimidate", "Advanced", "verb", "to frighten or overawe"),
    ("intolerable", "Advanced", "adjective", "unable to be endured"),
    ("intolerant", "Advanced", "adjective", "not tolerant of others"),
    ("intractable", "Advanced", "adjective", "hard to control"),
    ("intransigent", "Advanced", "adjective", "unwilling to change views"),
    ("intrepid", "Advanced", "adjective", "fearless and adventurous"),
    ("intricate", "Advanced", "adjective", "very complicated"),
    ("intrigue", "Advanced", "verb", "to arouse curiosity"),
    ("intrinsic", "Advanced", "adjective", "belonging naturally"),
    ("introspective", "Advanced", "adjective", "given to examining own feelings"),
    ("introvert", "Advanced", "noun", "shy and quiet person"),
    ("intrude", "Advanced", "verb", "to put oneself into situation"),
    ("intrusive", "Advanced", "adjective", "causing disruption"),
    ("intuitive", "Advanced", "adjective", "using instinctive feeling"),
    ("inundate", "Advanced", "verb", "to overwhelm with things"),
    ("inure", "Expert", "verb", "to accustom to something unpleasant"),
    ("invade", "Advanced", "verb", "to enter as enemy"),
    ("invalid", "Advanced", "adjective", "not legally recognized"),
    ("invalidate", "Advanced", "verb", "to make invalid"),
    ("invaluable", "Advanced", "adjective", "extremely useful"),
    ("invariable", "Advanced", "adjective", "never changing"),
    ("invasive", "Advanced", "adjective", "tending to spread"),
    ("invective", "Expert", "noun", "insulting abusive language"),
    ("inveigh", "Expert", "verb", "to speak against strongly"),
    ("inveigle", "Expert", "verb", "to persuade by deception"),
    ("inventive", "Advanced", "adjective", "having ability to create"),
    ("inverse", "Advanced", "adjective", "opposite in position"),
    ("invert", "Advanced", "verb", "to put upside down"),
    ("inveterate", "Advanced", "adjective", "having particular habit"),
    ("invidious", "Expert", "adjective", "likely to arouse resentment"),
    ("invigorate", "Advanced", "verb", "to give strength or energy"),
    ("invincible", "Advanced", "adjective", "too powerful to be defeated"),
    ("inviolable", "Advanced", "adjective", "never to be broken"),
    ("invoke", "Advanced", "verb", "to cite as authority"),
    ("involuntary", "Advanced", "adjective", "done without conscious control"),
    ("involve", "Advanced", "verb", "to include as necessary part"),
    ("invulnerable", "Advanced", "adjective", "impossible to harm"),
    ("iota", "Advanced", "noun", "extremely small amount"),
    ("irascible", "Advanced", "adjective", "having tendency to be angry"),
    ("irate", "Advanced", "adjective", "feeling or showing anger"),
    ("iridescent", "Expert", "adjective", "showing luminous colors"),
    ("irksome", "Advanced", "adjective", "irritating and tedious"),
    ("ironic", "Advanced", "adjective", "happening in opposite way"),
    ("irony", "Advanced", "noun", "expression of meaning through opposite"),
    ("irrational", "Advanced", "adjective", "not logical or reasonable"),
    ("irreconcilable", "Advanced", "adjective", "incompatible"),
    ("irrefutable", "Advanced", "adjective", "impossible to deny"),
    ("irrelevant", "Advanced", "adjective", "not connected with matter"),
    ("irremediable", "Expert", "adjective", "impossible to remedy"),
    ("irreparable", "Advanced", "adjective", "impossible to rectify"),
    ("irreproachable", "Advanced", "adjective", "beyond criticism"),
    ("irresistible", "Advanced", "adjective", "too attractive to resist"),
    ("irresolute", "Advanced", "adjective", "showing hesitancy"),
    ("irrespective", "Advanced", "adjective", "not taking into account"),
    ("irreverent", "Advanced", "adjective", "showing lack of respect"),
    ("irreversible", "Advanced", "adjective", "not able to be undone"),
    ("irrevocable", "Advanced", "adjective", "not able to be changed"),
    ("irritable", "Advanced", "adjective", "having tendency to be annoyed"),
    ("isolate", "Advanced", "verb", "to cause to be alone"),
    ("itinerant", "Advanced", "adjective", "traveling from place to place"),
    ("jaded", "Advanced", "adjective", "tired and bored"),
    ("jargon", "Advanced", "noun", "special words used by profession"),
    ("jaundiced", "Advanced", "adjective", "affected by bitterness"),
    ("jaunty", "Advanced", "adjective", "having lively manner"),
    ("jeer", "Advanced", "verb", "to make rude remarks"),
    ("jejune", "Expert", "adjective", "naive and simplistic"),
    ("jeopardize", "Advanced", "verb", "to put at risk"),
    ("jettison", "Advanced", "verb", "to throw or drop from aircraft"),
    ("jingoist", "Expert", "noun", "extreme patriot"),
    ("jocular", "Advanced", "adjective", "fond of joking"),
    ("jocund", "Expert", "adjective", "cheerful and lighthearted"),
    ("jostle", "Advanced", "verb", "to push roughly"),
    ("jovial", "Advanced", "adjective", "cheerful and friendly"),
    ("jubilant", "Advanced", "adjective", "feeling great happiness"),
    ("judicious", "Advanced", "adjective", "having good judgment"),
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
    start_id = 1801
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch21.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
