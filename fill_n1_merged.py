#!/usr/bin/env python3
"""
병합된 N1 데이터에서 빈 정의를 Jisho API로 채우기
"""

import json
import urllib.request
import urllib.parse
import time
import socket

def fetch_jisho_word(word, retries=3):
    """Jisho API에서 단어 정보 가져오기"""
    url = f"https://jisho.org/api/v1/search/words?keyword={urllib.parse.quote(word)}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    req = urllib.request.Request(url, headers=headers)
    
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=20) as response:
                data = json.loads(response.read().decode('utf-8'))
                
                if data['data']:
                    entry = data['data'][0]
                    word_text = entry['japanese'][0].get('word', '')
                    reading = entry['japanese'][0].get('reading', '')
                    
                    meanings = []
                    for sense in entry['senses'][:3]:
                        for gloss in sense.get('english_definitions', [])[:3]:
                            if gloss not in meanings:
                                meanings.append(gloss)
                    
                    definition = '; '.join(meanings[:6]) if meanings else ''
                    
                    return {
                        'word': word_text if word_text else word,
                        'reading': reading,
                        'definition': definition
                    }
                return None
                
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(1)
                continue
            return None
    
    return None

def main():
    input_file = 'C:/Users/hooni/Desktop/jlpt_vocab_app_n1/assets/data/words_n1_merged.json'
    output_file = 'C:/Users/hooni/Desktop/jlpt_vocab_app_n1/assets/data/words_n1_filled.json'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        words = json.load(f)
    
    print(f"총 단어: {len(words)}")
    
    # 정의가 없는 단어만 처리
    to_process = [w for w in words if not w.get('definition')]
    print(f"정의가 필요한 단어: {len(to_process)}")
    
    if not to_process:
        print("모든 단어에 정의가 있습니다!")
        return
    
    success_count = 0
    fail_count = 0
    
    for i, entry in enumerate(to_process):
        word = entry['word']
        
        try:
            result = fetch_jisho_word(word)
            
            if result and result['definition']:
                entry['definition'] = result['definition']
                if not entry.get('reading') and result['reading']:
                    entry['reading'] = result['reading']
                if not entry.get('hiragana') and result['reading']:
                    entry['hiragana'] = result['reading']
                success_count += 1
            else:
                fail_count += 1
            
            if (i + 1) % 50 == 0:
                print(f"   {i + 1}/{len(to_process)} (success: {success_count}, fail: {fail_count})", flush=True)
                # 중간 저장
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(words, f, ensure_ascii=False, indent=2)
            
            time.sleep(0.2)
            
        except KeyboardInterrupt:
            print("\n사용자 중단! 저장 중...")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(words, f, ensure_ascii=False, indent=2)
            raise
        except Exception as e:
            fail_count += 1
            continue
    
    # 최종 저장
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    
    # 통계
    with_def = sum(1 for w in words if w.get('definition'))
    print(f"완료: success={success_count}, fail={fail_count}")
    print(f"최종: {with_def}/{len(words)} words with definitions")
    print(f"저장: {output_file}")

if __name__ == '__main__':
    main()
