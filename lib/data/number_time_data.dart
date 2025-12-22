// 숫자, 시간, 날짜 데이터

class NumberItem {
  final int number;
  final String japanese;
  final String reading;
  final String? altReading;

  const NumberItem({
    required this.number,
    required this.japanese,
    required this.reading,
    this.altReading,
  });
}

class TimeItem {
  final String japanese;
  final String reading;
  final String meaning;
  final Map<String, String> translations;

  const TimeItem({
    required this.japanese,
    required this.reading,
    required this.meaning,
    this.translations = const {},
  });
}

class NumberTimeData {
  // 기본 숫자 (1-10)
  static const List<NumberItem> basicNumbers = [
    NumberItem(number: 0, japanese: '零/ゼロ', reading: 'れい/ゼロ'),
    NumberItem(number: 1, japanese: '一', reading: 'いち'),
    NumberItem(number: 2, japanese: '二', reading: 'に'),
    NumberItem(number: 3, japanese: '三', reading: 'さん'),
    NumberItem(number: 4, japanese: '四', reading: 'よん', altReading: 'し'),
    NumberItem(number: 5, japanese: '五', reading: 'ご'),
    NumberItem(number: 6, japanese: '六', reading: 'ろく'),
    NumberItem(number: 7, japanese: '七', reading: 'なな', altReading: 'しち'),
    NumberItem(number: 8, japanese: '八', reading: 'はち'),
    NumberItem(number: 9, japanese: '九', reading: 'きゅう', altReading: 'く'),
    NumberItem(number: 10, japanese: '十', reading: 'じゅう'),
  ];

  // 큰 숫자
  static const List<NumberItem> bigNumbers = [
    NumberItem(number: 100, japanese: '百', reading: 'ひゃく'),
    NumberItem(number: 1000, japanese: '千', reading: 'せん'),
    NumberItem(number: 10000, japanese: '万', reading: 'まん'),
    NumberItem(number: 100000000, japanese: '億', reading: 'おく'),
  ];

  // 11-99 예시
  static const List<NumberItem> compoundNumbers = [
    NumberItem(number: 11, japanese: '十一', reading: 'じゅういち'),
    NumberItem(number: 12, japanese: '十二', reading: 'じゅうに'),
    NumberItem(number: 20, japanese: '二十', reading: 'にじゅう'),
    NumberItem(number: 21, japanese: '二十一', reading: 'にじゅういち'),
    NumberItem(number: 30, japanese: '三十', reading: 'さんじゅう'),
    NumberItem(number: 50, japanese: '五十', reading: 'ごじゅう'),
    NumberItem(number: 99, japanese: '九十九', reading: 'きゅうじゅうきゅう'),
  ];

  // 시간 (時)
  static const List<TimeItem> hours = [
    TimeItem(japanese: '一時', reading: 'いちじ', meaning: '1 o\'clock'),
    TimeItem(japanese: '二時', reading: 'にじ', meaning: '2 o\'clock'),
    TimeItem(japanese: '三時', reading: 'さんじ', meaning: '3 o\'clock'),
    TimeItem(japanese: '四時', reading: 'よじ', meaning: '4 o\'clock'),
    TimeItem(japanese: '五時', reading: 'ごじ', meaning: '5 o\'clock'),
    TimeItem(japanese: '六時', reading: 'ろくじ', meaning: '6 o\'clock'),
    TimeItem(japanese: '七時', reading: 'しちじ', meaning: '7 o\'clock'),
    TimeItem(japanese: '八時', reading: 'はちじ', meaning: '8 o\'clock'),
    TimeItem(japanese: '九時', reading: 'くじ', meaning: '9 o\'clock'),
    TimeItem(japanese: '十時', reading: 'じゅうじ', meaning: '10 o\'clock'),
    TimeItem(japanese: '十一時', reading: 'じゅういちじ', meaning: '11 o\'clock'),
    TimeItem(japanese: '十二時', reading: 'じゅうにじ', meaning: '12 o\'clock'),
  ];

  // 분 (分)
  static const List<TimeItem> minutes = [
    TimeItem(japanese: '一分', reading: 'いっぷん', meaning: '1 minute'),
    TimeItem(japanese: '二分', reading: 'にふん', meaning: '2 minutes'),
    TimeItem(japanese: '三分', reading: 'さんぷん', meaning: '3 minutes'),
    TimeItem(japanese: '四分', reading: 'よんぷん', meaning: '4 minutes'),
    TimeItem(japanese: '五分', reading: 'ごふん', meaning: '5 minutes'),
    TimeItem(japanese: '六分', reading: 'ろっぷん', meaning: '6 minutes'),
    TimeItem(japanese: '七分', reading: 'ななふん', meaning: '7 minutes'),
    TimeItem(japanese: '八分', reading: 'はっぷん', meaning: '8 minutes'),
    TimeItem(japanese: '九分', reading: 'きゅうふん', meaning: '9 minutes'),
    TimeItem(japanese: '十分', reading: 'じゅっぷん', meaning: '10 minutes'),
    TimeItem(japanese: '十五分', reading: 'じゅうごふん', meaning: '15 minutes'),
    TimeItem(japanese: '三十分', reading: 'さんじゅっぷん', meaning: '30 minutes'),
    TimeItem(japanese: '半', reading: 'はん', meaning: 'half past'),
  ];

