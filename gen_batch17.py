import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("genuine", "Advanced", "adjective", "truly what it is said to be"),
    ("germane", "Advanced", "adjective", "relevant to subject"),
    ("germinate", "Advanced", "verb", "to begin to grow"),
    ("gestation", "Advanced", "noun", "process of developing"),
    ("gesticulate", "Advanced", "verb", "to use gestures instead of speaking"),
    ("ghastly", "Advanced", "adjective", "causing great horror"),
    ("gibe", "Expert", "verb", "to make insulting remarks"),
    ("giddy", "Advanced", "adjective", "having sensation of spinning"),
    ("gird", "Expert", "verb", "to encircle or bind"),
    ("gist", "Advanced", "noun", "substance or essence"),
    ("glacial", "Advanced", "adjective", "relating to ice"),
    ("glaring", "Advanced", "adjective", "shining with dazzling light"),
    ("glean", "Advanced", "verb", "to extract information"),
    ("glee", "Advanced", "noun", "great delight"),
    ("glib", "Advanced", "adjective", "fluent but insincere"),
    ("glimmer", "Advanced", "noun", "faint sign of feeling"),
    ("glimpse", "Advanced", "noun", "brief look at something"),
    ("glitch", "Advanced", "noun", "sudden malfunction"),
    ("gloat", "Advanced", "verb", "to contemplate with smugness"),
    ("gloom", "Advanced", "noun", "partial or total darkness"),
    ("glorify", "Advanced", "verb", "to describe as admirable"),
    ("glossary", "Advanced", "noun", "list of technical terms"),
    ("glower", "Advanced", "verb", "to look angrily"),
    ("glut", "Advanced", "noun", "excessively abundant supply"),
    ("glutton", "Advanced", "noun", "excessively greedy person"),
    ("gnarled", "Advanced", "adjective", "knobbly and twisted"),
    ("gnaw", "Advanced", "verb", "to bite at persistently"),
    ("goad", "Advanced", "verb", "to provoke to action"),
    ("gobble", "Advanced", "verb", "to eat hurriedly"),
    ("gory", "Advanced", "adjective", "involving much bloodshed"),
    ("gossamer", "Expert", "adjective", "used to refer to something delicate"),
    ("gouge", "Advanced", "verb", "to make groove in"),
    ("govern", "Advanced", "verb", "to conduct policy of"),
    ("graceful", "Advanced", "adjective", "having elegance"),
    ("gracious", "Advanced", "adjective", "courteous and kind"),
    ("gradient", "Advanced", "noun", "rate of change"),
    ("gradual", "Advanced", "adjective", "taking place by degrees"),
    ("graft", "Advanced", "noun", "practices for personal gain"),
    ("grandeur", "Advanced", "noun", "splendor and impressiveness"),
    ("grandiloquent", "Expert", "adjective", "pompous in language"),
    ("grandiose", "Advanced", "adjective", "impressive and imposing"),
    ("grapple", "Advanced", "verb", "to engage in struggle"),
    ("gratify", "Advanced", "verb", "to give pleasure to"),
    ("gratis", "Advanced", "adjective", "without charge"),
    ("gratuitous", "Advanced", "adjective", "uncalled for"),
    ("grave", "Advanced", "adjective", "giving cause for alarm"),
    ("gravity", "Advanced", "noun", "extreme importance"),
    ("gregarious", "Advanced", "adjective", "fond of company"),
    ("grievance", "Advanced", "noun", "real or imagined wrong"),
    ("grievous", "Advanced", "adjective", "very severe"),
    ("grimace", "Advanced", "noun", "ugly twisted expression"),
    ("grim", "Advanced", "adjective", "forbidding in aspect"),
    ("grisly", "Advanced", "adjective", "causing horror"),
    ("grouse", "Advanced", "verb", "to complain pettily"),
    ("grovel", "Advanced", "verb", "to lie face downward"),
    ("grudge", "Advanced", "noun", "persistent feeling of resentment"),
    ("grueling", "Advanced", "adjective", "extremely tiring"),
    ("gruesome", "Advanced", "adjective", "causing repulsion"),
    ("gruff", "Advanced", "adjective", "rough in manner"),
    ("guile", "Advanced", "noun", "sly or cunning intelligence"),
    ("guileless", "Advanced", "adjective", "devoid of guile"),
    ("gullible", "Advanced", "adjective", "easily persuaded to believe"),
    ("gush", "Advanced", "verb", "to send out in rapid stream"),
    ("gusto", "Advanced", "noun", "enjoyment and enthusiasm"),
    ("gutter", "Advanced", "noun", "shallow trough"),
    ("habituate", "Advanced", "verb", "to make accustomed"),
    ("hackneyed", "Advanced", "adjective", "lacking significance through overuse"),
    ("haggard", "Advanced", "adjective", "looking exhausted"),
    ("haggle", "Advanced", "verb", "to dispute over price"),
    ("halcyon", "Expert", "adjective", "denoting happy time"),
    ("hallow", "Advanced", "verb", "to honor as holy"),
    ("hallucination", "Advanced", "noun", "experience involving perception"),
    ("halt", "Advanced", "verb", "to bring to sudden stop"),
    ("hamper", "Advanced", "verb", "to hinder or impede"),
    ("haphazard", "Advanced", "adjective", "lacking any plan"),
    ("hapless", "Advanced", "adjective", "unfortunate"),
    ("harangue", "Advanced", "verb", "to lecture at length"),
    ("harass", "Advanced", "verb", "to subject to constant attacks"),
    ("harbinger", "Expert", "noun", "person or thing announcing approach"),
    ("harbor", "Advanced", "verb", "to keep thought in mind"),
    ("hardy", "Advanced", "adjective", "robust and sturdy"),
    ("harken", "Expert", "verb", "to listen attentively"),
    ("harmony", "Advanced", "noun", "state of being in agreement"),
    ("harness", "Advanced", "verb", "to control and make use of"),
    ("harp", "Advanced", "verb", "to talk persistently"),
    ("harridan", "Expert", "noun", "strict bossy woman"),
    ("harrowing", "Advanced", "adjective", "acutely distressing"),
    ("harsh", "Advanced", "adjective", "unpleasantly rough"),
    ("hasten", "Advanced", "verb", "to be quick to do"),
    ("hasty", "Advanced", "adjective", "done with excessive speed"),
    ("haughty", "Advanced", "adjective", "arrogantly superior"),
    ("haunt", "Advanced", "verb", "to continually appear in"),
    ("haven", "Advanced", "noun", "place of safety"),
    ("havoc", "Advanced", "noun", "widespread destruction"),
    ("hazard", "Advanced", "noun", "danger or risk"),
    ("hazy", "Advanced", "adjective", "covered by haze"),
    ("headstrong", "Advanced", "adjective", "willfully determined"),
    ("heckle", "Advanced", "verb", "to interrupt with comments"),
    ("hector", "Expert", "verb", "to talk in bullying way"),
    ("heed", "Advanced", "verb", "to pay attention to"),
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
    start_id = 1401
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"{i+1}/{len(GRE_WORDS)}: {word}")
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"They demonstrated a {word} response to the situation.",
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch17.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
