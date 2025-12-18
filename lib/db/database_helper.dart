import 'dart:convert';
import 'package:flutter/services.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import '../models/word.dart';

class DatabaseHelper {
  static final DatabaseHelper instance = DatabaseHelper._init();
  static Database? _database;

  DatabaseHelper._init();

  Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _initDB('gre_words.db');
    return _database!;
  }

  Future<Database> _initDB(String filePath) async {
    final dbPath = await getDatabasesPath();
    final path = join(dbPath, filePath);

    return await openDatabase(
      path,
      version: 2,
      onCreate: _createDB,
      onUpgrade: _upgradeDB,
    );
  }

  Future _createDB(Database db, int version) async {
    // ?¨ì–´ ?Œì´ë¸?(?´ì¥ ë²ˆì—­ ?¬í•¨)
    await db.execute('''
      CREATE TABLE words (
        id INTEGER PRIMARY KEY,
        word TEXT NOT NULL,
        level TEXT NOT NULL,
        partOfSpeech TEXT NOT NULL,
        definition TEXT NOT NULL,
        example TEXT NOT NULL,
        category TEXT DEFAULT 'General',
        isFavorite INTEGER DEFAULT 0,
        translations TEXT
      )
    ''');

    // ë²ˆì—­ ìºì‹œ ?Œì´ë¸?
    await db.execute('''
      CREATE TABLE translations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        wordId INTEGER NOT NULL,
        languageCode TEXT NOT NULL,
        fieldType TEXT NOT NULL,
        translatedText TEXT NOT NULL,
        createdAt INTEGER NOT NULL,
        UNIQUE(wordId, languageCode, fieldType)
      )
    ''');

    // ?¸ë±???ì„±
    await db.execute('''
      CREATE INDEX idx_translations_lookup 
      ON translations(wordId, languageCode, fieldType)
    ''');

    // Load initial data from JSON
    await _loadInitialData(db);
  }

  Future _upgradeDB(Database db, int oldVersion, int newVersion) async {
    // ??ƒ ?¬ìƒ?±í•˜???´ì¥ ë²ˆì—­ ?¬í•¨
    await db.execute('DROP TABLE IF EXISTS words');
    await db.execute('DROP TABLE IF EXISTS translations');
    await _createDB(db, newVersion);
  }

  Future<void> _loadInitialData(Database db) async {
    try {
      final String response = await rootBundle.loadString(
        'assets/data/words.json',
      );
      final List<dynamic> data = json.decode(response);

      for (var wordJson in data) {
        // translationsë¥?JSON ë¬¸ì?´ë¡œ ?€??
        String? translationsJson;
        if (wordJson['translations'] != null) {
          translationsJson = json.encode(wordJson['translations']);
        }

        await db.insert('words', {
          'id': wordJson['id'],
          'word': wordJson['word'],
          'level': wordJson['level'],
          'partOfSpeech': wordJson['partOfSpeech'],
          'definition': wordJson['definition'],
          'example': wordJson['example'],
          'category': wordJson['category'] ?? 'General',
          'isFavorite': 0,
          'translations': translationsJson,
        });
      }
      print('Loaded ${data.length} GRE words successfully');
    } catch (e) {
      print('Error loading initial data: $e');
    }
  }

  // ============ ë²ˆì—­ ìºì‹œ ë©”ì„œ??============

  /// ë²ˆì—­ ìºì‹œ?ì„œ ê°€?¸ì˜¤ê¸?
  Future<String?> getTranslation(
    int wordId,
    String languageCode,
    String fieldType,
  ) async {
    final db = await instance.database;
    final result = await db.query(
      'translations',
      columns: ['translatedText'],
      where: 'wordId = ? AND languageCode = ? AND fieldType = ?',
      whereArgs: [wordId, languageCode, fieldType],
    );
    if (result.isNotEmpty) {
      return result.first['translatedText'] as String;
    }
    return null;
  }

  /// ë²ˆì—­ ìºì‹œ???€??
  Future<void> saveTranslation(
    int wordId,
    String languageCode,
    String fieldType,
    String translatedText,
  ) async {
    final db = await instance.database;
    await db.insert('translations', {
      'wordId': wordId,
      'languageCode': languageCode,
      'fieldType': fieldType,
      'translatedText': translatedText,
      'createdAt': DateTime.now().millisecondsSinceEpoch,
    }, conflictAlgorithm: ConflictAlgorithm.replace);
  }

  /// ?¹ì • ?¸ì–´??ëª¨ë“  ë²ˆì—­ ?? œ
  Future<void> clearTranslations(String languageCode) async {
    final db = await instance.database;
    await db.delete(
      'translations',
      where: 'languageCode = ?',
      whereArgs: [languageCode],
    );
  }

  /// ëª¨ë“  ë²ˆì—­ ìºì‹œ ?? œ
  Future<void> clearAllTranslations() async {
    final db = await instance.database;
    await db.delete('translations');
  }

  // ============ ?¨ì–´ ë©”ì„œ??============

  Future<List<Word>> getAllWords() async {
    final db = await instance.database;
    final result = await db.query('words', orderBy: 'word ASC');
    return result.map((json) => Word.fromDb(json)).toList();
  }

  Future<List<Word>> getWordsByLevel(String level) async {
    final db = await instance.database;
    final result = await db.query(
      'words',
      where: 'level = ?',
      whereArgs: [level],
      orderBy: 'word ASC',
    );
    return result.map((json) => Word.fromDb(json)).toList();
  }

  Future<List<Word>> getWordsByCategory(String category) async {
    final db = await instance.database;
    final result = await db.query(
      'words',
      where: 'category = ?',
      whereArgs: [category],
      orderBy: 'word ASC',
    );
    return result.map((json) => Word.fromDb(json)).toList();
  }

  Future<List<String>> getAllCategories() async {
    final db = await instance.database;
    final result = await db.rawQuery(
      'SELECT DISTINCT category FROM words ORDER BY category ASC',
    );
    return result.map((row) => row['category'] as String).toList();
  }

  Future<List<Word>> getFavorites() async {
    final db = await instance.database;
    final result = await db.query(
      'words',
      where: 'isFavorite = ?',
      whereArgs: [1],
      orderBy: 'word ASC',
    );
    return result.map((json) => Word.fromDb(json)).toList();
  }

  Future<List<Word>> searchWords(String query) async {
    final db = await instance.database;
    final result = await db.query(
      'words',
      where: 'word LIKE ? OR definition LIKE ?',
      whereArgs: ['%$query%', '%$query%'],
      orderBy: 'word ASC',
    );
    return result.map((json) => Word.fromDb(json)).toList();
  }

  Future<void> toggleFavorite(int id, bool isFavorite) async {
    final db = await instance.database;
    await db.update(
      'words',
      {'isFavorite': isFavorite ? 1 : 0},
      where: 'id = ?',
      whereArgs: [id],
    );
  }

  Future<Word?> getWordById(int id) async {
    final db = await instance.database;
    final result = await db.query('words', where: 'id = ?', whereArgs: [id]);
    if (result.isEmpty) return null;
    return Word.fromDb(result.first);
  }

  Future<Word?> getRandomWord() async {
    final db = await instance.database;
    final result = await db.rawQuery(
      'SELECT * FROM words ORDER BY RANDOM() LIMIT 1',
    );
    if (result.isEmpty) return null;
    return Word.fromDb(result.first);
  }

  // JSON ?°ì´??ìºì‹œ (?´ì¥ ë²ˆì—­ ?¬í•¨)
  List<Word>? _jsonWordsCache;

  /// JSON ìºì‹œ ?´ë¦¬??(??ë¦¬ë¡œ?????¬ìš©)
  void clearJsonCache() {
    _jsonWordsCache = null;
  }

  /// JSON ?Œì¼?ì„œ ëª¨ë“  ?¨ì–´ ë¡œë“œ (?´ì¥ ë²ˆì—­ ?¬í•¨)
  /// ë²ˆì—­???ˆëŠ” ?Œì¼(band*.json)??ë¨¼ì? ë¡œë“œ?´ì„œ ë²ˆì—­ ?°ì´???°ì„ 
  Future<List<Word>> _loadWordsFromJson() async {
    // ìºì‹œ ë¬´ì‹œ?˜ê³  ??ƒ ?ˆë¡œ ë¡œë“œ (?”ë²„ê¹…ìš©)
    // if (_jsonWordsCache != null) return _jsonWordsCache!;

    try {
      final List<Word> allWords = [];
      // ë²ˆì—­???ˆëŠ” ?Œì¼??ë¨¼ì? ë¡œë“œ! (band*.json??ë²ˆì—­ ?°ì´???ˆìŒ)
      final jsonFiles = [
        'assets/data/basic_words.json',
        'assets/data/common_words.json',
        'assets/data/advanced_words.json',
        'assets/data/expert_words.json',
        'assets/data/words_batch2.json',
        'assets/data/words.json', // ë²ˆì—­ ?†ëŠ” ?Œì¼?€ ë§ˆì?ë§‰ì—
      ];

      for (final file in jsonFiles) {
        try {
          print('Loading JSON file: $file');
          final String response = await rootBundle.loadString(file);
          final List<dynamic> data = json.decode(response);
          final words = data.map((json) => Word.fromJson(json)).toList();
          print('  Loaded ${words.length} words from $file');
          // ì²?ë²ˆì§¸ ?¨ì–´??ë²ˆì—­ ?•ì¸
          if (words.isNotEmpty && words.first.translations != null) {
            print(
              '  First word has translations: ${words.first.translations!.keys}',
            );
          }
          allWords.addAll(words);
        } catch (e) {
          print('Error loading $file: $e');
        }
      }

      print('Total JSON words loaded: ${allWords.length}');
      _jsonWordsCache = allWords;
      return allWords;
    } catch (e) {
      print('Error loading JSON words: $e');
      return [];
    }
  }

  /// ?¨ì–´ ì°¾ê¸° (ë²ˆì—­???ˆëŠ” ?¨ì–´ ?°ì„ )
  Word? _findWordWithTranslation(List<Word> jsonWords, Word dbWord) {
    // ê°™ì? ?¨ì–´ëª…ìœ¼ë¡?ë§¤ì¹­?˜ëŠ” ëª¨ë“  ?¨ì–´ ì°¾ê¸°
    final matches =
        jsonWords
            .where((w) => w.word.toLowerCase() == dbWord.word.toLowerCase())
            .toList();

    print('=== _findWordWithTranslation ===');
    print('Looking for: ${dbWord.word}');
    print('Found ${matches.length} matches');

    if (matches.isEmpty) return null;

    // ë²ˆì—­???ˆëŠ” ?¨ì–´ ?°ì„  ë°˜í™˜
    for (final word in matches) {
      if (word.translations != null && word.translations!.isNotEmpty) {
        print('Found word with translations: ${word.translations!.keys}');
        return word;
      }
    }

    print('No word with translations found');
    // ë²ˆì—­ ?†ìœ¼ë©?ì²?ë²ˆì§¸ ë°˜í™˜
    return matches.first;
  }

  /// ëª¨ë“  ?¨ì–´ ê°€?¸ì˜¤ê¸?(?´ì¥ ë²ˆì—­ ?¬í•¨) - ?´ì¦ˆ??
  Future<List<Word>> getWordsWithTranslations() async {
    final db = await instance.database;
    final dbResult = await db.query('words', orderBy: 'word ASC');
    final dbWords = dbResult.map((json) => Word.fromDb(json)).toList();

    // JSON?ì„œ ?´ì¥ ë²ˆì—­ ë¡œë“œ
    final jsonWords = await _loadWordsFromJson();

    // DB ?¨ì–´??JSON??ë²ˆì—­ ?°ì´??ë³‘í•© (ë²ˆì—­ ?ˆëŠ” ?¨ì–´ ?°ì„ )
    return dbWords.map((dbWord) {
      final jsonWord = _findWordWithTranslation(jsonWords, dbWord) ?? dbWord;
      return dbWord.copyWith(translations: jsonWord.translations);
    }).toList();
  }

  /// ?¤ëŠ˜???¨ì–´ (?´ì¥ ë²ˆì—­ ?¬í•¨)
  Future<Word?> getTodayWord() async {
    try {
      final db = await instance.database;
      // Use date as seed for consistent daily word
      final today = DateTime.now();
      final seed = today.year * 10000 + today.month * 100 + today.day;
      final count =
          Sqflite.firstIntValue(
            await db.rawQuery('SELECT COUNT(*) FROM words'),
          ) ??
          0;

      if (count == 0) {
        print('No words in database');
        return null;
      }

      final index = seed % count;

      final result = await db.rawQuery('SELECT * FROM words LIMIT 1 OFFSET ?', [
        index,
      ]);
      if (result.isEmpty) return null;

      final dbWord = Word.fromDb(result.first);
      print('=== getTodayWord Debug ===');
      print('DB Word: ${dbWord.word}');

      // JSON?ì„œ ?´ì¥ ë²ˆì—­ ì°¾ê¸° (ë²ˆì—­ ?ˆëŠ” ?¨ì–´ ?°ì„ )
      final jsonWords = await _loadWordsFromJson();
      print('JSON words loaded: ${jsonWords.length}');

      final jsonWord = _findWordWithTranslation(jsonWords, dbWord);
      print('Found jsonWord: ${jsonWord != null}');
      print('jsonWord translations: ${jsonWord?.translations}');

      final finalWord = jsonWord ?? dbWord;

      // DB??isFavorite ?íƒœ?€ JSON??ë²ˆì—­ ?°ì´??ë³‘í•©
      final result2 = dbWord.copyWith(translations: finalWord.translations);
      print('Final word translations: ${result2.translations}');
      return result2;
    } catch (e) {
      print('Error getting today word: $e');
      return null;
    }
  }

  /// ?ˆë²¨ë³??¨ì–´ ??ê°€?¸ì˜¤ê¸?
  Future<Map<String, int>> getWordCountByLevel() async {
    final db = await instance.database;
    final result = await db.rawQuery(
      'SELECT level, COUNT(*) as count FROM words GROUP BY level',
    );
    final Map<String, int> counts = {};
    for (var row in result) {
      counts[row['level'] as String] = row['count'] as int;
    }
    return counts;
  }

  /// ?¨ì–´??ë²ˆì—­ ?°ì´???ìš©
  Future<Word> applyTranslations(Word word, String languageCode) async {
    if (languageCode == 'en') return word;

    final translatedDef = await getTranslation(
      word.id,
      languageCode,
      'definition',
    );
    final translatedEx = await getTranslation(word.id, languageCode, 'example');

    return word.copyWith(
      translatedDefinition: translatedDef,
      translatedExample: translatedEx,
    );
  }

  /// ?¬ëŸ¬ ?¨ì–´??ë²ˆì—­ ?ìš©
  Future<List<Word>> applyTranslationsToList(
    List<Word> words,
    String languageCode,
  ) async {
    if (languageCode == 'en') return words;

    final result = <Word>[];
    for (final word in words) {
      result.add(await applyTranslations(word, languageCode));
    }
    return result;
  }

  Future close() async {
    final db = await instance.database;
    db.close();
  }
}
