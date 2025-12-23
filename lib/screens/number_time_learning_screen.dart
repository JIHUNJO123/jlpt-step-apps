import 'package:flutter/material.dart';
import 'dart:math';
import '../data/number_time_data.dart';
import 'package:jlpt_vocab_app/l10n/generated/app_localizations.dart';

class NumberTimeLearningScreen extends StatefulWidget {
  const NumberTimeLearningScreen({super.key});

  @override
  State<NumberTimeLearningScreen> createState() =>
      _NumberTimeLearningScreenState();
}

class _NumberTimeLearningScreenState extends State<NumberTimeLearningScreen>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context)!;

    return Scaffold(
      appBar: AppBar(
        title: Text(l10n.numbersAndTime),
        bottom: TabBar(
          controller: _tabController,
          isScrollable: true,
          tabs: [
            Tab(text: l10n.numbers),
            Tab(text: l10n.time),
            Tab(text: l10n.daysMonths),
            Tab(text: l10n.quiz),
          ],
        ),
      ),
      body: TabBarView(
        controller: _tabController,
        children: [
          _buildNumbersTab(),
          _buildTimeTab(),
          _buildDaysMonthsTab(),
          _buildQuizTab(),
        ],
      ),
    );
  }

  Widget _buildNumbersTab() {
    final l10n = AppLocalizations.of(context)!;

    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        _buildSectionHeader(l10n.basicNumbers),
        const SizedBox(height: 8),
        _buildNumberGrid(NumberTimeData.basicNumbers),
        const SizedBox(height: 24),
        _buildSectionHeader(l10n.bigNumbers),
        const SizedBox(height: 8),
        _buildNumberGrid(NumberTimeData.bigNumbers),
        const SizedBox(height: 24),
        _buildSectionHeader(l10n.compoundNumbers),
        const SizedBox(height: 8),
        _buildNumberGrid(NumberTimeData.compoundNumbers),
      ],
    );
  }

  Widget _buildTimeTab() {
    final l10n = AppLocalizations.of(context)!;

    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        _buildSectionHeader(l10n.hours),
        const SizedBox(height: 8),
        _buildTimeItemList(NumberTimeData.hours),
        const SizedBox(height: 24),
        _buildSectionHeader(l10n.minutes),
        const SizedBox(height: 8),
        _buildTimeItemList(NumberTimeData.minutes),
        const SizedBox(height: 24),
        _buildSectionHeader(l10n.timeExpressions),
        const SizedBox(height: 8),
        _buildTimeItemList(NumberTimeData.timeExpressions),
      ],
    );
  }

  Widget _buildDaysMonthsTab() {
    final l10n = AppLocalizations.of(context)!;

    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        _buildSectionHeader(l10n.daysOfWeek),
        const SizedBox(height: 8),
        _buildTimeItemList(NumberTimeData.daysOfWeek),
        const SizedBox(height: 24),
        _buildSectionHeader(l10n.months),
        const SizedBox(height: 8),
        _buildTimeItemList(NumberTimeData.months),
        const SizedBox(height: 24),
        _buildSectionHeader(l10n.dates),
        const SizedBox(height: 8),
        _buildTimeItemList(NumberTimeData.dates),
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

  Widget _buildNumberGrid(List<NumberItem> numbers) {
    return Wrap(
      spacing: 8,
      runSpacing: 8,
      children: numbers.map((item) => _buildNumberCard(item)).toList(),
    );
  }

  Widget _buildNumberCard(NumberItem item) {
    return GestureDetector(
      onTap: () => _showNumberDetail(item),
      child: Container(
        width: 80,
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: Theme.of(context).cardColor,
          borderRadius: BorderRadius.circular(12),
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
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(
              item.number.toString(),
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
                color: Theme.of(context).primaryColor,
              ),
            ),
            const SizedBox(height: 4),
            Text(
              item.japanese,
              style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 2),
            Text(
              item.reading,
              style: TextStyle(fontSize: 11, color: Colors.grey[600]),
              textAlign: TextAlign.center,
            ),
          ],
        ),
      ),
    );
  }

  void _showNumberDetail(NumberItem item) {
    showDialog(
      context: context,
      builder:
          (context) => AlertDialog(
            content: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  item.number.toString(),
                  style: TextStyle(
                    fontSize: 32,
                    fontWeight: FontWeight.bold,
                    color: Theme.of(context).primaryColor,
                  ),
                ),
                const SizedBox(height: 16),
                Text(
                  item.japanese,
                  style: const TextStyle(
                    fontSize: 48,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 8),
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 16,
                    vertical: 8,
                  ),
                  decoration: BoxDecoration(
                    color: Colors.grey.withAlpha(30),
                    borderRadius: BorderRadius.circular(20),
                  ),
                  child: Text(
                    item.reading,
                    style: const TextStyle(fontSize: 20),
                  ),
                ),
                if (item.altReading != null) ...[
                  const SizedBox(height: 8),
                  Text(
                    '(${item.altReading})',
                    style: TextStyle(fontSize: 16, color: Colors.grey[600]),
                  ),
                ],
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

  Widget _buildTimeItemList(List<TimeItem> items) {
    return Column(
      children: items.map((item) => _buildTimeItemCard(item)).toList(),
    );
  }

  Widget _buildTimeItemCard(TimeItem item) {
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 4),
      child: ListTile(
        title: Text(
          item.japanese,
          style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
        ),
        subtitle: Text(item.reading),
        trailing: Container(
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
          decoration: BoxDecoration(
            color: Theme.of(context).primaryColor.withAlpha(30),
            borderRadius: BorderRadius.circular(16),
          ),
          child: Text(
            item.meaning,
            style: TextStyle(
              color: Theme.of(context).primaryColor,
              fontWeight: FontWeight.w500,
            ),
          ),
        ),
        onTap: () => _showTimeDetail(item),
      ),
    );
  }

  void _showTimeDetail(TimeItem item) {
    showDialog(
      context: context,
      builder:
          (context) => AlertDialog(
            content: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  item.japanese,
                  style: const TextStyle(
                    fontSize: 40,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 8),
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 16,
                    vertical: 8,
                  ),
                  decoration: BoxDecoration(
                    color: Colors.grey.withAlpha(30),
                    borderRadius: BorderRadius.circular(20),
                  ),
                  child: Text(
                    item.reading,
                    style: const TextStyle(fontSize: 20),
                  ),
                ),
                const SizedBox(height: 16),
                Text(
                  item.meaning,
                  style: TextStyle(
                    fontSize: 18,
                    color: Theme.of(context).primaryColor,
                    fontWeight: FontWeight.w500,
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

  Widget _buildQuizTab() {
    return _NumberTimeQuiz();
  }
}

class _NumberTimeQuiz extends StatefulWidget {
  @override
  State<_NumberTimeQuiz> createState() => _NumberTimeQuizState();
}

class _NumberTimeQuizState extends State<_NumberTimeQuiz> {
  final Random _random = Random();
  late List<_QuizQuestion> _questions;
  int _currentIndex = 0;
  int _score = 0;
  String? _selectedAnswer;
  bool _answered = false;
  List<String> _currentOptions = [];

  @override
  void initState() {
    super.initState();
    _startQuiz();
  }

  void _startQuiz() {
    _questions = _generateQuestions();
    _questions.shuffle();
    _questions = _questions.take(15).toList();
    _currentIndex = 0;
    _score = 0;
    _selectedAnswer = null;
    _answered = false;
    _generateCurrentOptions();
  }

  void _generateCurrentOptions() {
    final question = _questions[_currentIndex];
    final options = <String>{question.correctAnswer};

    List<String> pool;
    switch (question.type) {
      case 'number':
        pool =
            NumberTimeData.basicNumbers
                .map((n) => n.reading.split('/').first)
                .toList();
        break;
      case 'time':
        pool = NumberTimeData.hours.map((t) => t.reading).toList();
        break;
      case 'day':
        pool = NumberTimeData.daysOfWeek.map((d) => d.reading).toList();
        break;
      case 'month':
        pool = NumberTimeData.months.map((m) => m.reading).toList();
        break;
      default:
        pool = NumberTimeData.basicNumbers.map((n) => n.reading).toList();
    }

    while (options.length < 4 && pool.length >= 4) {
      final randomItem = pool[_random.nextInt(pool.length)];
      options.add(randomItem);
    }

    _currentOptions = options.toList()..shuffle();
  }

  void _nextQuestion() {
    setState(() {
      _currentIndex++;
      _selectedAnswer = null;
      _answered = false;
      if (_currentIndex < _questions.length) {
        _generateCurrentOptions();
      }
    });
  }

  List<_QuizQuestion> _generateQuestions() {
    final questions = <_QuizQuestion>[];

    // 숫자 문제
    for (final num in NumberTimeData.basicNumbers) {
      questions.add(
        _QuizQuestion(
          question: num.japanese,
          correctAnswer: num.reading.split('/').first,
          type: 'number',
        ),
      );
    }

    // 시간 문제
    for (final time in NumberTimeData.hours) {
      questions.add(
        _QuizQuestion(
          question: time.japanese,
          correctAnswer: time.reading,
          type: 'time',
        ),
      );
    }

    // 요일 문제
    for (final day in NumberTimeData.daysOfWeek) {
      questions.add(
        _QuizQuestion(
          question: day.japanese,
          correctAnswer: day.reading,
          type: 'day',
        ),
      );
    }

    // 월 문제
    for (final month in NumberTimeData.months) {
      questions.add(
        _QuizQuestion(
          question: month.japanese,
          correctAnswer: month.reading,
          type: 'month',
        ),
      );
    }

    return questions;
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

    final question = _questions[_currentIndex];

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
            child: Column(
              children: [
                Text(
                  l10n.whatIsTheReading,
                  style: const TextStyle(fontSize: 16, color: Colors.grey),
                ),
                const SizedBox(height: 16),
                Text(
                  question.question,
                  style: const TextStyle(
                    fontSize: 48,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ],
            ),
          ),

          const SizedBox(height: 32),

          // Options
          ..._currentOptions.map((option) {
            final isCorrect = option == question.correctAnswer;
            final isSelected = option == _selectedAnswer;

            Color? backgroundColor;
            Color? borderColor;
            Widget? trailingIcon;

            if (_answered) {
              if (isCorrect) {
                backgroundColor = Colors.green.withAlpha(50);
                borderColor = Colors.green;
                trailingIcon = const Icon(
                  Icons.check_circle,
                  color: Colors.green,
                );
              } else if (isSelected) {
                backgroundColor = Colors.red.withAlpha(50);
                borderColor = Colors.red;
                trailingIcon = const Icon(Icons.cancel, color: Colors.red);
              }
            }

            return Padding(
              padding: const EdgeInsets.symmetric(vertical: 4),
              child: SizedBox(
                width: double.infinity,
                child: OutlinedButton(
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
                  style: OutlinedButton.styleFrom(
                    backgroundColor: backgroundColor,
                    side:
                        borderColor != null
                            ? BorderSide(color: borderColor, width: 2)
                            : null,
                    padding: const EdgeInsets.symmetric(vertical: 16),
                    disabledBackgroundColor: backgroundColor,
                  ),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text(
                        option,
                        style: TextStyle(
                          fontSize: 18,
                          color:
                              _answered && isCorrect
                                  ? Colors.green
                                  : _answered && isSelected
                                  ? Colors.red
                                  : null,
                          fontWeight:
                              _answered && (isCorrect || isSelected)
                                  ? FontWeight.bold
                                  : null,
                        ),
                      ),
                      if (trailingIcon != null) ...[
                        const SizedBox(width: 8),
                        trailingIcon,
                      ],
                    ],
                  ),
                ),
              ),
            );
          }),

          const Spacer(),

          // Next button
          if (_answered)
            ElevatedButton.icon(
              onPressed: _nextQuestion,
              icon: const Icon(Icons.arrow_forward),
              label: Text(l10n.next),
            ),
        ],
      ),
    );
  }
}

class _QuizQuestion {
  final String question;
  final String correctAnswer;
  final String type;

  _QuizQuestion({
    required this.question,
    required this.correctAnswer,
    required this.type,
  });
}
