
# localhostで走らせる

## DBの設定

```bash
sudo ln -s /var/run/mysqld/mysqld.sock /tmp/mysql.sock
```

```bash
mysql -uroot -e 'create database isucon5q'
mysql -uroot isucon5q < schema.sql
mysql -uroot isucon5q < create_user.sql
mysql -uroot isucon5q < isucon5q.dev.sql```
```

## topページでのログインアカウント

- user: moris@tagomor.is
- pass: moris11

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

