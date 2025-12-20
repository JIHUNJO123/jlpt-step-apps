#!/usr/bin/env python3
"""
N2 데이터 병합: 기존 앱 데이터에 Bluskyo reading 추가
"""

import json

# 새 Bluskyo 데이터 (공식 JLPT 기반)
with open('C:/Users/hooni/Desktop/jlpt_vocab_app/words_n2_final.json', 'r', encoding='utf-8') as f:
    bluskyo_data = json.load(f)

# 기존 앱 데이터
with open('C:/Users/hooni/Desktop/jlpt_vocab_app_n2/assets/data/words_n2.json', 'r', encoding='utf-8') as f:
    old_data = json.load(f)

# Bluskyo 인덱스 (단어 -> reading, definition)
bluskyo_index = {}
for w in bluskyo_data:
    bluskyo_index[w['word']] = {
        'reading': w.get('reading', ''),
        'definition': w.get('definition', '')
    }

print(f'기존 N2 데이터: {len(old_data)} 단어')
print(f'Bluskyo N2 데이터: {len(bluskyo_data)} 단어')

# 기존 데이터에 Bluskyo reading 추가
updated_count = 0
for word in old_data:
    word_text = word['word']
    if word_text in bluskyo_index:
        bluskyo_info = bluskyo_index[word_text]
        # reading이 비어있으면 Bluskyo에서 가져오기
        if not word.get('reading') and bluskyo_info['reading']:
            word['reading'] = bluskyo_info['reading']
            updated_count += 1
        # definition이 비어있으면 Bluskyo에서 가져오기  
        if not word.get('definition') and bluskyo_info['definition']:
            word['definition'] = bluskyo_info['definition']
            updated_count += 1

print(f'업데이트된 항목: {updated_count}')

# Bluskyo에만 있는 단어들 추가
old_words = {w['word'] for w in old_data}
new_words = [w for w in bluskyo_data if w['word'] not in old_words]
print(f'새로 추가할 단어: {len(new_words)}')

# 새 단어들을 level=N2로 설정
for w in new_words:
    w['level'] = 'N2'

# 병합
merged = old_data + new_words
print(f'최종 병합 데이터: {len(merged)} 단어')

# 저장
output_path = 'C:/Users/hooni/Desktop/jlpt_vocab_app_n2/assets/data/words_n2_merged.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

print(f'저장: {output_path}')

# 통계
with_reading = sum(1 for w in merged if w.get('reading'))
with_def = sum(1 for w in merged if w.get('definition'))
print(f'reading 있는 단어: {with_reading}/{len(merged)}')
print(f'definition 있는 단어: {with_def}/{len(merged)}')