  // 요일
  static const List<TimeItem> daysOfWeek = [
    TimeItem(japanese: '月曜日', reading: 'げつようび', meaning: 'Monday'),
    TimeItem(japanese: '火曜日', reading: 'かようび', meaning: 'Tuesday'),
    TimeItem(japanese: '水曜日', reading: 'すいようび', meaning: 'Wednesday'),
    TimeItem(japanese: '木曜日', reading: 'もくようび', meaning: 'Thursday'),
    TimeItem(japanese: '金曜日', reading: 'きんようび', meaning: 'Friday'),
    TimeItem(japanese: '土曜日', reading: 'どようび', meaning: 'Saturday'),
    TimeItem(japanese: '日曜日', reading: 'にちようび', meaning: 'Sunday'),
  ];

  // 월 (月)
  static const List<TimeItem> months = [
    TimeItem(japanese: '一月', reading: 'いちがつ', meaning: 'January'),
    TimeItem(japanese: '二月', reading: 'にがつ', meaning: 'February'),
    TimeItem(japanese: '三月', reading: 'さんがつ', meaning: 'March'),
    TimeItem(japanese: '四月', reading: 'しがつ', meaning: 'April'),
    TimeItem(japanese: '五月', reading: 'ごがつ', meaning: 'May'),
    TimeItem(japanese: '六月', reading: 'ろくがつ', meaning: 'June'),
    TimeItem(japanese: '七月', reading: 'しちがつ', meaning: 'July'),
    TimeItem(japanese: '八月', reading: 'はちがつ', meaning: 'August'),
    TimeItem(japanese: '九月', reading: 'くがつ', meaning: 'September'),
    TimeItem(japanese: '十月', reading: 'じゅうがつ', meaning: 'October'),
    TimeItem(japanese: '十一月', reading: 'じゅういちがつ', meaning: 'November'),
    TimeItem(japanese: '十二月', reading: 'じゅうにがつ', meaning: 'December'),
  ];

  // 날짜 (日)
  static const List<TimeItem> dates = [
    TimeItem(japanese: '一日', reading: 'ついたち', meaning: '1st'),
    TimeItem(japanese: '二日', reading: 'ふつか', meaning: '2nd'),
    TimeItem(japanese: '三日', reading: 'みっか', meaning: '3rd'),
    TimeItem(japanese: '四日', reading: 'よっか', meaning: '4th'),
    TimeItem(japanese: '五日', reading: 'いつか', meaning: '5th'),
    TimeItem(japanese: '六日', reading: 'むいか', meaning: '6th'),
    TimeItem(japanese: '七日', reading: 'なのか', meaning: '7th'),
    TimeItem(japanese: '八日', reading: 'ようか', meaning: '8th'),
    TimeItem(japanese: '九日', reading: 'ここのか', meaning: '9th'),
    TimeItem(japanese: '十日', reading: 'とおか', meaning: '10th'),
    TimeItem(japanese: '十四日', reading: 'じゅうよっか', meaning: '14th'),
    TimeItem(japanese: '二十日', reading: 'はつか', meaning: '20th'),
    TimeItem(japanese: '二十四日', reading: 'にじゅうよっか', meaning: '24th'),
  ];

  // 시간 관련 표현
  static const List<TimeItem> timeExpressions = [
    TimeItem(japanese: '午前', reading: 'ごぜん', meaning: 'AM / morning'),
    TimeItem(japanese: '午後', reading: 'ごご', meaning: 'PM / afternoon'),
    TimeItem(japanese: '朝', reading: 'あさ', meaning: 'morning'),
    TimeItem(japanese: '昼', reading: 'ひる', meaning: 'noon / daytime'),
    TimeItem(japanese: '夕方', reading: 'ゆうがた', meaning: 'evening'),
    TimeItem(japanese: '夜', reading: 'よる', meaning: 'night'),
    TimeItem(japanese: '今日', reading: 'きょう', meaning: 'today'),
    TimeItem(japanese: '明日', reading: 'あした', meaning: 'tomorrow'),
    TimeItem(japanese: '昨日', reading: 'きのう', meaning: 'yesterday'),
    TimeItem(japanese: '今週', reading: 'こんしゅう', meaning: 'this week'),
    TimeItem(japanese: '来週', reading: 'らいしゅう', meaning: 'next week'),
    TimeItem(japanese: '先週', reading: 'せんしゅう', meaning: 'last week'),
    TimeItem(japanese: '今月', reading: 'こんげつ', meaning: 'this month'),
    TimeItem(japanese: '来月', reading: 'らいげつ', meaning: 'next month'),
    TimeItem(japanese: '先月', reading: 'せんげつ', meaning: 'last month'),
    TimeItem(japanese: '今年', reading: 'ことし', meaning: 'this year'),
    TimeItem(japanese: '来年', reading: 'らいねん', meaning: 'next year'),
    TimeItem(japanese: '去年', reading: 'きょねん', meaning: 'last year'),
  ];
}
