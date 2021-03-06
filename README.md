# pyglview version 0.0.3

## Use glview with python3

glviewをPython3から利用できます。

## 動作確認環境

- ubuntu 21.10,Python 3.9.7
- ubuntu 22.04,Python 3.10.4
- glview: version 0.1.18 or later

- glviewのシェアードライブラリ経由でlibgles2又はlibOpenGLを呼び出します。
glviewは、libgles2を使用する場合、OpenGL/ES1.1のいくつかのAPIをエミュレーションします。  
（pyopenglは、使用せず、独自に実装しています。）  
現時点では、テストプログラムで必要なOpenGL/ES 2.0APIのみ動作確認しています。

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
chmod +x m mm simple-egl smoke test s001 s002
# コンパイル
./m
# ./m 又は ./m gles で、OpenGL/ES(libGLESv2.so)とリンクします。
# ./m opengl で、OpenGL(libOpenGL.so)とリンクします。

---------------------------------------------------------------------
pip3 install numpy

cd ../
git clone https://github.com/t-aikawa/pyglview.git
cd pyglview
```

## サンプルアプリ

```
txxx_basic.py       # C言語のAPIを呼び出した例
txxx_class.py       # クラスライブラリを経由して、呼び出した例

pip3 install opencv-contrib-python
opencv_video.py xxx.mp4     # opencvでmp4を再生

pip3 install matplotlib
matplotlib_sample.py        # matplotlibを使用した例
```

## 問い合わせ等は、以下のメールアドレスまで

```
aikawat@jcom.home.ne.jp
```

## サンプルアプリ(スクリーンショット)

### egl_class.py
<img width="300" alt="s001" src="./docs/Screenshot_egl_class.png">

### t003_class.py
<img width="300" alt="smoke" src="./docs/Screenshot_t003_class.png">

### matplotlib_sample.py
<img width="300" alt="simple-egl" src="./docs/Screenshot_matplotlib_sample.png">

 - マウスの左クリックで動かすと、視点を変更できます。