import json
import requests
import time

API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

GRE_WORDS = [
    ("regale", "Advanced", "verb", "to entertain with stories"),
    ("regal", "Advanced", "adjective", "of or befitting royalty"),
    ("regime", "Advanced", "noun", "government in power"),
    ("regimen", "Advanced", "noun", "prescribed course"),
    ("rehabilitate", "Advanced", "verb", "to restore to normal life"),
    ("reimburse", "Advanced", "verb", "to repay money spent"),
    ("reiterate", "Advanced", "verb", "to say again"),
    ("relegate", "Advanced", "verb", "to consign to inferior position"),
    ("relent", "Advanced", "verb", "to abandon harsh intention"),
    ("relentless", "Advanced", "adjective", "oppressively constant"),
    ("relevant", "Advanced", "adjective", "closely connected to matter"),
    ("relic", "Advanced", "noun", "object surviving from earlier time"),
    ("relinquish", "Advanced", "verb", "to voluntarily give up"),
    ("relish", "Advanced", "verb", "to enjoy greatly"),
    ("reluctant", "Advanced", "adjective", "unwilling and hesitant"),
    ("remedial", "Advanced", "adjective", "giving remedy"),
    ("reminisce", "Advanced", "verb", "to indulge in enjoyable recollection"),
    ("remiss", "Advanced", "adjective", "lacking care or attention"),
    ("remonstrate", "Expert", "verb", "to make forceful protest"),
    ("remorse", "Advanced", "noun", "deep regret for wrongdoing"),
    ("renaissance", "Advanced", "noun", "revival of interest"),
    ("rend", "Expert", "verb", "to tear to pieces"),
    ("render", "Advanced", "verb", "to provide or give"),
    ("renege", "Advanced", "verb", "to go back on promise"),
    ("renounce", "Advanced", "verb", "to formally declare abandonment"),
    ("renovate", "Advanced", "verb", "to restore to good condition"),
    ("renown", "Advanced", "noun", "state of being famous"),
    ("repast", "Expert", "noun", "meal"),
    ("repeal", "Advanced", "verb", "to revoke or annul"),
    ("repel", "Advanced", "verb", "to drive back by force"),
    ("repertoire", "Advanced", "noun", "body of pieces one is prepared to perform"),
    ("replete", "Advanced", "adjective", "filled or well-supplied"),
    ("replicate", "Advanced", "verb", "to make exact copy"),
    ("repose", "Advanced", "noun", "state of rest"),
    ("reprehensible", "Advanced", "adjective", "deserving censure"),
    ("repress", "Advanced", "verb", "to subdue by force"),
    ("reprieve", "Advanced", "noun", "cancellation of punishment"),
    ("reprimand", "Advanced", "verb", "to rebuke formally"),
    ("reprisal", "Advanced", "noun", "act of retaliation"),
    ("reproach", "Advanced", "verb", "to express disapproval"),
    ("reprobate", "Expert", "noun", "unprincipled person"),
    ("repudiate", "Advanced", "verb", "to refuse to accept"),
    ("repugnant", "Advanced", "adjective", "extremely distasteful"),
    ("reputable", "Advanced", "adjective", "having good reputation"),
    ("requisite", "Advanced", "adjective", "made necessary"),
    ("rescind", "Advanced", "verb", "to revoke or cancel"),
    ("reserved", "Advanced", "adjective", "slow to reveal emotions"),
    ("residual", "Advanced", "adjective", "remaining after greater part is gone"),
    ("resilient", "Advanced", "adjective", "able to withstand difficulty"),
    ("resolute", "Advanced", "adjective", "admirably determined"),
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
    start_id = 2451
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
    with open("C:/Users/hooni/Desktop/gre_vocab_app/assets/data/words_batch28.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(words)} words")
