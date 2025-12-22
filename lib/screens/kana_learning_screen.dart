import 'package:flutter/material.dart';
import 'dart:math';
import '../data/kana_data.dart';
import 'package:jlpt_vocab_app/l10n/generated/app_localizations.dart';

class KanaLearningScreen extends StatefulWidget {
  final bool isKatakana;

  const KanaLearningScreen({super.key, this.isKatakana = false});

  @override
  State<KanaLearningScreen> createState() => _KanaLearningScreenState();
}

class _KanaLearningScreenState extends State<KanaLearningScreen>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;
  bool _showRomaji = true;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 3, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context)!;
    final title = widget.isKatakana ? l10n.katakana : l10n.hiragana;

    return Scaffold(
      appBar: AppBar(
        title: Text(title),
        actions: [
          IconButton(
            icon: Icon(_showRomaji ? Icons.visibility : Icons.visibility_off),
            onPressed: () {
              setState(() {
                _showRomaji = !_showRomaji;
              });
            },
            tooltip: l10n.showRomaji,
          ),
        ],
        bottom: TabBar(
          controller: _tabController,
          tabs: [
            Tab(text: l10n.chart),
            Tab(text: l10n.flashcard),
            Tab(text: l10n.quiz),
          ],
        ),
      ),
      body: TabBarView(
        controller: _tabController,
        children: [_buildChartTab(), _buildFlashcardTab(), _buildQuizTab()],
      ),
    );
  }

  Widget _buildChartTab() {
    final l10n = AppLocalizations.of(context)!;

    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        // 기본 가나 (청음)
        _buildSectionHeader(l10n.basicKana),
        const SizedBox(height: 8),
        ...List.generate(KanaData.basicRows.length, (index) {
          return _buildKanaRow(
            KanaData.rowNames[index],
            KanaData.basicRows[index],
          );
        }),

        const SizedBox(height: 24),

        // 탁음/반탁음
        _buildSectionHeader(l10n.dakutenKana),
        const SizedBox(height: 8),
        ...List.generate(KanaData.dakutenRows.length, (index) {
          return _buildKanaRow(
            KanaData.dakutenRowNames[index],
            KanaData.dakutenRows[index],
          );
        }),
      ],
    );
  }

  Widget _buildSectionHeader(String title) {
    return Container(
      padding: const EdgeInsets.symmetric(vertical: 8, horizontal: 12),
      decoration: BoxDecoration(
        color: Theme.of(context).primaryColor.withAlpha(30),
        borderRadius: BorderRadius.circular(8),
      ),
      child: Text(
        title,
        style: TextStyle(
          fontSize: 18,
          fontWeight: FontWeight.bold,
          color: Theme.of(context).primaryColor,
        ),
      ),
    );
  }

  Widget _buildKanaRow(String rowName, List<KanaCharacter> characters) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Padding(
          padding: const EdgeInsets.symmetric(vertical: 8),
          child: Text(
            rowName,
            style: const TextStyle(
              fontWeight: FontWeight.w600,
              fontSize: 14,
              color: Colors.grey,
            ),
          ),
        ),
        Wrap(
          spacing: 8,
          runSpacing: 8,
          children: characters.map((kana) => _buildKanaCard(kana)).toList(),
        ),
        const SizedBox(height: 8),
      ],
    );
  }

  Widget _buildKanaCard(KanaCharacter kana) {
    final displayChar = widget.isKatakana ? kana.katakana : kana.hiragana;

    return GestureDetector(
      onTap: () => _showKanaDetail(kana),
      child: Container(
        width: 60,
        height: 75,
        decoration: BoxDecoration(
          color: Theme.of(context).cardColor,
          borderRadius: BorderRadius.circular(8),
          border: Border.all(color: Theme.of(context).dividerColor),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withAlpha(10),
              blurRadius: 4,
              offset: const Offset(0, 2),
            ),
          ],
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              displayChar,
              style: const TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
            ),
            if (_showRomaji)
              Text(
                kana.romaji,
                style: TextStyle(fontSize: 12, color: Colors.grey[600]),
              ),
          ],
        ),
      ),
    );
  }

  void _showKanaDetail(KanaCharacter kana) {
    showDialog(
      context: context,
      builder:
          (context) => AlertDialog(
            content: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                    Column(
                      children: [
                        const Text(
                          'ひらがな',
                          style: TextStyle(fontSize: 12, color: Colors.grey),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          kana.hiragana,
                          style: const TextStyle(
                            fontSize: 48,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                    Column(
                      children: [
                        const Text(
                          'カタカナ',
                          style: TextStyle(fontSize: 12, color: Colors.grey),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          kana.katakana,
                          style: const TextStyle(
                            fontSize: 48,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
                const SizedBox(height: 16),
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 24,
                    vertical: 8,
                  ),
                  decoration: BoxDecoration(
                    color: Theme.of(context).primaryColor.withAlpha(30),
                    borderRadius: BorderRadius.circular(20),
                  ),
                  child: Text(
                    kana.romaji,
                    style: TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                      color: Theme.of(context).primaryColor,
                    ),
                  ),
                ),
              ],
            ),
            actions: [
              TextButton(
                onPressed: () => Navigator.pop(context),
                child: const Text('OK'),
              ),
            ],
          ),
    );
  }

  Widget _buildFlashcardTab() {
    return _KanaFlashcard(isKatakana: widget.isKatakana);
  }

  Widget _buildQuizTab() {
    return _KanaQuiz(isKatakana: widget.isKatakana);
  }
}

class _KanaFlashcard extends StatefulWidget {
  final bool isKatakana;

  const _KanaFlashcard({required this.isKatakana});

  @override
  State<_KanaFlashcard> createState() => _KanaFlashcardState();
}

class _KanaFlashcardState extends State<_KanaFlashcard> {
  late List<KanaCharacter> _shuffledKana;
  int _currentIndex = 0;
  bool _showAnswer = false;

  @override
  void initState() {
    super.initState();
    _shuffleKana();
  }

  void _shuffleKana() {
    _shuffledKana = List.from(KanaData.allKana)..shuffle();
    _currentIndex = 0;
    _showAnswer = false;
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context)!;

    if (_currentIndex >= _shuffledKana.length) {
      return Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Icon(Icons.celebration, size: 64, color: Colors.amber),
            const SizedBox(height: 16),
            Text(
              l10n.completed,
              style: const TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 24),
            ElevatedButton.icon(
              onPressed: () {
                setState(() {
                  _shuffleKana();
                });
              },
              icon: const Icon(Icons.refresh),
              label: Text(l10n.tryAgain),
            ),
          ],
        ),
      );
    }

    final kana = _shuffledKana[_currentIndex];
    final displayChar = widget.isKatakana ? kana.katakana : kana.hiragana;

    return Padding(
      padding: const EdgeInsets.all(24),
      child: Column(
        children: [
          // Progress
          LinearProgressIndicator(
            value: (_currentIndex + 1) / _shuffledKana.length,
          ),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 8),
            child: Text(
              '${_currentIndex + 1} / ${_shuffledKana.length}',
              style: const TextStyle(color: Colors.grey),
            ),
          ),

          const Spacer(),

          // Flashcard
          GestureDetector(
            onTap: () {
              setState(() {
                _showAnswer = !_showAnswer;
              });
            },
            child: AnimatedContainer(
              duration: const Duration(milliseconds: 300),
              width: double.infinity,
              height: 300,
              decoration: BoxDecoration(
                color:
                    _showAnswer
                        ? Theme.of(context).primaryColor.withAlpha(30)
                        : Theme.of(context).cardColor,
                borderRadius: BorderRadius.circular(20),
                boxShadow: [
                  BoxShadow(
                    color: Colors.black.withAlpha(20),
                    blurRadius: 10,
                    offset: const Offset(0, 5),
                  ),
                ],
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    displayChar,
                    style: const TextStyle(
                      fontSize: 100,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  if (_showAnswer) ...[
                    const SizedBox(height: 16),
                    Text(
                      kana.romaji,
                      style: TextStyle(
                        fontSize: 32,
                        color: Theme.of(context).primaryColor,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ] else ...[
                    const SizedBox(height: 16),
                    Text(
                      l10n.tapToReveal,
                      style: const TextStyle(color: Colors.grey),
                    ),
                  ],
                ],
              ),
            ),
          ),

          const Spacer(),

          // Navigation
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              ElevatedButton.icon(
                onPressed:
                    _currentIndex > 0
                        ? () {
                          setState(() {
                            _currentIndex--;
                            _showAnswer = false;
                          });
                        }
                        : null,
                icon: const Icon(Icons.arrow_back),
                label: Text(l10n.previous),
              ),
              ElevatedButton.icon(
                onPressed: () {
                  setState(() {
                    _currentIndex++;
                    _showAnswer = false;
                  });
                },
                icon: const Icon(Icons.arrow_forward),
                label: Text(l10n.next),
              ),
            ],
          ),
          const SizedBox(height: 16),
        ],
      ),
    );
  }
}

