# window_OCR

## 概要
window_OCRは、任意のウィンドウのスクリーンショットを撮影し、OCR（Optical Character Recognition）を用いてそのウィンドウの文字を抽出するツールです。このツールは、GUIアプリケーションのテキストデータを取得したり、スクリーンショットから文字情報を抽出する必要がある場合に便利です。

## 使用方法
1. 必要なパッケージのインストール
```bash
pip install -r requirements.txt
```
requirements.txtのほかに、paddlepaddleのインストールは下記urlの公式を参照

https://www.paddlepaddle.org.cn/en/install/quick?docurl=/documentation/docs/en/install/pip/windows-pip_en.html

2. 任意のウィンドウの設定
   show_window_names.pyを実行すると現在開いているすべてのウィンドウの名前を取得できる
   その中から任意のウィンドウを選択しそのウィンドウの名前をmain.pyの変数window_nameに代入

4. 実行
   任意のウィンドウが最小化、非表示されていないことを確認して実行することで、任意のウィンドウのテキストがコマンドラインに出力されます。
