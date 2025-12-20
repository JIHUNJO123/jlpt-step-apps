import os
import re

base_path = r"C:\Users\hooni\Desktop\sat_vocab_app_new"

# 1. pubspec.yaml 수정
pubspec_path = os.path.join(base_path, "pubspec.yaml")
with open(pubspec_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('name: gre_vocab_app', 'name: sat_vocab_app')
content = content.replace('description: "GRE Vocabulary', 'description: "SAT Vocabulary')

with open(pubspec_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ pubspec.yaml 수정 완료")

# 2. Android build.gradle.kts 수정
gradle_path = os.path.join(base_path, "android", "app", "build.gradle.kts")
with open(gradle_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('com.jhuni.gre_vocab_app', 'com.jhuni.sat_vocab_app')
content = content.replace('"GRE Vocabulary"', '"SAT Vocabulary"')

with open(gradle_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ build.gradle.kts 수정 완료")

# 3. Android AndroidManifest.xml 수정
manifest_path = os.path.join(base_path, "android", "app", "src", "main", "AndroidManifest.xml")
with open(manifest_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('android:label="GRE Vocabulary"', 'android:label="SAT Vocabulary"')

with open(manifest_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ AndroidManifest.xml 수정 완료")

# 4. MainActivity.kt 경로 변경
old_kotlin_path = os.path.join(base_path, "android", "app", "src", "main", "kotlin", "com", "jhuni", "gre_vocab_app")
new_kotlin_path = os.path.join(base_path, "android", "app", "src", "main", "kotlin", "com", "jhuni", "sat_vocab_app")
if os.path.exists(old_kotlin_path):
    os.rename(old_kotlin_path, new_kotlin_path)
    print("✅ Kotlin 폴더 이름 변경 완료")

# MainActivity.kt 패키지 이름 수정
main_activity_path = os.path.join(new_kotlin_path, "MainActivity.kt")
with open(main_activity_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('package com.jhuni.gre_vocab_app', 'package com.jhuni.sat_vocab_app')

with open(main_activity_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ MainActivity.kt 수정 완료")

# 5. iOS project.pbxproj 수정
ios_project_path = os.path.join(base_path, "ios", "Runner.xcodeproj", "project.pbxproj")
with open(ios_project_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('PRODUCT_BUNDLE_IDENTIFIER = com.jhuni.grevocabapp', 'PRODUCT_BUNDLE_IDENTIFIER = com.jhuni.satvocabapp')
content = content.replace('PRODUCT_NAME = "GRE Vocabulary"', 'PRODUCT_NAME = "SAT Vocabulary"')

with open(ios_project_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ iOS project.pbxproj 수정 완료")

# 6. iOS Info.plist 수정
info_plist_path = os.path.join(base_path, "ios", "Runner", "Info.plist")
with open(info_plist_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<string>GRE Vocabulary</string>', '<string>SAT Vocabulary</string>')

with open(info_plist_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ iOS Info.plist 수정 완료")

# 7. main.dart 수정 (앱 제목)
main_dart_path = os.path.join(base_path, "lib", "main.dart")
with open(main_dart_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("'GRE Vocabulary'", "'SAT Vocabulary'")
content = content.replace('"GRE Vocabulary"', '"SAT Vocabulary"')

with open(main_dart_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ main.dart 수정 완료")

# 8. home_screen.dart 수정
home_screen_path = os.path.join(base_path, "lib", "screens", "home_screen.dart")
with open(home_screen_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("'GRE Vocabulary'", "'SAT Vocabulary'")
content = content.replace('"GRE Vocabulary"', '"SAT Vocabulary"')
content = content.replace("'GRE '", "'SAT '")
content = content.replace('"GRE "', '"SAT "')

with open(home_screen_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ home_screen.dart 수정 완료")

# 9. ad_service.dart 수정 (광고 ID)
ad_service_path = os.path.join(base_path, "lib", "services", "ad_service.dart")
with open(ad_service_path, 'r', encoding='utf-8') as f:
    content = f.read()

# GRE 광고 ID를 SAT 광고 ID로 변경 (테스트 ID 유지)
# 실제 배포시 SAT 앱 광고 ID로 변경 필요

with open(ad_service_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ ad_service.dart 확인 완료")

# 10. purchase_service.dart 수정 (인앱 결제 ID)
purchase_service_path = os.path.join(base_path, "lib", "services", "purchase_service.dart")
with open(purchase_service_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('gre_', 'sat_')

with open(purchase_service_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ purchase_service.dart 수정 완료")

# 11. flutter_launcher_icons.yaml 확인/생성
icons_config = """flutter_launcher_icons:
  android: "launcher_icon"
  ios: true
  image_path: "assets/icon/app_icon.png"
  min_sdk_android: 21
  adaptive_icon_background: "#1E3A8A"
  adaptive_icon_foreground: "assets/icon/app_icon.png"
"""

# pubspec.yaml에 flutter_launcher_icons 설정 추가
with open(pubspec_path, 'r', encoding='utf-8') as f:
    content = f.read()

if 'flutter_launcher_icons' not in content:
    content = content + "\n" + icons_config
    with open(pubspec_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ flutter_launcher_icons 설정 추가 완료")

# 12. iml 파일 이름 변경
old_iml = os.path.join(base_path, "gre_vocab_app.iml")
new_iml = os.path.join(base_path, "sat_vocab_app.iml")
if os.path.exists(old_iml):
    os.rename(old_iml, new_iml)
    print("✅ .iml 파일 이름 변경 완료")

old_android_iml = os.path.join(base_path, "android", "gre_vocab_app_android.iml")
new_android_iml = os.path.join(base_path, "android", "sat_vocab_app_android.iml")
if os.path.exists(old_android_iml):
    os.rename(old_android_iml, new_android_iml)
    print("✅ Android .iml 파일 이름 변경 완료")

# 13. 불필요한 GRE 관련 파일 삭제
import glob
for f in glob.glob(os.path.join(base_path, "gen_batch*.py")):
    os.remove(f)
for f in glob.glob(os.path.join(base_path, "generate_gre*.py")):
    os.remove(f)
merge_file = os.path.join(base_path, "merge_words.py")
if os.path.exists(merge_file):
    os.remove(merge_file)
print("✅ 불필요한 파일 삭제 완료")

print("\n🎉 SAT 앱 설정 완료!")
print("다음 단계:")
print("1. 아이콘 파일 복사")
print("2. flutter pub get")
print("3. dart run flutter_launcher_icons")
print("4. flutter build appbundle --release")
