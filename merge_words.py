import json
import glob
import os

data_dir = "C:/Users/hooni/Desktop/gre_vocab_app/assets/data"
all_words = []

# 모든 words_ 파일 로드
for f in sorted(glob.glob(os.path.join(data_dir, "words_batch*.json"))):
    print(f"Loading: {os.path.basename(f)}")
    with open(f, "r", encoding="utf-8-sig") as file:
        words = json.load(file)
        all_words.extend(words)

# ID 재정렬
for i, word in enumerate(all_words):
    word["id"] = i + 1

# 메인 words.json 저장
with open(os.path.join(data_dir, "words.json"), "w", encoding="utf-8") as f:
    json.dump(all_words, f, ensure_ascii=False, indent=2)

print(f"\n총 {len(all_words)}개 단어 병합 완료!")
print(f"저장: {data_dir}/words.json")

# 레벨별 분류
advanced = [w for w in all_words if w.get("level") == "Advanced"]
expert = [w for w in all_words if w.get("level") == "Expert"]

print(f"Advanced: {len(advanced)}개")
print(f"Expert: {len(expert)}개")

# 레벨별 저장
with open(os.path.join(data_dir, "words_advanced.json"), "w", encoding="utf-8") as f:
    json.dump(advanced, f, ensure_ascii=False, indent=2)

with open(os.path.join(data_dir, "words_expert.json"), "w", encoding="utf-8") as f:
    json.dump(expert, f, ensure_ascii=False, indent=2)

print("레벨별 파일 저장 완료!")
