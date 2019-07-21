# DataRegistration
データの集積システム

## コマンドメモ

### プロジェクト作成
- ```pipenv run scrapy startproject プロジェクト名```

### スパイダーの作成（URL単位で作成）
- ```pipenv run scrapy genspider スクレイピングするURL ```

### 実行
- ```pipenv run scrapy crawl スパイダー名 -o 出力ファイルパス ```