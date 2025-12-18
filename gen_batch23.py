import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("matriculate", "Expert", "verb", "to be enrolled in college"),
    ("maverick", "Advanced", "noun", "independent-minded person"),
    ("mawkish", "Expert", "adjective", "sentimental in sickly way"),
    ("meager", "Advanced", "adjective", "lacking in quantity"),
    ("meander", "Advanced", "verb", "to follow winding course"),
    ("measured", "Advanced", "adjective", "carefully considered"),
    ("mediate", "Advanced", "verb", "to intervene in dispute"),
    ("mediocre", "Advanced", "adjective", "of only moderate quality"),
    ("meditate", "Advanced", "verb", "to think deeply"),
    ("medley", "Advanced", "noun", "varied mixture"),
    ("meek", "Advanced", "adjective", "quiet and submissive"),
    ("melancholy", "Advanced", "noun", "deep sadness"),
    ("melee", "Advanced", "noun", "confused fight"),
    ("mellifluous", "Expert", "adjective", "sweet-sounding"),
    ("mendacious", "Expert", "adjective", "not telling truth"),
    ("mendicant", "Expert", "noun", "beggar"),
    ("menial", "Advanced", "adjective", "not requiring skill"),
    ("mentor", "Advanced", "noun", "experienced adviser"),
    ("mercenary", "Advanced", "adjective", "primarily concerned with money"),
    ("mercurial", "Advanced", "adjective", "subject to sudden changes"),
    ("merge", "Advanced", "verb", "to combine into one"),
    ("meritorious", "Advanced", "adjective", "deserving reward"),
    ("mesmerize", "Advanced", "verb", "to hold attention completely"),
    ("metamorphosis", "Advanced", "noun", "transformation of form"),
    ("metaphor", "Advanced", "noun", "figure of speech"),
    ("mete", "Expert", "verb", "to dispense or allot"),
    ("meteoric", "Advanced", "adjective", "developing very fast"),
    ("methodical", "Advanced", "adjective", "orderly and systematic"),
    ("meticulous", "Advanced", "adjective", "very careful and precise"),
    ("mettle", "Advanced", "noun", "ability to cope well"),
    ("miasma", "Expert", "noun", "unpleasant atmosphere"),
    ("microcosm", "Advanced", "noun", "small representation"),
    ("mien", "Expert", "noun", "person's manner or bearing"),
    ("milieu", "Advanced", "noun", "person's social environment"),
    ("militant", "Advanced", "adjective", "aggressively active"),
    ("militate", "Advanced", "verb", "to be a powerful factor against"),
    ("minatory", "Expert", "adjective", "expressing a threat"),
    ("mince", "Advanced", "verb", "to walk affectedly"),
    ("mingle", "Advanced", "verb", "to mix or cause to mix"),
    ("minimize", "Advanced", "verb", "to reduce to smallest amount"),
    ("minion", "Advanced", "noun", "servile follower"),
    ("minute", "Advanced", "adjective", "extremely small"),
    ("minutiae", "Advanced", "noun", "small or precise details"),
    ("mirage", "Advanced", "noun", "optical illusion"),
    ("mire", "Advanced", "noun", "swampy ground"),
    ("mirth", "Advanced", "noun", "amusement expressed in laughter"),
    ("misanthrope", "Expert", "noun", "person who dislikes humankind"),
    ("miscellaneous", "Advanced", "adjective", "of various types"),
    ("mischievous", "Advanced", "adjective", "causing minor trouble"),
    ("misconception", "Advanced", "noun", "view based on wrong thinking"),
    ("misconstrue", "Advanced", "verb", "to interpret wrongly"),
    ("misdemeanor", "Advanced", "noun", "minor wrongdoing"),
    ("miserly", "Advanced", "adjective", "of person who hoards wealth"),
    ("misgiving", "Advanced", "noun", "feeling of doubt"),
    ("misnomer", "Advanced", "noun", "wrong or inaccurate name"),
    ("misogynist", "Expert", "noun", "person who dislikes women"),
    ("mitigate", "Advanced", "verb", "to make less severe"),
    ("mock", "Advanced", "verb", "to tease or laugh at"),
    ("modicum", "Advanced", "noun", "small quantity"),
    ("modulate", "Advanced", "verb", "to regulate or adjust"),
    ("mollify", "Advanced", "verb", "to appease anger"),
    ("molt", "Advanced", "verb", "to shed feathers"),
    ("momentous", "Advanced", "adjective", "of great importance"),
    ("monarchy", "Advanced", "noun", "government by monarch"),
    ("monetary", "Advanced", "adjective", "of or relating to money"),
    ("monolithic", "Advanced", "adjective", "large and uniform"),
    ("monotonous", "Advanced", "adjective", "dull and tedious"),
    ("moot", "Advanced", "adjective", "subject to debate"),
    ("morbid", "Advanced", "adjective", "having unhealthy interest"),
    ("mordant", "Expert", "adjective", "having sharp quality"),
    ("mores", "Advanced", "noun", "customs of a group"),
    ("moribund", "Expert", "adjective", "in terminal decline"),
    ("morose", "Advanced", "adjective", "sullen and ill-tempered"),
    ("mortify", "Advanced", "verb", "to cause to feel embarrassed"),
    ("motley", "Advanced", "adjective", "incongruously varied"),
    ("mourn", "Advanced", "verb", "to feel sorrow for death"),
    ("muddle", "Advanced", "verb", "to bring into confusion"),
    ("multifaceted", "Advanced", "adjective", "having many facets"),
    ("multifarious", "Expert", "adjective", "many and various"),
    ("mundane", "Advanced", "adjective", "lacking interest"),
    ("munificent", "Expert", "adjective", "very generous"),
    ("murky", "Advanced", "adjective", "dark and gloomy"),
    ("muse", "Advanced", "verb", "to be absorbed in thought"),
    ("muster", "Advanced", "verb", "to assemble troops"),
    ("musty", "Advanced", "adjective", "having stale smell"),
    ("mutable", "Advanced", "adjective", "liable to change"),
    ("muted", "Advanced", "adjective", "quiet and soft"),
    ("mutinous", "Advanced", "adjective", "refusing to obey orders"),
    ("myopic", "Advanced", "adjective", "lacking foresight"),
    ("myriad", "Advanced", "adjective", "countless or many"),
    ("mystify", "Advanced", "verb", "to utterly bewilder"),
    ("naive", "Advanced", "adjective", "lacking experience"),
    ("narcissist", "Advanced", "noun", "person with excessive self-interest"),
    ("narrative", "Advanced", "noun", "spoken or written account"),
    ("nascent", "Advanced", "adjective", "just beginning"),
    ("nauseous", "Advanced", "adjective", "feeling sick"),
    ("nebulous", "Advanced", "adjective", "unclear or vague"),
    ("nefarious", "Advanced", "adjective", "wicked or criminal"),
    ("negate", "Advanced", "verb", "to nullify or invalidate"),
    ("negligent", "Advanced", "adjective", "failing to take proper care"),
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
    start_id = 2001
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch23.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
