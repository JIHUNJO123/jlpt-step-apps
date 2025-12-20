import sqlite3
import json

# Load words from JSON
with open('assets/data/words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

print(f"Loaded {len(words)} words from JSON")

# Check level distribution in JSON
levels = {}
for word in words:
    level = word.get('level', 'Unknown')
    levels[level] = levels.get(level, 0) + 1
print(f"JSON level distribution: {levels}")

# Create database
conn = sqlite3.connect('assets/data/prebuilt_words.db')
cursor = conn.cursor()

# Create words table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL,
        definition TEXT NOT NULL,
        example TEXT NOT NULL,
        partOfSpeech TEXT NOT NULL,
        level TEXT NOT NULL,
        isFavorite INTEGER DEFAULT 0,
        translations TEXT
    )
''')

# Create translations table for quick lookup
cursor.execute('''
    CREATE TABLE IF NOT EXISTS translations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        wordId INTEGER NOT NULL,
        languageCode TEXT NOT NULL,
        fieldType TEXT NOT NULL,
        translatedText TEXT NOT NULL,
        FOREIGN KEY (wordId) REFERENCES words(id)
    )
''')

cursor.execute('''
    CREATE INDEX IF NOT EXISTS idx_translations_lookup
    ON translations(wordId, languageCode, fieldType)
''')

# Insert words and translations
for i, word in enumerate(words):
    word_id = i + 1
    cursor.execute('''
        INSERT INTO words (id, word, definition, example, partOfSpeech, level, isFavorite, translations)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        word_id,
        word['word'],
        word['definition'],
        word['example'],
        word['partOfSpeech'],
        word['level'],
        0,
        json.dumps(word.get('translations', {}))
    ))
    
    # Insert translations for each language
    translations = word.get('translations', {})
    for lang_code, lang_data in translations.items():
        if isinstance(lang_data, dict):
            definition = lang_data.get('definition', '')
            example = lang_data.get('example', '')
            
            if definition:
                cursor.execute('''
                    INSERT INTO translations (wordId, languageCode, fieldType, translatedText)
                    VALUES (?, ?, ?, ?)
                ''', (word_id, lang_code, 'definition', definition))
            
            if example:
                cursor.execute('''
                    INSERT INTO translations (wordId, languageCode, fieldType, translatedText)
                    VALUES (?, ?, ?, ?)
                ''', (word_id, lang_code, 'example', example))

conn.commit()

# Verify
cursor.execute("SELECT level, COUNT(*) FROM words GROUP BY level")
print(f"DB level distribution: {cursor.fetchall()}")

cursor.execute("SELECT COUNT(*) FROM words")
print(f"Total words in DB: {cursor.fetchone()[0]}")

cursor.execute("SELECT COUNT(*) FROM translations")
print(f"Total translations in DB: {cursor.fetchone()[0]}")

cursor.execute("SELECT languageCode, COUNT(*) FROM translations GROUP BY languageCode")
print(f"Translations by language: {cursor.fetchall()}")

conn.close()
print("Database created successfully!")
