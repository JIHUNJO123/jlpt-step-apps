#!/usr/bin/env python3
"""N2 데이터 분석 및 병합"""

import json

# 새 Bluskyo 데이터 (공식 JLPT 기반)
with open('C:/Users/hooni/Desktop/jlpt_vocab_app/words_n2_final.json', 'r', encoding='utf-8') as f:
    bluskyo_data = json.load(f)

# 기존 앱 데이터
with open('C:/Users/hooni/Desktop/jlpt_vocab_app_n2/assets/data/words_n2.json', 'r', encoding='utf-8') as f:
    old_data = json.load(f)

print(f'Bluskyo N2: {len(bluskyo_data)} words')
print(f'기존 앱 N2: {len(old_data)} words')

# Bluskyo 단어들로 인덱스 만들기
bluskyo_words = {w['word'] for w in bluskyo_data}

# 기존 데이터에서 Bluskyo에 없는 단어들
extra_words = [w for w in old_data if w['word'] not in bluskyo_words]
print(f'기존 앱에만 있는 단어: {len(extra_words)}')

# 샘플 확인
print('\n기존 앱 데이터 샘플 (첫 5개):')
for w in old_data[:5]:
    print(f"  {w['word']} ({w.get('reading','')}) - {w.get('definition','')[:50]}")

# Bluskyo 데이터 샘플
print('\nBluskyo 데이터 샘플 (첫 5개):')
for w in bluskyo_data[:5]:
    print(f"  {w['word']} ({w.get('reading','')}) - {w.get('definition','')[:50]}")
