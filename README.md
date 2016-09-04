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
