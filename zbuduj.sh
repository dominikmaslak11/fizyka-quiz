#!/usr/bin/env bash
# Przebudowuje wszystko od zera: wzory, grafiki, JSON i APK.
set -euo pipefail
cd "$(dirname "$0")"
export JAVA_HOME=${JAVA_HOME:-/usr/lib/jvm/java-21-openjdk-amd64}
export ANDROID_HOME=${ANDROID_HOME:-$HOME/Android/Sdk}

echo "== 1/3 wzory i bank pytań =="
python3 narzedzia/zbuduj.py

echo
echo "== 2/3 grafiki modułów =="
python3 narzedzia/grafiki.py

echo
echo "== 3/3 aplikacja =="
echo "sdk.dir=$ANDROID_HOME" > android/local.properties
GRADLE=$(find "$HOME/.gradle/wrapper/dists" -name gradle -type f -path '*/bin/*' 2>/dev/null | sort | tail -1)
[ -x "$GRADLE" ] || GRADLE=$(command -v gradle)
(cd android && "$GRADLE" assembleDebug --console=plain -q)

cp android/app/build/outputs/apk/debug/app-debug.apk Fizyka-Quiz-v1.0-debug.apk
echo
echo "Gotowe: $(pwd)/Fizyka-Quiz-v1.0-debug.apk"
