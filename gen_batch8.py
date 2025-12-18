import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("aversion", "Advanced", "noun", "strong dislike"),
    ("avid", "Advanced", "adjective", "having keen interest"),
    ("axiom", "Advanced", "noun", "statement accepted as true"),
    ("banal", "Advanced", "adjective", "lacking originality"),
    ("bane", "Advanced", "noun", "cause of great distress"),
    ("baroque", "Advanced", "adjective", "highly ornate and extravagant"),
    ("barrage", "Advanced", "noun", "overwhelming quantity"),
    ("bastion", "Advanced", "noun", "stronghold defending principle"),
    ("beget", "Advanced", "verb", "to bring about"),
    ("begrudge", "Advanced", "verb", "to envy someone's possession"),
    ("beguile", "Advanced", "verb", "to charm or enchant"),
    ("behemoth", "Advanced", "noun", "huge creature or thing"),
    ("behold", "Advanced", "verb", "to see or observe"),
    ("beholden", "Advanced", "adjective", "owing thanks or duty"),
    ("belie", "Advanced", "verb", "to fail to give true impression"),
    ("belittle", "Advanced", "verb", "to make seem unimportant"),
    ("bellicose", "Advanced", "adjective", "demonstrating aggression"),
    ("belligerent", "Advanced", "adjective", "hostile and aggressive"),
    ("bemoan", "Advanced", "verb", "to express discontent"),
    ("bemused", "Advanced", "adjective", "puzzled or confused"),
    ("benefactor", "Advanced", "noun", "person who gives aid"),
    ("beneficent", "Advanced", "adjective", "generous and doing good"),
    ("benevolent", "Advanced", "adjective", "well meaning and kindly"),
    ("benign", "Advanced", "adjective", "gentle and kindly"),
    ("bequeath", "Advanced", "verb", "to leave property by will"),
    ("berate", "Advanced", "verb", "to scold angrily"),
    ("bereft", "Advanced", "adjective", "deprived of"),
    ("beset", "Advanced", "verb", "to trouble persistently"),
    ("besmirch", "Expert", "verb", "to damage reputation"),
    ("bestow", "Advanced", "verb", "to confer gift or honor"),
    ("betray", "Advanced", "verb", "to expose to enemy"),
    ("bewilder", "Advanced", "verb", "to cause perplexity"),
    ("bias", "Advanced", "noun", "prejudice for or against"),
    ("bifurcate", "Expert", "verb", "to divide into two branches"),
    ("bigot", "Advanced", "noun", "person intolerant toward others"),
    ("bilateral", "Advanced", "adjective", "involving two parties"),
    ("bilk", "Advanced", "verb", "to cheat or defraud"),
    ("blasphemy", "Advanced", "noun", "irreverent talk about religion"),
    ("blatant", "Advanced", "adjective", "completely obvious"),
    ("blight", "Advanced", "noun", "thing that impairs quality"),
    ("bliss", "Advanced", "noun", "perfect happiness"),
    ("blithe", "Advanced", "adjective", "showing casual indifference"),
    ("blunder", "Advanced", "noun", "stupid or careless mistake"),
    ("blunt", "Advanced", "adjective", "uncompromisingly forthright"),
    ("boast", "Advanced", "verb", "to talk with excessive pride"),
    ("bode", "Advanced", "verb", "to be omen of outcome"),
    ("bogus", "Advanced", "adjective", "not genuine"),
    ("boisterous", "Advanced", "adjective", "noisy and energetic"),
    ("bolster", "Advanced", "verb", "to support or strengthen"),
    ("bombastic", "Advanced", "adjective", "high-sounding but meaningless"),
    ("boon", "Advanced", "noun", "thing that is helpful"),
    ("bourgeois", "Advanced", "adjective", "of middle class"),
    ("bracing", "Advanced", "adjective", "fresh and invigorating"),
    ("brandish", "Advanced", "verb", "to wave or flourish"),
    ("brash", "Advanced", "adjective", "self-assertive in rude way"),
    ("bravado", "Advanced", "noun", "bold manner to impress"),
    ("breach", "Advanced", "noun", "gap in wall or barrier"),
    ("brevity", "Advanced", "noun", "concise expression"),
    ("bridle", "Advanced", "verb", "to show resentment"),
    ("bristle", "Advanced", "verb", "to react angrily"),
    ("broach", "Advanced", "verb", "to raise subject for discussion"),
    ("bromide", "Expert", "noun", "trite and unoriginal idea"),
    ("brook", "Advanced", "verb", "to tolerate or allow"),
    ("browbeat", "Advanced", "verb", "to intimidate with words"),
    ("brusque", "Advanced", "adjective", "abrupt in manner"),
    ("bucolic", "Expert", "adjective", "relating to countryside"),
    ("buffoon", "Advanced", "noun", "ridiculous but amusing person"),
    ("bulwark", "Advanced", "noun", "defensive wall"),
    ("bungle", "Advanced", "verb", "to carry out task clumsily"),
    ("buoyant", "Advanced", "adjective", "cheerful and optimistic"),
    ("burgeon", "Advanced", "verb", "to begin to grow rapidly"),
    ("burnish", "Advanced", "verb", "to polish by rubbing"),
    ("buttress", "Advanced", "verb", "to increase strength of"),
    ("byzantine", "Expert", "adjective", "excessively complicated"),
    ("cache", "Advanced", "noun", "hidden store of things"),
    ("cacophony", "Advanced", "noun", "harsh discordant sound"),
    ("cadence", "Advanced", "noun", "rhythmic flow of sequence"),
    ("cajole", "Advanced", "verb", "to persuade by flattery"),
    ("calamity", "Advanced", "noun", "event causing great damage"),
    ("calibrate", "Advanced", "verb", "to adjust precisely"),
    ("callous", "Advanced", "adjective", "showing cruel disregard"),
    ("callow", "Advanced", "adjective", "inexperienced and immature"),
    ("calumny", "Expert", "noun", "false statement to damage"),
    ("camaraderie", "Advanced", "noun", "mutual trust among friends"),
    ("candid", "Advanced", "adjective", "truthful and straightforward"),
    ("candor", "Advanced", "noun", "quality of being open"),
    ("canvass", "Advanced", "verb", "to seek opinion of"),
    ("capacity", "Advanced", "noun", "maximum amount containable"),
    ("capitulate", "Advanced", "verb", "to cease to resist"),
    ("capricious", "Advanced", "adjective", "given to sudden change"),
    ("captious", "Expert", "adjective", "tending to find fault"),
    ("cardinal", "Advanced", "adjective", "of greatest importance"),
    ("caricature", "Advanced", "noun", "exaggerated description"),
    ("carping", "Expert", "adjective", "difficult to please"),
    ("castigate", "Advanced", "verb", "to reprimand severely"),
    ("catalyst", "Advanced", "noun", "person or thing precipitating change"),
    ("categorical", "Advanced", "adjective", "unambiguously explicit"),
    ("catharsis", "Advanced", "noun", "release of strong emotions"),
    ("caustic", "Advanced", "adjective", "sarcastic in bitter way"),
    ("cavalier", "Advanced", "adjective", "showing lack of proper concern"),
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
    start_id = 501
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"{i+1}/{len(GRE_WORDS)}: {word}")
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"His {word} nature was evident in the meeting.",
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch8.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