class _KanaQuiz extends StatefulWidget {
  final bool isKatakana;

  const _KanaQuiz({required this.isKatakana});

  @override
  State<_KanaQuiz> createState() => _KanaQuizState();
}

class _KanaQuizState extends State<_KanaQuiz> {
  late List<KanaCharacter> _questions;
  int _currentIndex = 0;
  int _score = 0;
  String? _selectedAnswer;
  bool _answered = false;
  final Random _random = Random();

  @override
  void initState() {
    super.initState();
    _startQuiz();
  }

  void _startQuiz() {
    _questions = List.from(KanaData.allKana)..shuffle();
    _questions = _questions.take(20).toList(); // 20문제
    _currentIndex = 0;
    _score = 0;
    _selectedAnswer = null;
    _answered = false;
  }

  List<String> _generateOptions(KanaCharacter correctKana) {
    final correctAnswer = correctKana.romaji;
    final options = <String>{correctAnswer};

    final allRomaji = KanaData.allKana.map((k) => k.romaji).toSet().toList();

    while (options.length < 4) {
      final randomRomaji = allRomaji[_random.nextInt(allRomaji.length)];
      options.add(randomRomaji);
    }

    return options.toList()..shuffle();
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context)!;

    if (_currentIndex >= _questions.length) {
      final percentage = (_score / _questions.length * 100).round();
      return Center(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(
                percentage >= 80
                    ? Icons.emoji_events
                    : Icons.sentiment_satisfied,
                size: 64,
                color: percentage >= 80 ? Colors.amber : Colors.blue,
              ),
              const SizedBox(height: 16),
              Text(
                l10n.quizComplete,
                style: const TextStyle(
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 8),
              Text(
                '$_score / ${_questions.length} ($percentage%)',
                style: const TextStyle(
                  fontSize: 32,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 8),
              Text(
                percentage >= 80 ? l10n.excellent : l10n.keepPracticing,
                style: const TextStyle(fontSize: 16, color: Colors.grey),
              ),
              const SizedBox(height: 24),
              ElevatedButton.icon(
                onPressed: () {
                  setState(() {
                    _startQuiz();
                  });
                },
                icon: const Icon(Icons.refresh),
                label: Text(l10n.tryAgain),
              ),
            ],
          ),
        ),
      );
    }

    final kana = _questions[_currentIndex];
    final displayChar = widget.isKatakana ? kana.katakana : kana.hiragana;
    final options = _generateOptions(kana);

    return Padding(
      padding: const EdgeInsets.all(24),
      child: Column(
        children: [
          // Progress
          LinearProgressIndicator(
            value: (_currentIndex + 1) / _questions.length,
          ),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 8),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  '${l10n.question} ${_currentIndex + 1}/${_questions.length}',
                  style: const TextStyle(color: Colors.grey),
                ),
                Text(
                  '${l10n.score}: $_score',
                  style: TextStyle(
                    color: Theme.of(context).primaryColor,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ],
            ),
          ),

          const Spacer(),

          // Question
          Container(
            padding: const EdgeInsets.all(32),
            decoration: BoxDecoration(
              color: Theme.of(context).cardColor,
              borderRadius: BorderRadius.circular(20),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withAlpha(20),
                  blurRadius: 10,
                  offset: const Offset(0, 5),
                ),
              ],
            ),
            child: Text(
              displayChar,
              style: const TextStyle(fontSize: 80, fontWeight: FontWeight.bold),
            ),
          ),

          const SizedBox(height: 32),

          // Options
          ...options.map((option) {
            final isCorrect = option == kana.romaji;
            final isSelected = option == _selectedAnswer;

            Color? backgroundColor;
            if (_answered) {
              if (isCorrect) {
                backgroundColor = Colors.green.withAlpha(50);
              } else if (isSelected) {
                backgroundColor = Colors.red.withAlpha(50);
              }
            }

            return Padding(
              padding: const EdgeInsets.symmetric(vertical: 4),
              child: SizedBox(
                width: double.infinity,
                child: ElevatedButton(
                  onPressed:
                      _answered
                          ? null
                          : () {
                            setState(() {
                              _selectedAnswer = option;
                              _answered = true;
                              if (isCorrect) {
                                _score++;
                              }
                            });
                          },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: backgroundColor,
                    padding: const EdgeInsets.symmetric(vertical: 16),
                  ),
                  child: Text(option, style: const TextStyle(fontSize: 20)),
                ),
              ),
            );
          }),

          const Spacer(),

          // Next button
          if (_answered)
            ElevatedButton.icon(
              onPressed: () {
                setState(() {
                  _currentIndex++;
                  _selectedAnswer = null;
                  _answered = false;
                });
              },
              icon: const Icon(Icons.arrow_forward),
              label: Text(l10n.next),
            ),
        ],
      ),
    );
  }
}
