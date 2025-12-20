import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("solicitous", "Advanced", "adjective", "showing interest or concern"),
    ("soporific", "Expert", "adjective", "tending to induce sleep"),
    ("specious", "Advanced", "adjective", "superficially plausible but wrong"),
    ("sporadic", "Advanced", "adjective", "occurring at irregular intervals"),
    ("spurious", "Advanced", "adjective", "not genuine; false"),
    ("squander", "Advanced", "verb", "to waste recklessly"),
    ("staid", "Advanced", "adjective", "sedate and respectable"),
    ("stalwart", "Advanced", "adjective", "loyal and hardworking"),
    ("stigmatize", "Advanced", "verb", "to describe disgracefully"),
    ("stint", "Advanced", "noun", "period of time spent doing something"),
    ("stolid", "Expert", "adjective", "calm and showing little emotion"),
    ("strident", "Advanced", "adjective", "loud and harsh"),
    ("stringent", "Advanced", "adjective", "strict and precise"),
    ("stymie", "Advanced", "verb", "to prevent from making progress"),
    ("subpoena", "Advanced", "noun", "writ ordering person to attend court"),
    ("substantiate", "Advanced", "verb", "to provide evidence for"),
    ("subterfuge", "Advanced", "noun", "deceit used to achieve one's goal"),
    ("subversive", "Advanced", "adjective", "seeking to undermine"),
    ("succinct", "Advanced", "adjective", "briefly and clearly expressed"),
    ("supercilious", "Advanced", "adjective", "behaving as if superior"),
    ("superfluous", "Advanced", "adjective", "unnecessary; more than enough"),
    ("supplant", "Advanced", "verb", "to take the place of"),
    ("surfeit", "Expert", "noun", "excessive amount of something"),
    ("surreptitious", "Advanced", "adjective", "kept secret"),
    ("sycophant", "Advanced", "noun", "person who flatters for advantage"),
    ("tacit", "Advanced", "adjective", "understood without being stated"),
    ("taciturn", "Advanced", "adjective", "reserved in speech"),
    ("tangential", "Advanced", "adjective", "barely touching a matter"),
    ("tantamount", "Advanced", "adjective", "equivalent in value"),
    ("temerity", "Advanced", "noun", "excessive confidence or boldness"),
    ("temperance", "Advanced", "noun", "moderation in action"),
    ("tenacious", "Advanced", "adjective", "holding firmly"),
    ("tendentious", "Expert", "adjective", "expressing a strong opinion"),
    ("tenuous", "Advanced", "adjective", "very weak or slight"),
    ("terse", "Advanced", "adjective", "sparing in use of words"),
    ("timorous", "Expert", "adjective", "showing nervousness"),
    ("toady", "Advanced", "noun", "person who flatters"),
    ("torpid", "Expert", "adjective", "mentally or physically inactive"),
    ("tortuous", "Advanced", "adjective", "full of twists and turns"),
    ("tractable", "Advanced", "adjective", "easy to control"),
    ("transgression", "Advanced", "noun", "act that violates law"),
    ("transient", "Advanced", "adjective", "lasting only a short time"),
    ("trenchant", "Advanced", "adjective", "vigorous and articulate"),
    ("trite", "Advanced", "adjective", "lacking originality"),
    ("truculent", "Advanced", "adjective", "eager to fight"),
    ("tumultuous", "Advanced", "adjective", "making loud noise"),
    ("turgid", "Expert", "adjective", "swollen; pompous"),
    ("turpitude", "Expert", "noun", "depravity; wickedness"),
    ("ubiquitous", "Advanced", "adjective", "present everywhere"),
    ("umbrage", "Advanced", "noun", "offense or annoyance"),
    ("unctuous", "Expert", "adjective", "excessively flattering"),
    ("undermine", "Advanced", "verb", "to weaken gradually"),
    ("unequivocal", "Advanced", "adjective", "leaving no doubt"),
    ("unfettered", "Advanced", "adjective", "not confined"),
    ("unimpeachable", "Advanced", "adjective", "entirely trustworthy"),
    ("unprecedented", "Advanced", "adjective", "never done before"),
    ("unprepossessing", "Expert", "adjective", "not attractive"),
    ("unscrupulous", "Advanced", "adjective", "having no moral principles"),
    ("untenable", "Advanced", "adjective", "not able to be defended"),
    ("upbraid", "Advanced", "verb", "to find fault with"),
    ("urbane", "Advanced", "adjective", "suave and courteous"),
    ("usurp", "Advanced", "verb", "to seize power wrongfully"),
    ("vacillate", "Advanced", "verb", "to alternate between opinions"),
    ("vacuous", "Advanced", "adjective", "having no content"),
    ("vapid", "Advanced", "adjective", "offering nothing stimulating"),
    ("variegated", "Expert", "adjective", "exhibiting different colors"),
    ("vehement", "Advanced", "adjective", "showing strong feeling"),
    ("venal", "Expert", "adjective", "showing susceptibility to bribery"),
    ("venerate", "Advanced", "verb", "to regard with respect"),
    ("veracious", "Expert", "adjective", "speaking the truth"),
    ("verbose", "Advanced", "adjective", "using more words than needed"),
    ("vestige", "Advanced", "noun", "trace of something disappearing"),
    ("vex", "Advanced", "verb", "to make annoyed"),
    ("viable", "Advanced", "adjective", "capable of working successfully"),
    ("vicarious", "Advanced", "adjective", "experienced through another"),
    ("vigilant", "Advanced", "adjective", "keeping careful watch"),
    ("vilify", "Advanced", "verb", "to speak ill of"),
    ("vindicate", "Advanced", "verb", "to clear of blame"),
    ("vindictive", "Advanced", "adjective", "having strong desire for revenge"),
    ("virtuoso", "Advanced", "noun", "person highly skilled in music"),
    ("virulent", "Advanced", "adjective", "extremely severe"),
    ("visceral", "Advanced", "adjective", "relating to deep feelings"),
    ("vitiate", "Expert", "verb", "to spoil or impair"),
    ("vitriolic", "Advanced", "adjective", "filled with bitter criticism"),
    ("vituperative", "Expert", "adjective", "bitter and abusive"),
    ("vivacious", "Advanced", "adjective", "attractively lively"),
    ("vociferous", "Advanced", "adjective", "vehement and loud"),
    ("volatile", "Advanced", "adjective", "liable to change rapidly"),
    ("voracious", "Advanced", "adjective", "wanting great quantities"),
    ("warranted", "Advanced", "adjective", "justified or authorized"),
    ("wary", "Advanced", "adjective", "feeling caution about danger"),
    ("whimsical", "Advanced", "adjective", "playfully quaint"),
    ("wistful", "Advanced", "adjective", "having melancholy longing"),
    ("zealous", "Advanced", "adjective", "having great energy"),
    ("zenith", "Advanced", "noun", "highest point reached"),
    ("zephyr", "Expert", "noun", "soft gentle breeze"),
    ("aberrant", "Advanced", "adjective", "departing from accepted standard"),
    ("abjure", "Expert", "verb", "to solemnly renounce"),
    ("abnegate", "Expert", "verb", "to renounce or reject"),
    ("abrogate", "Advanced", "verb", "to abolish or annul"),
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
    start_id = 301
    for i, (word, level, pos, definition) in enumerate(GRE_WORDS):
        print(f"{i+1}/{len(GRE_WORDS)}: {word}")
        word_data = {
            "id": start_id + i,
            "word": word,
            "level": level,
            "partOfSpeech": pos,
            "definition": definition,
            "example": f"The professor's {word} explanation helped students understand.",
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch6.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
