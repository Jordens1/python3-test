#/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
github 上面有redis-windows  配置  maxheap 1024000000  requirepass  sunck
auth sunck   redis的可视化工具  redis Desktop manager
redis 是键值对的形式 键值是字符串：值是 字符串string、哈希hash、集合set、有序集合zset、、列表list

文档：http://www.redis.cn/commands.html#generic

string
 是redis的最简单的类型，最大512M，二进制的，什么都可以存
set key value    setex key seconds value 过期时间   mset key value [key value]
get    mget
运算： incr key加一   decr key 减一  incrby key intnum 加整数   decrby key intnum
追加： append key value   strlen key  获取长度

key
 支持正则  key *   exists key   type key  del key   expire key seconds   ttl key

hash    {name:"tom", age:18}
  hset key field value   hmset key field value [field value ..]
  hget key field    hmget key field [field ..]    hgetall key   hkeys key   hvals key   hlen key
  hexits key field   hdel keu field [field ..]   hstrlen key field

list
  lpush key value [..]   rpush key value [..]   linsert key before|after value   lset key index value
  lpop key   rpop key   lrange key start_index end_index
  ltrim key start end   llen key    lindex key index

set
  sadd key member [..]   smember key   scard key
  sinter key [..]   sdiff key [key ..]   sunion key [..]   sismember key member

zset :有序的集合，里面的元素唯一性，元素通过里面的score（权重值）排序
  zadd key score member [score member ..]
  zrange key start end   zcard key   zcount key min max   zscore key member

'''
import redis

#连接
r = redis.StrictRedis(host="localhost", port=6379, password="xishi")
#r = redis.Redis(host="localhost", port=6379, password="xishi")

#方法一 ：根据数据类型的不同，调用响应的方法
#写
r.set("p1", "good")
#读    其余命令类似
print(r.get("p1"))

#方法二：pipline
#缓冲多条命令，依次执行，减少tcp连接
pipe = r.pipeline()
pipe.set("p2", "nice")
pipe.set("p3", "handsome")
pipe.set("p4", "cool")
pipe.execute()












