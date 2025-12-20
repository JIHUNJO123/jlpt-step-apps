import json
from deep_translator import GoogleTranslator
import time

def translate_word(definition, target_lang):
    """Translate definition to target language"""
    try:
        translator = GoogleTranslator(source='en', target=target_lang)
        result = translator.translate(definition)
        return result
    except Exception as e:
        print(f"Error translating to {target_lang}: {e}")
        return None

def main():
    # Load words
    with open('assets/data/words.json', 'r', encoding='utf-8') as f:
        words = json.load(f)
    
    print(f"Total words: {len(words)}")
    
    # Count words needing translation
    needs_trans = [w for w in words if 'SAT vocabulary word' in w.get('translations', {}).get('ko', {}).get('definition', '')]
    print(f"Words needing translation: {len(needs_trans)}")
    
    # Process each word
    for i, word in enumerate(words):
        ko_def = word.get('translations', {}).get('ko', {}).get('definition', '')
        
        if 'SAT vocabulary word' in ko_def:
            definition = word['definition']
            
            # Translate to each language
            ko_trans = translate_word(definition, 'ko')
            zh_trans = translate_word(definition, 'zh-CN')
            hi_trans = translate_word(definition, 'hi')
            
            if ko_trans and zh_trans and hi_trans:
                word['translations'] = {
                    'ko': {'definition': ko_trans},
                    'zh': {'definition': zh_trans},
                    'hi': {'definition': hi_trans}
                }
                print(f"[{i+1}/{len(words)}] {word['word']}: {ko_trans}")
            else:
                print(f"[{i+1}/{len(words)}] {word['word']}: FAILED")
            
            # Save progress every 50 words
            if (i + 1) % 50 == 0:
                with open('assets/data/words.json', 'w', encoding='utf-8') as f:
                    json.dump(words, f, ensure_ascii=False, indent=2)
                print(f"Saved progress at {i+1} words")
            
            # Small delay to avoid rate limiting
            time.sleep(0.2)
    
    # Final save
    with open('assets/data/words.json', 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    
    print("\nTranslation complete!")
    
    # Verify
    ok_count = sum(1 for w in words if 'SAT vocabulary word' not in w.get('translations', {}).get('ko', {}).get('definition', ''))
    print(f"Words with proper translations: {ok_count}/{len(words)}")

if __name__ == "__main__":
    main()
