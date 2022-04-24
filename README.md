## sqlalchemy 同步/异步压力测试

>接口调用200次

### 1. 同步

+ `Sqlite`

  ![](./images/sync_or_async/sqlite_sync_read_start.png)

  ![](./images/sync_or_async/sqlite_sync_read_end.png)

  ><font color="red">耗时 `18` s</font>

+ `Mysql`

  ![](./images/sync_or_async/mysql_sync_start.png)

  ![](./images/sync_or_async/mysql_sync_end.png)

  ><font color="red">耗时 `18` s</font>

+ `Postgresql`

### 2.  异步

+ `Sqlite`

  ![](./images/sync_or_async/sqlite_async_read_start.png)

  ![](./images/sync_or_async/sqlite_async_read_end.png)

  ><font color="red">耗时近 `18` s</font>

+ `Mysql`

  ![](./images/sync_or_async/mysql_async_start.png)

  ![](./images/sync_or_async/mysql_async_end.png)

  ><font color="red">耗时近 `18` s</font>

+ `Postgresql`

  ><font color="red">耗时近 `18` s</font>

想不明白为什么耗时都是一样。。。！！！！



## FastAPI 并发压力测试(同步/异步)

```python
@app.get("/")
async def root():
    return {"message": "Hello World"}
```

### 1. 同步

![](images/concurrent/sync_concurrent_1000_1.png)

![](images/concurrent/sync_concurrent_1000_2.png)

![](images/concurrent/sync_concurrent_1000_3.png)

![](images/concurrent/sync_concurrent_1000_4.png)

![](images/concurrent/sync_concurrent_1000_5.png)

### 2. 异步

![](images/concurrent/async_concurrent_1000_1.png)

![](images/concurrent/async_concurrent_1000_2.png)

![](images/concurrent/async_concurrent_1000_3.png)

![](images/concurrent/async_concurrent_1000_4.png)

![](images/concurrent/async_concurrent_1000_5.png)