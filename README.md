Under :construction:

## 準備　

### 前処理

mecabで形態素解析する場合は、`tools/mecab.py`を使います。

```
python mecab.py -i INPUT_DIR -o OUTPUT_DIR
```

ディレクトリ内のテキストファイルを分割し、同じファイル名で出力ディレクトリに保存します。

ネットスラングなどが多いデータの場合は[NPYLM](https://github.com/musyoku/python-npylm)による教師なし形態素解析が有効です。

### ビルド

```
make install
```

CSTMの学習速度はコンパイラに影響されます。

Intelのicpcがあれば使った方が学習速度が速いです（1.3倍程度）。

## 学習

```
python train.py -d DOCUMENT_DIR -dim 20 -ignore 3
```

オプション
- -d
	- 文書ファイルが入っているディレクトリ
- -dim
	- 文書・単語ベクトルの次元数
- -ignore
	- 出現頻度がこの値以下の単語は学習しない
	- 学習の高速化のために行う
- -thread
	- 文書ベクトルの更新をマルチスレッドで行う場合のスレッド数

- -m
	- 学習されたモデルを保存するファイルのパス

## プロット

`plot`にプロット用スクリプトが入っています。

### 文書ベクトルの可視化

```
python doc.py
```

各次元ごとにプロットします。

### 単語ベクトルの可視化

```
python word.py
```

各次元ごとにプロットします。

実際にプロットされるのは点ではなく単語の文字です。

### fの可視化

```
python f.py -doc 0
```

指定された文書のベクトルと各単語のベクトルのfを計算しプロットします。

実際にプロットされるのは点ではなく単語の文字です。

## ワードクラウド

文書の特徴を可視化できます。



