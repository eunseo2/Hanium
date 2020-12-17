# 한이음 IoT 기반 스마트 공유 주차 관리 시스템 구축


## 영상 링크

https://www.youtube.com/watch?v=Ov4Ln_jivjA


 ## 프로젝트 소개
  ### 기획의도
  - 인력 기반 주차 관리의 개선
  - 정기 주차 차량과 방문 주차 차량의 구분
  - 전기 자동차와 장애인 주차 구역의 관리의 활성화

  ### 작품 내용
  - 정기(거주자) 차량 주차 시간 패턴 분석 후 주차 가용 공간 예측
  - IoT 기반 스마트 공유 주차관리 인프라팀 과의 통신을 이용한 주차 관리
  - 정기(거주자)/방문자 데이터를 이용해 가용 주차구역을 실시간 예측 및 확대
  - OpenCV로 영상 데이터를 분석하여 전기 자동차, 장애인 자동차 식별
  - 지정 주차구역(전기자동차, 장애인) 실시간 관리
  - 차량 번호판 정보를 통해 정기(거주자) 및 방문자 차량을 구분하는 시스템
  - 정기 차량의 주차 위치, 주차 시간 및 주차 가능한 공간을 알려주는 시스템
  - 주차장 시각화를 통해 실시간 주차장 정보 및 차량 정보 제공
  
  ## 개발배경 및 필요성
   
 ### 개발 배경
  - 공용 주차공간을 사용하여 정기 주차 차량과 방문 주차 차량을 수용하는 경우 
    방문 주차 차량의 주차 현황을 알 수 없음. 이로 인해 정기 거주 차량의  
    주차 구역 이용 불편 사항 발생
  - 지정 주차 구역(전기자동차, 장애인 등)에 일반 차량이 주차를 하더라도 현재
    는 인력에 의존하여 관리하는 시스템
  - 방문자 차량의 주차 공간 점유, 불법 주차로 인한 주차 공간 부족으로 거주민   
    (정기주차) 차량 주차 공간 확보의 어려움과 이로 인한 주거 공간 침해 심각
  - 주차된 차량의 위치를 차주의 기억에 의존하여 주차차량 찾기에 불편함 존재
      

 ### 필요성
  - 지정 주차 구역(전기자동차, 장애인 등)의 무인 관리와 공간 확보 필요
  - 정기 주차 차량과 방문 주차 차량의 주차 상태 파악, 지정 주차 구역 주차차량  
    인식을 무인화 한다면 인력 기반 주차관리 시스템 개선
  - 정기 거주 차량의 가용 주차 공간 확보에 유리한 시스템
  - 실시간 주차 정보를 제공해 주차된 차량의 원활한 위치 파악  
     

  

## 구축 환경
- 웹 서버 : Ubuntu - AWS EC2, Apache Web Server
- 데이터베이스 : mariaDB
- 프론트엔드 언어 : HTML
- 백엔드 언어 : PHP




## 제공 기능
- OpenCV를 이용하여 차량번호 식별
- 영상 분석 데이터를 기반으로 전기 자동차, 장애인 자동차 등록 여부 판단 및 지정 주차 구역 위반 차량 식별
- parking, parking_area, user, manager, resident_long-term, resident table PARK DB 구축
- R 프로그램을 이용하여 정기 거주자 차량의 시간 패턴을 분석
- 관리자 웹 페이지 구축
- 사용자 웹 페이지 구축


   
##### 서비스 흐름도

<img width="1000" src="https://user-images.githubusercontent.com/70589857/102481201-bf1b8c80-40a4-11eb-8c90-8bd7fa5bb301.png">


##### OpenCv
- 차량 번호 인식
<img width="1000" src="https://user-images.githubusercontent.com/70589857/102481552-351ff380-40a5-11eb-8cc9-ae5db504b416.png">

- 장애인 차량 스티커 인식
<img width="1000" src="https://user-images.githubusercontent.com/70589857/102481607-4963f080-40a5-11eb-8fac-a15cbc1fb8e6.png">


### 관리자 웹 페이지
<img width="1000" src="https://user-images.githubusercontent.com/70589857/102481733-79ab8f00-40a5-11eb-84a7-333c500cc2a2.PNG">
    1. 관리자 로그인
    2. 관리자 페이지의 홈 화면
    3. 주차장 실시간 확민 및 특수 구역 관리
    4. 차량 번호 조회를 통한 거주자의 정보 확인
    5. 장기 주차 차량 조회 및 출차 유도를 통한 관리
    
### 사용자 웹 페이지
<img width="1000" src="https://user-images.githubusercontent.com/70589857/102481810-9ba51180-40a5-11eb-8696-ad2349e715da.PNG">

  1. 프론트 페이지에서 사용자/매니저 구분 및 회원가입
  2. 사용자 로그인
  3. 사용자 페이지에서 현재 잔여 좌석 확인

   
## 역할분담

 - 김은서 : AWS EC2, manager web, DB 
 - 김보연 : R, AWS S3 , web css
 - 이소윤 : OpenCV,  AWS S3 , web css
 - 홍민아 : AWS EC2, user web
