import json
import re
import os

def analyze_file(filepath):
    try:
        data = json.load(open(filepath, 'r', encoding='utf-8'))
        
        suspicious = []
        for word in data:
            ko_def = word.get('translations', {}).get('ko', {}).get('definition', '')
            
            # 영어가 포함된 경우
            if re.search(r'[a-zA-Z]{3,}', ko_def):
                suspicious.append({
                    'word': word['word'],
                    'ko': ko_def[:100],
                })
        
        return len(data), len(suspicious), suspicious
    except Exception as e:
        return 0, 0, str(e)

# 분석
files = [
    'assets/data/words.json',
    'assets/data/words_n5_n3.json',
]

for f in files:
    if os.path.exists(f):
        total, issues, samples = analyze_file(f)
        print(f"\n{f}: {total} words, {issues} issues")
        if isinstance(samples, list):
            for s in samples[:10]:
                print(f"  {s['word']}: {s['ko']}")
