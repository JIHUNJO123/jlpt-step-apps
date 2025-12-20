#!/usr/bin/env python3
"""N2/N1 데이터 분석"""

import json

def analyze_data(filepath, name):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f'\n=== {name} 데이터 분석 ===')
    print(f'총 단어: {len(data)}')
    
    # 필드 확인
    no_kanji = sum(1 for w in data if not w.get('kanji'))
    no_hiragana = sum(1 for w in data if not w.get('hiragana'))
    no_pos = sum(1 for w in data if not w.get('partOfSpeech'))
    no_trans = sum(1 for w in data if not w.get('translations'))
    
    print(f'kanji 없음: {no_kanji}')
    print(f'hiragana 없음: {no_hiragana}')
    print(f'partOfSpeech 없음: {no_pos}')
    print(f'translations 없음: {no_trans}')
    
    # 샘플
    print('\n샘플 (첫 3개):')
    for w in data[:3]:
        print(f"  word: {w.get('word')} | kanji: {w.get('kanji')} | hiragana: {w.get('hiragana')} | pos: {w.get('partOfSpeech')}")

# N2 분석
analyze_data('C:/Users/hooni/Desktop/jlpt_vocab_app_n2/assets/data/words_n2.json', 'N2')

# N1 분석
analyze_data('C:/Users/hooni/Desktop/jlpt_vocab_app_n1/assets/data/words_n1.json', 'N1')
