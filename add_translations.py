#!/usr/bin/env python3
"""
N5-N3 데이터에 한국어/중국어 번역 추가
Google Translate API (무료) 사용
"""

import json
import urllib.request
import urllib.parse
import time

def translate_google(text, target_lang, source_lang='en'):
    """Google Translate 무료 API로 번역"""
    if not text:
        return ''
    
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_lang}&tl={target_lang}&dt=t&q={urllib.parse.quote(text)}"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            # 번역 결과 추출
            if data and data[0]:
                translated = ''.join([item[0] for item in data[0] if item[0]])
                return translated
    except Exception as e:
        print(f"번역 오류 ({text[:20]}...): {e}")
    
    return ''

def main():
    # 데이터 로드
    with open('assets/data/words_n5_n3.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f'총 단어 수: {len(data)}')
    
    # 번역 필요한 단어 수
    need_trans = [w for w in data if not w.get('translations') or not w['translations'].get('ko')]
    print(f'번역 필요한 단어: {len(need_trans)}')
    
    success_count = 0
    fail_count = 0
    
    for i, word in enumerate(need_trans):
        definition = word.get('definition', '')
        
        if not definition:
            fail_count += 1
            continue
        
        try:
            # 한국어 번역
            ko_trans = translate_google(definition, 'ko')
            # 중국어 번역
            zh_trans = translate_google(definition, 'zh-CN')
            
            if ko_trans or zh_trans:
                if 'translations' not in word:
                    word['translations'] = {}
                
                if ko_trans:
                    word['translations']['ko'] = {'definition': ko_trans}
                if zh_trans:
                    word['translations']['zh'] = {'definition': zh_trans}
                
                success_count += 1
            else:
                fail_count += 1
            
            if (i + 1) % 50 == 0:
                print(f'   {i + 1}/{len(need_trans)} (success: {success_count}, fail: {fail_count})', flush=True)
                # 중간 저장
                with open('assets/data/words_n5_n3.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
            
            time.sleep(0.3)  # Rate limit 방지
            
        except KeyboardInterrupt:
            print('\n사용자 중단! 저장 중...')
            with open('assets/data/words_n5_n3.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            raise
        except Exception as e:
            fail_count += 1
            print(f'오류: {e}')
            continue
    
    # 최종 저장
    with open('assets/data/words_n5_n3.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # 통계
    with_trans = sum(1 for w in data if w.get('translations') and w['translations'].get('ko'))
    print(f'\n완료: success={success_count}, fail={fail_count}')
    print(f'최종: {with_trans}/{len(data)} words with translations')

if __name__ == '__main__':
    main()
