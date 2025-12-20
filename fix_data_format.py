#!/usr/bin/env python3
"""
N5-N3 데이터 수정:
1. kanji 필드 추가 (word가 한자인 경우)
2. hiragana 필드 추가 (reading에서 가져옴)
3. partOfSpeech 필드 기본값 설정
4. 앱 형식에 맞게 변환
"""

import json
import re

# 한자 패턴 (CJK 통합 한자)
KANJI_PATTERN = re.compile(r'[\u4e00-\u9fff]')

def has_kanji(text):
    """문자열에 한자가 포함되어 있는지 확인"""
    if not text:
        return False
    return bool(KANJI_PATTERN.search(text))

def fix_word_data(word_data):
    """단어 데이터 수정"""
    word = word_data.get('word', '')
    reading = word_data.get('reading', '')
    
    # kanji: word가 한자를 포함하면 word, 아니면 빈 문자열
    if has_kanji(word):
        word_data['kanji'] = word
    else:
        word_data['kanji'] = ''
    
    # hiragana: reading 값 사용
    word_data['hiragana'] = reading
    
    # partOfSpeech: 빈 문자열로 설정 (unknown 대신)
    if not word_data.get('partOfSpeech'):
        word_data['partOfSpeech'] = ''
    
    # example: 없으면 빈 문자열
    if not word_data.get('example'):
        word_data['example'] = ''
    
    # category: 없으면 General
    if not word_data.get('category'):
        word_data['category'] = 'General'
    
    # translations: 없으면 빈 객체
    if not word_data.get('translations'):
        word_data['translations'] = {}
    
    return word_data

# 데이터 로드
with open('assets/data/words_n5_n3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f'총 단어 수: {len(data)}')

# 데이터 수정
fixed_data = []
for i, word in enumerate(data):
    fixed_word = fix_word_data(word)
    # id 추가 (없는 경우)
    if 'id' not in fixed_word:
        fixed_word['id'] = i + 1
    fixed_data.append(fixed_word)

# 레벨별 카운트
levels = {}
for w in fixed_data:
    level = w.get('level', 'unknown')
    levels[level] = levels.get(level, 0) + 1

print('\n=== 수정 후 레벨별 단어 수 ===')
for level in sorted(levels.keys()):
    print(f'{level}: {levels[level]}')

# 샘플 확인
print('\n=== 수정 후 샘플 (첫 5개) ===')
for w in fixed_data[:5]:
    print(f"  word: {w['word']} | kanji: {w['kanji']} | hiragana: {w['hiragana']} | pos: {w['partOfSpeech']}")

# 한자 있는 단어 수
with_kanji = sum(1 for w in fixed_data if w['kanji'])
print(f'\n한자 있는 단어: {with_kanji}/{len(fixed_data)}')

# 저장
with open('assets/data/words_n5_n3.json', 'w', encoding='utf-8') as f:
    json.dump(fixed_data, f, ensure_ascii=False, indent=2)

print('\n저장 완료: assets/data/words_n5_n3.json')
