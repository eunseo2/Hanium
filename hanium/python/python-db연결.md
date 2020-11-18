# python-db연결
pip-mysql 
![pip-mysql](https://user-images.githubusercontent.com/70589857/95280505-1bd21e00-0890-11eb-89e5-574ab076f29f.PNG)
```
 import pymysql

conn = pymysql.connect(host='localhost', user='root', password=pw,db='park', charset='utf8') //mysql park db pw 비번 

curs = conn.cursor()

sql = "insert into parking_area (car_num,parking_area_location) values(%s,%s)"

val = ("13가 1234","나-1")

curs.execute(sql,val)

conn.commit()
 

```

# 참고할 만한 사이트

https://yanguelna-programmer.tistory.com/43
