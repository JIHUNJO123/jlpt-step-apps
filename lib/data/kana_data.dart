// 히라가나/카타카나 데이터

class KanaCharacter {
  final String hiragana;
  final String katakana;
  final String romaji;
  final String? audioHint;

  const KanaCharacter({
    required this.hiragana,
    required this.katakana,
    required this.romaji,
    this.audioHint,
  });
}

class KanaData {
  // 기본 모음 (5)
  static const List<KanaCharacter> vowels = [
    KanaCharacter(hiragana: 'あ', katakana: 'ア', romaji: 'a'),
    KanaCharacter(hiragana: 'い', katakana: 'イ', romaji: 'i'),
    KanaCharacter(hiragana: 'う', katakana: 'ウ', romaji: 'u'),
    KanaCharacter(hiragana: 'え', katakana: 'エ', romaji: 'e'),
    KanaCharacter(hiragana: 'お', katakana: 'オ', romaji: 'o'),
  ];

  // K행 (5)
  static const List<KanaCharacter> kRow = [
    KanaCharacter(hiragana: 'か', katakana: 'カ', romaji: 'ka'),
    KanaCharacter(hiragana: 'き', katakana: 'キ', romaji: 'ki'),
    KanaCharacter(hiragana: 'く', katakana: 'ク', romaji: 'ku'),
    KanaCharacter(hiragana: 'け', katakana: 'ケ', romaji: 'ke'),
    KanaCharacter(hiragana: 'こ', katakana: 'コ', romaji: 'ko'),
  ];

  // S행 (5)
  static const List<KanaCharacter> sRow = [
    KanaCharacter(hiragana: 'さ', katakana: 'サ', romaji: 'sa'),
    KanaCharacter(hiragana: 'し', katakana: 'シ', romaji: 'shi'),
    KanaCharacter(hiragana: 'す', katakana: 'ス', romaji: 'su'),
    KanaCharacter(hiragana: 'せ', katakana: 'セ', romaji: 'se'),
    KanaCharacter(hiragana: 'そ', katakana: 'ソ', romaji: 'so'),
  ];

  // T행 (5)
  static const List<KanaCharacter> tRow = [
    KanaCharacter(hiragana: 'た', katakana: 'タ', romaji: 'ta'),
    KanaCharacter(hiragana: 'ち', katakana: 'チ', romaji: 'chi'),
    KanaCharacter(hiragana: 'つ', katakana: 'ツ', romaji: 'tsu'),
    KanaCharacter(hiragana: 'て', katakana: 'テ', romaji: 'te'),
    KanaCharacter(hiragana: 'と', katakana: 'ト', romaji: 'to'),
  ];

  // N행 (5)
  static const List<KanaCharacter> nRow = [
    KanaCharacter(hiragana: 'な', katakana: 'ナ', romaji: 'na'),
    KanaCharacter(hiragana: 'に', katakana: 'ニ', romaji: 'ni'),
    KanaCharacter(hiragana: 'ぬ', katakana: 'ヌ', romaji: 'nu'),
    KanaCharacter(hiragana: 'ね', katakana: 'ネ', romaji: 'ne'),
    KanaCharacter(hiragana: 'の', katakana: 'ノ', romaji: 'no'),
  ];

  // H행 (5)
  static const List<KanaCharacter> hRow = [
    KanaCharacter(hiragana: 'は', katakana: 'ハ', romaji: 'ha'),
    KanaCharacter(hiragana: 'ひ', katakana: 'ヒ', romaji: 'hi'),
    KanaCharacter(hiragana: 'ふ', katakana: 'フ', romaji: 'fu'),
    KanaCharacter(hiragana: 'へ', katakana: 'ヘ', romaji: 'he'),
    KanaCharacter(hiragana: 'ほ', katakana: 'ホ', romaji: 'ho'),
  ];

  // M행 (5)
  static const List<KanaCharacter> mRow = [
    KanaCharacter(hiragana: 'ま', katakana: 'マ', romaji: 'ma'),
    KanaCharacter(hiragana: 'み', katakana: 'ミ', romaji: 'mi'),
    KanaCharacter(hiragana: 'む', katakana: 'ム', romaji: 'mu'),
    KanaCharacter(hiragana: 'め', katakana: 'メ', romaji: 'me'),
    KanaCharacter(hiragana: 'も', katakana: 'モ', romaji: 'mo'),
  ];

  // Y행 (3)
  static const List<KanaCharacter> yRow = [
    KanaCharacter(hiragana: 'や', katakana: 'ヤ', romaji: 'ya'),
    KanaCharacter(hiragana: 'ゆ', katakana: 'ユ', romaji: 'yu'),
    KanaCharacter(hiragana: 'よ', katakana: 'ヨ', romaji: 'yo'),
  ];

  // R행 (5)
  static const List<KanaCharacter> rRow = [
    KanaCharacter(hiragana: 'ら', katakana: 'ラ', romaji: 'ra'),
    KanaCharacter(hiragana: 'り', katakana: 'リ', romaji: 'ri'),
    KanaCharacter(hiragana: 'る', katakana: 'ル', romaji: 'ru'),
    KanaCharacter(hiragana: 'れ', katakana: 'レ', romaji: 're'),
    KanaCharacter(hiragana: 'ろ', katakana: 'ロ', romaji: 'ro'),
  ];

