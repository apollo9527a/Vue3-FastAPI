## sqlalchemy 同步/异步压力测试

>接口调用200次

### 1. 同步

+ `Sqlite`

  ![](./images/sqlite_sync_read_start.png)

  ![](./images/sqlite_sync_read_end.png)

  ><font color="red">耗时 `18` s</font>

+ `Mysql`

  ![](./images/mysql_sync_start.png)

  ![](./images/mysql_sync_end.png)

  ><font color="red">耗时 `18` s</font>

+ `Postgresql`

### 2.  异步

+ `Sqlite`

  ![](./images/sqlite_async_read_start.png)

  ![](./images/sqlite_async_read_end.png)

  ><font color="red">耗时近 `18` s</font>

+ `Mysql`

  ![](./images/mysql_async_start.png)

  ![](./images/mysql_async_end.png)

  ><font color="red">耗时近 `18` s</font>

+ `Postgresql`

  >出错。。





想不明白为什么耗时都是一样。。。！！！！