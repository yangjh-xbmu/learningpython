# MongoDB

MongoDB 是一款开源的非关系数据库管理软件，性能优异，在诸多大型项目中表现良好，是非关系型数据库的首选。

## 在macOS中的安装

MongoDB 只支持macOS 10.11及以后的产品。

### 使用包管理工具安装

我们使用在macOS 中的包管理工具Homebrew进行安装。

```bash
brew install mongodb
```

上述指令将安装MongoDB的最新发行版，并会自动安装MongoDB所需要的依赖环境。

### 运行前的准备

在启动MongoDB之前，需要创建MongoDB读写数据的目录，默认情况下，MongoDB会以`/data/db`为默认目录。下面的命令将创建默认的`/data/db`目录：

```bash
mkdir -p /data/db
```

创建目录后，为给目录指定读写权限。然后使用如下命令将MongoDB加入到系统服务中，以便每次启动时都可自动启动MongoDB服务。

```bash
brew services start mongodb
```

### 安装PyMongo库

启动虚拟python环境，然后通过pip安装PyMongo库：

```bash
 👉  source bin/activate
(spider) 
 👉  pip3 install pymongo
Collecting pymongo
  Downloading https://files.pythonhosted.org/packages/d7/ac/d2e324c1f9bcf653fa106785371a16b4709506a35b04948655de8b961a85/pymongo-3.7.2-cp37-cp37m-macosx_10_9_x86_64.whl (307kB)
    100% |████████████████████████████████| 317kB 1.6MB/s 
Installing collected packages: pymongo
Successfully installed pymongo-3.7.2
```

### 安装Robo 3T

MongoDB并没有默认的图形化管理工具，只提供Mongo shell的命令行方式。为了方便，我们还可以使用诸如Robo 3T这样的图形化管理工具进行查询、修改等管理工作。使用Homebrew安装：

```bash
brew install robo-3t
```

安装后，在应用程序中找到robo-3t，进行必要的配置（指定主机名和端口），即可对MongoDB进行管理。

## 连接MongoDB

使用PyMongo库，可以在Python中对MongoDB进行操作，连接到数据库，使用MongoClient方法即可：

```python
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
```

## 指定数据库

MongoDB中建立和使用数据库非常简单，直接指定数据库名称即可，如果该数据库不存在，MongoDB就会创建该数据库：

```python
db = client['weibo']
```

## 指定集合

MongoDB中的集合（collection），相当于MySQL等关系型数据库中的数据表（table），具体的信息，必须指定一个集合，才能进行存入、修改等操作。使用Collection对象，即可指定集合：

```python
import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['weibo']
collection = db['yangjh']
```

## 插入数据

推荐使用`insert_one()`和`insert_many()`方法来分别插入单条记录和多条记录。

```python
card = {
    "id": "20183210",
    "name": 'yangjh',
    "age": 20,
    'gender': 'male'
}

result = collection.insert_one(card)
print(result)
print(result.inserted_id)
```

运行结果为：

```bash
<pymongo.results.InsertOneResult object at 0x10436da48>
5bf8b3f897c32c4128ae8f6f
```

`insert_one()`方法返回一个对象，调用其`inserted_id`属性，可以获得`_id`字段的值。

还可以使用`insert_many()`方法，一次插入多条记录：

```python
card1 = {
    "id": "20183211",
    "name": 'yangzh',
    "age": 20,
    'gender': 'male'
}

card2 = {
    "id": "20183212",
    "name": 'yangzhh',
    "age": 40,
    'gender': 'female'
}
result = collection.insert_many([card1, card2])
print(result)
print(result.inserted_ids)
```

## 查询数据

查询数据，使用`find_one()`或`find()`方法进行查询，顾名思义，`find_one()`方法查询结果是单条，而`find()`方法返回全部结果。

```python
results = collection.find({'age': 20})
print(results)
for result in results:
    print(result)
```

运行结果为：

```bash
<pymongo.cursor.Cursor object at 0x103afe550>
{'_id': ObjectId('5bf8b3f897c32c4128ae8f6f'), 'id': '20183210', 'name': 'yangjh', 'age': 20, 'gender': 'male'}
{'_id': ObjectId('5bf8b81c97c32c433d302e60'), 'id': '20183210', 'name': 'yangjh', 'age': 20, 'gender': 'male'}
{'_id': ObjectId('5bf8b81c97c32c433d302e61'), 'id': '20183211', 'name': 'yangzh', 'age': 20, 'gender': 'male'}
```

可以看出，查询结果为Cursor类型，是一个生成器，需要遍历才能获取其中所有的结果。

在使用find()或find_one()方法时，需要以对象的形式传入查询条件。常见的查询条件总结如下：

|  符号   |      含义      |             示例              |
| ------- | -------------- | ----------------------------- |
|         | 等于           | {'age':20}                    |
| $lt     | 小于           | {'age':{'$lt':20}}            |
| $gt     | 大于           | {'age':{'$gt':20}}            |
| $lte    | 小于等于       | {'age':{'$lte':20}}           |
| $gte    | 大于等于       | {'age':{'$gte':20}}           |
| $ne     | 不等于         | {'age':{'$ne':20}}            |
| $in     | 在范围内       | {'age':{'$in':[20,30]}}       |
| $nin    | 不在范围内     | {'age':{'$nin':[20,30]}}      |
| $regex  | 匹配正则表达式 | {'name':{'$regex':'^yangzh'}} |
| $exists | 属性是否存在   | {'age':{'$exists':True}}      |
| $type   | 类型判断       | {'age':{'$type':'int'}}       |
| $text   | 文本查询       | {'$text':{'$search':'yang'}}  |
| $where  | 高级条件查询   | {'$where':'python表达式'}     |

## 计数

可以使用`count()`方法统计查询结果的数量。

## 排序

使用`sort()`方法进行排序，排序时需要传入字段名及升降序标记，如：

```python
results = collection.find().sort('name')
```

将以name字段为依据，按照字母升序进行排序。若要倒序，则传入`pymongo.DESCENDING`。

## 偏移和限定

使用`skip()`方法，可以从指定的位置获取查询结果。使用`limit()`方法，可以限定返回的数量结果。

## 更新

使用`update_one()`方法和`update_many()`方法，可以更新符合条件的数据。

## 删除

使用`delete_one()`方法和`delete_many()`方法，可以删除符合条件的数据。

## 其他操作

还可以使用类似`fine_one_and_delete()`的方法，对数据进行操作。

## 参考资料

1. [https://docs.mongodb.com/](https://docs.mongodb.com/)
1. [https://api.mongodb.com/python/current/](https://api.mongodb.com/python/current/)
1. [MongoDB查询操作符手册](https://docs.mongodb.com/manual/reference/operator/query/)