  // W행 (2) + N (1)
  static const List<KanaCharacter> wRow = [
    KanaCharacter(hiragana: 'わ', katakana: 'ワ', romaji: 'wa'),
    KanaCharacter(hiragana: 'を', katakana: 'ヲ', romaji: 'wo'),
    KanaCharacter(hiragana: 'ん', katakana: 'ン', romaji: 'n'),
  ];

  // 탁음 G행
  static const List<KanaCharacter> gRow = [
    KanaCharacter(hiragana: 'が', katakana: 'ガ', romaji: 'ga'),
    KanaCharacter(hiragana: 'ぎ', katakana: 'ギ', romaji: 'gi'),
    KanaCharacter(hiragana: 'ぐ', katakana: 'グ', romaji: 'gu'),
    KanaCharacter(hiragana: 'げ', katakana: 'ゲ', romaji: 'ge'),
    KanaCharacter(hiragana: 'ご', katakana: 'ゴ', romaji: 'go'),
  ];

  // 탁음 Z행
  static const List<KanaCharacter> zRow = [
    KanaCharacter(hiragana: 'ざ', katakana: 'ザ', romaji: 'za'),
    KanaCharacter(hiragana: 'じ', katakana: 'ジ', romaji: 'ji'),
    KanaCharacter(hiragana: 'ず', katakana: 'ズ', romaji: 'zu'),
    KanaCharacter(hiragana: 'ぜ', katakana: 'ゼ', romaji: 'ze'),
    KanaCharacter(hiragana: 'ぞ', katakana: 'ゾ', romaji: 'zo'),
  ];

  // 탁음 D행
  static const List<KanaCharacter> dRow = [
    KanaCharacter(hiragana: 'だ', katakana: 'ダ', romaji: 'da'),
    KanaCharacter(hiragana: 'ぢ', katakana: 'ヂ', romaji: 'ji'),
    KanaCharacter(hiragana: 'づ', katakana: 'ヅ', romaji: 'zu'),
    KanaCharacter(hiragana: 'で', katakana: 'デ', romaji: 'de'),
    KanaCharacter(hiragana: 'ど', katakana: 'ド', romaji: 'do'),
  ];

  // 탁음 B행
  static const List<KanaCharacter> bRow = [
    KanaCharacter(hiragana: 'ば', katakana: 'バ', romaji: 'ba'),
    KanaCharacter(hiragana: 'び', katakana: 'ビ', romaji: 'bi'),
    KanaCharacter(hiragana: 'ぶ', katakana: 'ブ', romaji: 'bu'),
    KanaCharacter(hiragana: 'べ', katakana: 'ベ', romaji: 'be'),
    KanaCharacter(hiragana: 'ぼ', katakana: 'ボ', romaji: 'bo'),
  ];

  // 반탁음 P행
  static const List<KanaCharacter> pRow = [
    KanaCharacter(hiragana: 'ぱ', katakana: 'パ', romaji: 'pa'),
    KanaCharacter(hiragana: 'ぴ', katakana: 'ピ', romaji: 'pi'),
    KanaCharacter(hiragana: 'ぷ', katakana: 'プ', romaji: 'pu'),
    KanaCharacter(hiragana: 'ぺ', katakana: 'ペ', romaji: 'pe'),
    KanaCharacter(hiragana: 'ぽ', katakana: 'ポ', romaji: 'po'),
  ];

  // 기본 가나 (청음)
  static List<KanaCharacter> get basicKana => [
    ...vowels,
    ...kRow,
    ...sRow,
    ...tRow,
    ...nRow,
    ...hRow,
    ...mRow,
    ...yRow,
    ...rRow,
    ...wRow,
  ];

  // 탁음/반탁음
  static List<KanaCharacter> get dakutenKana => [
    ...gRow,
    ...zRow,
    ...dRow,
    ...bRow,
    ...pRow,
  ];

  // 전체 가나
  static List<KanaCharacter> get allKana => [...basicKana, ...dakutenKana];

  // 행 이름들
  static const List<String> rowNames = [
    'あ행 (모음)',
    'か행',
    'さ행',
    'た행',
    'な행',
    'は행',
    'ま행',
    'や행',
    'ら행',
    'わ행',
  ];

  static const List<String> dakutenRowNames = [
    'が행 (탁음)',
    'ざ행 (탁음)',
    'だ행 (탁음)',
    'ば행 (탁음)',
    'ぱ행 (반탁음)',
  ];

  // 행별로 가나 가져오기
  static List<List<KanaCharacter>> get basicRows => [
    vowels,
    kRow,
    sRow,
    tRow,
    nRow,
    hRow,
    mRow,
    yRow,
    rRow,
    wRow,
  ];

  static List<List<KanaCharacter>> get dakutenRows => [
    gRow,
    zRow,
    dRow,
    bRow,
    pRow,
  ];
}
