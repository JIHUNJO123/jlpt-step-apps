import os
import re

base_path = r"C:\Users\hooni\Desktop\sat_vocab_app_new"

# SAT 앱 설정
config = {
    "app_name": "SAT Vocabulary",
    "bundle_id": "com.jhuni.satvocabapp",
    "product_id": "sat_vocab_premium",
    
    # AdMob IDs
    "android_app_id": "ca-app-pub-5837885590326347~5018201928",
    "android_banner": "ca-app-pub-5837885590326347/3658579299",
    "android_interstitial": "ca-app-pub-5837885590326347/6767958368",
    "ios_app_id": "ca-app-pub-5837885590326347~5399036377",
    "ios_banner": "ca-app-pub-5837885590326347/2375726715",
    "ios_interstitial": "ca-app-pub-5837885590326347/8034429261",
}

# 1. Update ad_service.dart
ad_service_path = os.path.join(base_path, "lib", "services", "ad_service.dart")
with open(ad_service_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Replace AdMob IDs
content = re.sub(
    r"static const String _androidBannerId =\s*'[^']+';",
    f"static const String _androidBannerId =\n      '{config['android_banner']}';",
    content
)
content = re.sub(
    r"static const String _androidInterstitialId =\s*'[^']+';",
    f"static const String _androidInterstitialId =\n      '{config['android_interstitial']}';",
    content
)
content = re.sub(
    r"static const String _iosBannerId = '[^']+';",
    f"static const String _iosBannerId = '{config['ios_banner']}';",
    content
)
content = re.sub(
    r"static const String _iosInterstitialId =\s*'[^']+';",
    f"static const String _iosInterstitialId =\n      '{config['ios_interstitial']}';",
    content
)

with open(ad_service_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ ad_service.dart updated")

# 2. Update AndroidManifest.xml
manifest_path = os.path.join(base_path, "android", "app", "src", "main", "AndroidManifest.xml")
with open(manifest_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'android:value="ca-app-pub-[^"]+~[^"]+"',
    f'android:value="{config["android_app_id"]}"',
    content
)

with open(manifest_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ AndroidManifest.xml updated")

# 3. Update iOS Info.plist
info_plist_path = os.path.join(base_path, "ios", "Runner", "Info.plist")
with open(info_plist_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update GADApplicationIdentifier
content = re.sub(
    r'(<key>GADApplicationIdentifier</key>\s*<string>)[^<]+(</string>)',
    f'\\g<1>{config["ios_app_id"]}\\2',
    content
)

# Update CFBundleDisplayName
content = re.sub(
    r'(<key>CFBundleDisplayName</key>\s*<string>)[^<]+(</string>)',
    f'\\g<1>{config["app_name"]}\\2',
    content
)

# Update CFBundleName
content = re.sub(
    r'(<key>CFBundleName</key>\s*<string>)[^<]+(</string>)',
    f'\\g<1>sat_vocab_app\\2',
    content
)

with open(info_plist_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ Info.plist updated")

# 4. Update purchase_service.dart
purchase_path = os.path.join(base_path, "lib", "services", "purchase_service.dart")
with open(purchase_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r"static const String removeAdsProductId = '[^']+';",
    f"static const String removeAdsProductId = '{config['product_id']}';",
    content
)

with open(purchase_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ purchase_service.dart updated")

print("\n🎉 All configurations updated!")
print(f"""
SAT Vocabulary App Configuration:
================================
Bundle ID: {config['bundle_id']}
SKU: sat_vocab_app_ios
Privacy Policy: https://jihunjo123.github.io/sat-vocab-app/privacy
Marketing URL: https://jihunjo123.github.io/sat-vocab-app
Support URL: https://jihunjo123.github.io/sat-vocab-app/support
In-App Purchase ID: {config['product_id']}

Android AdMob:
- App ID: {config['android_app_id']}
- Banner: {config['android_banner']}
- Interstitial: {config['android_interstitial']}

iOS AdMob:
- App ID: {config['ios_app_id']}
- Banner: {config['ios_banner']}
- Interstitial: {config['ios_interstitial']}
""")
