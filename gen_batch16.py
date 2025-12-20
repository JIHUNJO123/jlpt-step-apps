import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("fodder", "Advanced", "noun", "food for livestock"),
    ("foible", "Expert", "noun", "minor weakness in character"),
    ("foil", "Advanced", "verb", "to prevent success of"),
    ("foist", "Expert", "verb", "to impose unwanted thing"),
    ("foment", "Advanced", "verb", "to instigate or stir up"),
    ("foolhardy", "Advanced", "adjective", "recklessly bold"),
    ("foppish", "Expert", "adjective", "excessively concerned with appearance"),
    ("forbearance", "Advanced", "noun", "patient self-control"),
    ("forbid", "Advanced", "verb", "to refuse to allow"),
    ("forbidding", "Advanced", "adjective", "unfriendly or threatening"),
    ("forceful", "Advanced", "adjective", "vigorous and powerful"),
    ("foreboding", "Advanced", "noun", "fearful apprehension"),
    ("foreclose", "Advanced", "verb", "to rule out possibility"),
    ("foreground", "Advanced", "verb", "to make most prominent"),
    ("foremost", "Advanced", "adjective", "most prominent in rank"),
    ("foresee", "Advanced", "verb", "to be aware of beforehand"),
    ("foreshadow", "Advanced", "verb", "to be warning of future"),
    ("foresight", "Advanced", "noun", "ability to predict future"),
    ("forestall", "Advanced", "verb", "to prevent by taking action"),
    ("forfeit", "Advanced", "verb", "to lose as penalty"),
    ("forge", "Advanced", "verb", "to make or shape"),
    ("forgo", "Advanced", "verb", "to omit or decline"),
    ("forlorn", "Advanced", "adjective", "pitifully sad"),
    ("formalize", "Advanced", "verb", "to give legal status to"),
    ("formidable", "Advanced", "adjective", "inspiring fear or respect"),
    ("forsake", "Advanced", "verb", "to abandon or renounce"),
    ("forte", "Advanced", "noun", "thing at which one excels"),
    ("forthcoming", "Advanced", "adjective", "about to happen"),
    ("forthright", "Advanced", "adjective", "direct and outspoken"),
    ("fortify", "Advanced", "verb", "to strengthen place"),
    ("fortitude", "Advanced", "noun", "courage in pain"),
    ("fortuitous", "Advanced", "adjective", "happening by chance"),
    ("forum", "Advanced", "noun", "place for public discussion"),
    ("foster", "Advanced", "verb", "to encourage development"),
    ("foul", "Advanced", "adjective", "offensive to senses"),
    ("founder", "Advanced", "verb", "to fail completely"),
    ("fractious", "Expert", "adjective", "irritable and quarrelsome"),
    ("fracture", "Advanced", "noun", "crack or break"),
    ("fragile", "Advanced", "adjective", "easily broken"),
    ("fragment", "Advanced", "noun", "small part broken off"),
    ("fragrant", "Advanced", "adjective", "having pleasant smell"),
    ("frail", "Advanced", "adjective", "weak and delicate"),
    ("frank", "Advanced", "adjective", "open and sincere"),
    ("frantic", "Advanced", "adjective", "wild with excitement"),
    ("fraternal", "Advanced", "adjective", "of or like brother"),
    ("fraud", "Advanced", "noun", "wrongful deception"),
    ("fraudulent", "Advanced", "adjective", "obtained by deception"),
    ("fraught", "Advanced", "adjective", "filled with something"),
    ("fray", "Advanced", "verb", "to unravel at edge"),
    ("frenetic", "Advanced", "adjective", "fast and energetic"),
    ("frenzy", "Advanced", "noun", "state of uncontrolled excitement"),
    ("frequent", "Advanced", "adjective", "occurring or done often"),
    ("friction", "Advanced", "noun", "conflict between people"),
    ("frivolous", "Advanced", "adjective", "not having serious purpose"),
    ("frugal", "Advanced", "adjective", "sparing with money"),
    ("fruitful", "Advanced", "adjective", "producing good results"),
    ("fruitless", "Advanced", "adjective", "failing to achieve results"),
    ("frustrate", "Advanced", "verb", "to prevent from achieving"),
    ("fulminate", "Expert", "verb", "to express vehement protest"),
    ("fulsome", "Expert", "adjective", "excessively flattering"),
    ("fumble", "Advanced", "verb", "to use hands clumsily"),
    ("functional", "Advanced", "adjective", "designed to be practical"),
    ("fundamental", "Advanced", "adjective", "forming necessary base"),
    ("funereal", "Expert", "adjective", "having characteristics of funeral"),
    ("furbish", "Expert", "verb", "to restore to good condition"),
    ("furious", "Advanced", "adjective", "extremely angry"),
    ("furtive", "Advanced", "adjective", "attempting to avoid notice"),
    ("fury", "Advanced", "noun", "wild or violent anger"),
    ("fuse", "Advanced", "verb", "to join or blend"),
    ("futile", "Advanced", "adjective", "incapable of producing result"),
    ("gadfly", "Expert", "noun", "annoying person"),
    ("gaffe", "Advanced", "noun", "embarrassing blunder"),
    ("gainsay", "Expert", "verb", "to deny or contradict"),
    ("gait", "Advanced", "noun", "manner of walking"),
    ("gall", "Advanced", "noun", "bold impudence"),
    ("gallant", "Advanced", "adjective", "brave and heroic"),
    ("galvanize", "Advanced", "verb", "to shock into action"),
    ("gambit", "Advanced", "noun", "device or action to gain advantage"),
    ("gamble", "Advanced", "verb", "to play games for money"),
    ("gamut", "Advanced", "noun", "complete range"),
    ("gape", "Advanced", "verb", "to stare with mouth open"),
    ("garble", "Advanced", "verb", "to reproduce incorrectly"),
    ("garish", "Advanced", "adjective", "obtrusively bright"),
    ("garner", "Advanced", "verb", "to gather or collect"),
    ("garnish", "Advanced", "verb", "to decorate food"),
    ("garrulous", "Advanced", "adjective", "excessively talkative"),
    ("gauche", "Advanced", "adjective", "lacking social grace"),
    ("gaudy", "Advanced", "adjective", "extravagantly bright"),
    ("gauge", "Advanced", "verb", "to estimate or determine"),
    ("gaunt", "Advanced", "adjective", "lean and haggard"),
    ("gawk", "Advanced", "verb", "to stare stupidly"),
    ("generate", "Advanced", "verb", "to cause to arise"),
    ("generic", "Advanced", "adjective", "characteristic of class"),
    ("generous", "Advanced", "adjective", "showing kindness"),
    ("genesis", "Advanced", "noun", "origin or mode of formation"),
    ("genial", "Advanced", "adjective", "friendly and cheerful"),
    ("genius", "Advanced", "noun", "exceptional intellectual ability"),
    ("genocide", "Advanced", "noun", "deliberate killing of people"),
    ("genre", "Advanced", "noun", "category of artistic composition"),
    ("genteel", "Advanced", "adjective", "polite and refined"),
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
    start_id = 1301
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"{i+1}/{len(GRE_WORDS)}: {word}")
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"The {word} nature of the event surprised everyone.",
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch16.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
