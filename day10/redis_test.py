
import redis


r = redis.Redis(host = '172.16.38.133', port=6379)

r.set("QF", "www.qfedu.com")
print(r.get("QF").decode())





























































