#! /usr/bin/bash
set -ex

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

pkgs=(ffmpeg )
ns=""
export CONAN_USER_HOME=$DIR/conan_cache

rm -rf $CONAN_USER_HOME
rm conan.lock

for pkg in "${pkgs[@]}"; do
  pushd $pkg
  conan export . $ns
  popd
done


conan export variant $ns
conan graph lock --build --lockfile . variant
conan graph build-order --build cascade --build outdated .
cat conan.lock
conan create --build ffmpeg/1.0 --test-folder=None -ne --lockfile . ffmpeg

exit
