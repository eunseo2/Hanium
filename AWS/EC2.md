# AWS - EC2 서버 구축
```
  Client - webserver - php - DB
  
  Client가 정보를 요청하면 웹서버는 html만 이해할 수 있으므로 php부분은 php에게 넘기고 php가 db에 정보를 요청하는 방식
```

# 문제 발생 + 해결과정
```
  php와 mysql을 연결 오류 발생
  
  root 계정이 2개가 원인이었음.
  
  localhost:3307 이라고 포트 번호를 명시해준 후 오류 해결
```

# 참고할 만한 사이트

https://www.php.net/manual/en/mysqlinfo.api.choosing.php
