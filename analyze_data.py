#!/usr/bin/env python3
"""데이터 분석 스크립트"""

import json

with open('assets/data/words_n5_n3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 레벨별 카운트
levels = {}
for w in data:
    level = w.get('level', 'unknown')
    levels[level] = levels.get(level, 0) + 1

print('=== 레벨별 단어 수 ===')
for level in sorted(levels.keys()):
    print(f'{level}: {levels[level]}')
print(f'총: {len(data)}')

# 샘플 데이터 확인
print('\n=== 샘플 데이터 (첫 10개) ===')
for i, w in enumerate(data[:10]):
    print(f"--- 단어 {i+1} ---")
    print(f"  word: {w.get('word')}")
    print(f"  kanji: {w.get('kanji')}")
    print(f"  hiragana: {w.get('hiragana')}")
    print(f"  reading: {w.get('reading')}")
    print(f"  level: {w.get('level')}")
    print(f"  partOfSpeech: {w.get('partOfSpeech')}")
    print(f"  definition: {w.get('definition', '')[:50]}")

# 문제 분석: hiragana == word인 경우 (한자가 없는 경우)
print('\n=== 문제 분석 ===')
no_kanji = [w for w in data if w.get('word') == w.get('hiragana') or not w.get('kanji')]
print(f'한자가 없는 단어: {len(no_kanji)}개')

# 품사가 없는 경우
no_pos = [w for w in data if not w.get('partOfSpeech')]
print(f'품사가 없는 단어: {len(no_pos)}개')

# translations가 없는 경우
no_trans = [w for w in data if not w.get('translations')]
print(f'번역이 없는 단어: {len(no_trans)}개')

# word와 hiragana가 같은 샘플
print('\n=== word == hiragana 샘플 ===')
for w in data[:20]:
    if w.get('word') == w.get('hiragana'):
        print(f"  {w.get('word')} | kanji: {w.get('kanji')} | hiragana: {w.get('hiragana')}")
