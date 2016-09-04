# 反省点

- [ ] Top-k 系のクエリはRedisが速い。
- [ ] 始まった段階で各種ログを取って集計したい。
    - クエリログ
        - 全クエリ出してN+1っぽいのを検出
        - `log_queries_not_using_indexes` でインデックス効いてないクエリをチェック
        - `pt-query-digest` で集計して遅いクエリをランキングで見る
    - Nginxのアクセスログ
        - kataribeで集計し、ページ単位での遅さランキングを出す
- [ ] 設定ファイルのプリセットを用意。
    - MySQL
       - `innodb_buffer_pool_size`
    - Nginx
       - `gzip`
       - `unix domain socket`
    - Redis
       - Persistentの長さ設定(オンメモリになるようにする)

## Next Action

### 澤田

- my.cnf, nginx.confの準備
- Redisの準備(設定ファイル込み)
- 諸々インストーラを作る

### 中谷

- Ruby (sinatra, rails) からRedis使えるようにしておく


# localhostで走らせる

## DBの設定

```bash
sudo ln -s /var/run/mysqld/mysqld.sock /tmp/mysql.sock
```

```bash
mysql -uroot -e 'create database isucon5q'
mysql -uroot isucon5q < schema.sql
mysql -uroot isucon5q < create_user.sql
mysql -uroot isucon5q < isucon5q.dev.sql
```

## DBの中身を一部本番に合わせる(必須)

```bash
insert into users (id, account_name, nick_name, email, passhash) values(3657, 'edwardo3657', 'タダハル', 'edwardo3657@isucon.net', '5f3f6cb518fc304c5014a494e39ce12a4e4567733158b3aca9cd3861936ec92ea86f62fcf2997b380db48dc8877b1268f90138b4d365889f956f72424b36a14b');
insert into salts (user_id, salt) values (3657, 'b2945e');
```

## topページでのログインアカウント

- user: edwardo3657@isucon.net
- pass: edwardo3657

# deploy


## pull

ソースファイルの pull および bundle install

```bash
fab pull
```

## status

アプリケーションサーバのステータス確認

```bash
fab status
```

## restart_ruby

アプリケーションサーバのリスタート

```
fab restart_ruby
```

## restart_nginx

nginx のリスタート

```
fab restart_nginx
```

## deploy

pull, restart_ruby, restart_nginx の実行

```
fab deploy
```

