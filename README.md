# pyglview

## Use glview with python3

## 動作確認環境

ubuntu 21.10,Python 3.9.7

pyopenglでは動作がおかしいので、glview経由でlibgles2を呼び出しています。

## ビルド＆動作手順

```bash
sudo apt install gcc
sudo apt install g++
sudo apt-get install libglib2.0*
sudo apt-get install libway*
sudo apt-get install wayland-protocols
sudo apt-get install libegl1-mesa libegl1-mesa-dev
sudo apt-get install libgles2-mesa-dev
sudo apt-get install libfreetype6-dev
sudo apt-get install libxkbcommon-dev
sudo apt-get install ibus-1.0
sudo apt-get install fcitx-libs-dev
sudo apt-get install libpng-dev
sudo apt-get install fonts-ipa*

sudo apt-get install ninja-build
sudo apt-get install meson

git clone https://github.com/t-aikawa/glview.git
cd glview
./m

---------------------------------------------------------------------

cd ../
git clone https://github.com/t-aikawa/pyglview.git
cd pyglview

python3 xxxx.py
```

## サンプルアプリ

- xxxx_basic.py : C言語のAPIを直接呼び出した例
- xxxx_class.py : クラスライブラリを経由して、呼び出した例

## 問い合わせ等は、以下のメールアドレスまで

```
aikawat@jcom.home.ne.jp
```
