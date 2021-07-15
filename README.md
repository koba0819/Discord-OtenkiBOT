# Discord用のお天気を教えてくれるBOT　python学習用

### Herokuでの利用を想定しています

## 実行環境
Python3.6以上

## 必要なもの
.env

requests

discord.py rewrite

## 導入
Herokuへリポジトリを連携するだけで動作します

必要なのは.env.sampleのリネームとTOKEN_KEYの設定です

例: ```.env.sample -> .env```

例: ```TOKEN_KEY "" -> TOKEN_KEY "test0123456789"```

## 使用方法
discordへBOTを招待し、都道府県を付けずにメッセージへ書き込みます

例: ```東京```

例: ```大阪```

今日 明日 明後日の3日分の天気予報がメッセージで帰ってきます

**注意:最後に"都道府県"をつけると反応しません**

## 使用した技術
livedoor 天気API

