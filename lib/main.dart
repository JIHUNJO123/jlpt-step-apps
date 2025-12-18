import 'dart:io';
import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:sat_vocab_app/l10n/generated/app_localizations.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:sqflite_common_ffi/sqflite_ffi.dart';
import 'package:sqflite_common_ffi_web/sqflite_ffi_web.dart';
import 'screens/home_screen.dart';
import 'services/translation_service.dart';
import 'services/ad_service.dart';
import 'services/purchase_service.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // ?�랫?�별 sqflite 초기??
  if (kIsWeb) {
    // ?�에??sqflite 초기??
    databaseFactory = databaseFactoryFfiWeb;
  } else if (Platform.isWindows || Platform.isLinux || Platform.isMacOS) {
    // Windows, Linux, macOS?�서 sqflite 초기??
    sqfliteFfiInit();
    databaseFactory = databaseFactoryFfi;
  }

  // 번역 ?�비??초기??
  await TranslationService.instance.init();

  // 광고 ?�비??초기??
  await AdService.instance.initialize();

  // ?�앱 구매 ?�비??초기??
  await PurchaseService.instance.initialize();

  runApp(
    ChangeNotifierProvider(
      create: (_) => LocaleProvider(),
      child: const GREVocabApp(),
    ),
  );
}

/// ?�어 �??�마 변경을 ?�한 Provider
class LocaleProvider extends ChangeNotifier {
  Locale _locale = const Locale('en');
  ThemeMode _themeMode = ThemeMode.light;

  Locale get locale => _locale;
  ThemeMode get themeMode => _themeMode;

  LocaleProvider() {
    _loadSavedSettings();
  }

  Future<void> _loadSavedSettings() async {
    final prefs = await SharedPreferences.getInstance();

    // ?�어 로드
    await TranslationService.instance.init();
    final langCode = TranslationService.instance.currentLanguage;
    _locale = _createLocale(langCode);

    // ?�크모드 로드
    final isDarkMode = prefs.getBool('darkMode') ?? false;
    _themeMode = isDarkMode ? ThemeMode.dark : ThemeMode.light;

    notifyListeners();
  }

  Locale _createLocale(String langCode) {
    return Locale(langCode);
  }

  void setLocale(Locale locale) {
    _locale = locale;
    TranslationService.instance.setLanguage(locale.languageCode);
    notifyListeners();
  }

  void setLocaleDirectly(Locale locale) {
    _locale = locale;
    notifyListeners();
  }

  void toggleDarkMode(bool isDark) {
    _themeMode = isDark ? ThemeMode.dark : ThemeMode.light;
    notifyListeners();
  }
}

class GREVocabApp extends StatelessWidget {
  const GREVocabApp({super.key});

  @override
  Widget build(BuildContext context) {
    final localeProvider = Provider.of<LocaleProvider>(context);

    return MaterialApp(
      title: 'GRE Vocabulary Master',
      debugShowCheckedModeBanner: false,

      // Localization ?�정
      locale: localeProvider.locale,
      localizationsDelegates: const [
        AppLocalizations.delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      supportedLocales: const [
        Locale('en'),
        Locale('hi'),
        Locale('zh'),
        Locale('ko'),
      ],

      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF6B4EAB), // GRE 블루
          brightness: Brightness.light,
        ),
        useMaterial3: false,
        appBarTheme: const AppBarTheme(centerTitle: true, elevation: 0),
        cardTheme: CardThemeData(
          elevation: 2,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
        ),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(12),
            ),
          ),
        ),
        inputDecorationTheme: InputDecorationTheme(
          border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
          filled: true,
        ),
      ),
      darkTheme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF6B4EAB),
          brightness: Brightness.dark,
        ),
        useMaterial3: true,
        appBarTheme: const AppBarTheme(centerTitle: true, elevation: 0),
        cardTheme: CardThemeData(
          elevation: 2,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
        ),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(12),
            ),
          ),
        ),
        inputDecorationTheme: InputDecorationTheme(
          border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
          filled: true,
        ),
      ),
      themeMode: localeProvider.themeMode,
      home: const HomeScreen(),
    );
  }
}
