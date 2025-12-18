import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("juggernaut", "Expert", "noun", "huge and overwhelming force"),
    ("juxtapose", "Advanced", "verb", "to place side by side"),
    ("keen", "Advanced", "adjective", "sharp or penetrating"),
    ("kernel", "Advanced", "noun", "central or essential part"),
    ("kindle", "Advanced", "verb", "to light or ignite"),
    ("kinetic", "Advanced", "adjective", "relating to motion"),
    ("knave", "Expert", "noun", "dishonest or unscrupulous man"),
    ("laborious", "Advanced", "adjective", "requiring much work"),
    ("labyrinth", "Advanced", "noun", "complicated network of passages"),
    ("lacerate", "Advanced", "verb", "to tear or cut jaggedly"),
    ("lachrymose", "Expert", "adjective", "tearful or sad"),
    ("lackadaisical", "Advanced", "adjective", "lacking enthusiasm"),
    ("lackluster", "Advanced", "adjective", "lacking brilliance"),
    ("laconic", "Advanced", "adjective", "using very few words"),
    ("laggard", "Expert", "noun", "person who falls behind"),
    ("lambaste", "Advanced", "verb", "to criticize harshly"),
    ("lament", "Advanced", "verb", "to mourn or express sorrow"),
    ("lampoon", "Advanced", "verb", "to publicly criticize through satire"),
    ("languid", "Advanced", "adjective", "lacking energy"),
    ("languish", "Advanced", "verb", "to lose vitality"),
    ("larceny", "Advanced", "noun", "theft of personal property"),
    ("largesse", "Expert", "noun", "generosity in giving"),
    ("lascivious", "Expert", "adjective", "feeling or showing sexual desire"),
    ("lassitude", "Advanced", "noun", "physical or mental weariness"),
    ("latent", "Advanced", "adjective", "existing but not developed"),
    ("lateral", "Advanced", "adjective", "of or relating to side"),
    ("latitude", "Advanced", "noun", "freedom from restrictions"),
    ("laudable", "Advanced", "adjective", "deserving praise"),
    ("laudatory", "Advanced", "adjective", "expressing praise"),
    ("lavish", "Advanced", "adjective", "sumptuously rich"),
    ("lax", "Advanced", "adjective", "not sufficiently strict"),
    ("leery", "Advanced", "adjective", "cautious due to suspicion"),
    ("legacy", "Advanced", "noun", "something handed down"),
    ("legitimate", "Advanced", "adjective", "conforming to rules"),
    ("lenient", "Advanced", "adjective", "permissive or merciful"),
    ("lethal", "Advanced", "adjective", "sufficient to cause death"),
    ("lethargic", "Advanced", "adjective", "affected by lack of energy"),
    ("levity", "Advanced", "noun", "humor or frivolity"),
    ("levy", "Advanced", "verb", "to impose tax or fine"),
    ("liable", "Advanced", "adjective", "responsible by law"),
    ("liaison", "Advanced", "noun", "communication or cooperation"),
    ("liberal", "Advanced", "adjective", "willing to respect others"),
    ("libertine", "Expert", "noun", "person devoid of moral restraints"),
    ("licentious", "Expert", "adjective", "promiscuous and unprincipled"),
    ("limpid", "Expert", "adjective", "clear and transparent"),
    ("lineage", "Advanced", "noun", "lineal descent from ancestor"),
    ("lionize", "Advanced", "verb", "to give public attention"),
    ("lithe", "Advanced", "adjective", "thin and supple"),
    ("litigate", "Advanced", "verb", "to take legal action"),
    ("litigious", "Advanced", "adjective", "unreasonably prone to go to law"),
    ("livid", "Advanced", "adjective", "furiously angry"),
    ("loathe", "Advanced", "verb", "to feel intense dislike"),
    ("lofty", "Advanced", "adjective", "of imposing height"),
    ("loquacious", "Advanced", "adjective", "tending to talk much"),
    ("lout", "Advanced", "noun", "uncouth and aggressive man"),
    ("lubricate", "Advanced", "verb", "to apply oil or grease"),
    ("lucid", "Advanced", "adjective", "expressed clearly"),
    ("lucrative", "Advanced", "adjective", "producing great profit"),
    ("ludicrous", "Advanced", "adjective", "so foolish as to be amusing"),
    ("lugubrious", "Expert", "adjective", "looking or sounding sad"),
    ("lull", "Advanced", "verb", "to calm or send to sleep"),
    ("lumber", "Advanced", "verb", "to move heavily and clumsily"),
    ("luminary", "Advanced", "noun", "person who inspires others"),
    ("luminous", "Advanced", "adjective", "full of light"),
    ("lurch", "Advanced", "verb", "to make an abrupt movement"),
    ("lurid", "Advanced", "adjective", "very vivid in color"),
    ("lurk", "Advanced", "verb", "to be hidden waiting"),
    ("luscious", "Advanced", "adjective", "richly sweet"),
    ("lustrous", "Advanced", "adjective", "shining and soft"),
    ("luxuriant", "Advanced", "adjective", "rich and profuse"),
    ("machination", "Expert", "noun", "scheming or crafty plot"),
    ("magnanimous", "Advanced", "adjective", "very generous or forgiving"),
    ("magnate", "Advanced", "noun", "wealthy influential person"),
    ("magnitude", "Advanced", "noun", "great size or importance"),
    ("majestic", "Advanced", "adjective", "having impressive beauty"),
    ("maladroit", "Expert", "adjective", "ineffective or clumsy"),
    ("malady", "Advanced", "noun", "disease or ailment"),
    ("malaise", "Advanced", "noun", "general feeling of discomfort"),
    ("malapropism", "Expert", "noun", "mistaken use of word"),
    ("malcontent", "Advanced", "noun", "person dissatisfied"),
    ("malevolent", "Advanced", "adjective", "having evil intentions"),
    ("malicious", "Advanced", "adjective", "intending to do harm"),
    ("malign", "Advanced", "verb", "to speak about in harmful way"),
    ("malignant", "Advanced", "adjective", "very virulent or harmful"),
    ("malleable", "Advanced", "adjective", "easily influenced"),
    ("mandate", "Advanced", "noun", "official order or commission"),
    ("mandatory", "Advanced", "adjective", "required by law"),
    ("manifest", "Advanced", "adjective", "clear or obvious"),
    ("manifold", "Advanced", "adjective", "many and various"),
    ("manipulate", "Advanced", "verb", "to handle or control"),
    ("mantle", "Advanced", "noun", "role or responsibility"),
    ("mar", "Advanced", "verb", "to impair the quality of"),
    ("marginal", "Advanced", "adjective", "of minor importance"),
    ("maritime", "Advanced", "adjective", "connected with the sea"),
    ("marshal", "Advanced", "verb", "to arrange in proper order"),
    ("martial", "Advanced", "adjective", "of or relating to war"),
    ("martinet", "Expert", "noun", "strict disciplinarian"),
    ("marvel", "Advanced", "verb", "to be filled with wonder"),
    ("materialize", "Advanced", "verb", "to become actual fact"),
    ("maternal", "Advanced", "adjective", "of or relating to mother"),
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
    start_id = 1901
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch22.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
