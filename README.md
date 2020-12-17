# 한이음 IoT 기반 스마트 공유 주차 관리 시스템 구축


## 영상 링크

https://www.youtube.com/watch?v=Ov4Ln_jivjA

## 프로젝트 개요


 ## 프로젝트 소개
 1. 기획의도
  1) 인력 기반 주차 관리의 개선
  2) 정기 주차 차량과 방문 주차 차량의 구분
  3) 전기 자동차와 장애인 주차 구역의 관리의 활성화

2. 작품 내용
  1)정기(거주자) 차량 주차 시간 패턴 분석 후 주차 가용 공간 예측
  2) IoT 기반 스마트 공유 주차관리 인프라팀 과의 통신을 이용한 주차 관리
  3) 정기(거주자)/방문자 데이터를 이용해 가용 주차구역을 실시간 예측 및 확대
  4) OpenCV로 영상 데이터를 분석하여 전기 자동차, 장애인 자동차 식별
  5) 지정 주차구역(전기자동차, 장애인) 실시간 관리
  6) 차량 번호판 정보를 통해 정기(거주자) 및 방문자 차량을 구분하는 시스템
  7) 정기 차량의 주차 위치, 주차 시간 및 주차 가능한 공간을 알려주는 시스템
  8) 주차장 시각화를 통해 실시간 주차장 정보 및 차량 정보 제공
  
  ## 개발배경 및 필요성
   
  1. 개발 배경
      - 공용 주차공간을 사용하여 정기 주차 차량과 방문 주차 차량을 수용하는 경우 
        방문 주차 차량의 주차 현황을 알 수 없음. 이로 인해 정기 거주 차량의  
        주차 구역 이용 불편 사항 발생
      - 지정 주차 구역(전기자동차, 장애인 등)에 일반 차량이 주차를 하더라도 현재
        는 인력에 의존하여 관리하는 시스템
      - 방문자 차량의 주차 공간 점유, 불법 주차로 인한 주차 공간 부족으로 거주민   
        (정기주차) 차량 주차 공간 확보의 어려움과 이로 인한 주거 공간 침해 심각
      - 주차된 차량의 위치를 차주의 기억에 의존하여 주차차량 찾기에 불편함 존재
      

   2. 필요성
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
- 각 구의 대여 반납 이용량을 시각화한 그래프 확인(한 달 기준)
- 각 구별 자전거 포화 대여소 확인
- 각 구별 자전거 부족 대여소 확인
- 입력한 자전거 대여소의 자전거 대수 포화/부족 상태 확인
- 입력한 자전거 대여소와 1km이내 범위의 가장 가까운 순으로 대여소 추천

## 각 페이지 별 소개 및 이용 방법
### 1. Index 페이지 
   - 자전거 포화/부족 확인 화면 연결
   - 원하는 대여소와 시간 상태 확인 화면 연결 
<img width="600" src="https://user-images.githubusercontent.com/53183320/102006605-a38f4980-3d65-11eb-84a3-92739e018e69.PNG">


### 2. 자전거 포화/부족 상태 확인과 구별 대여, 반납 비교 그래프
   - 전체 대여소의 자전거 포화/부족 상태 확인
   - 구를 입력하면 원하는 구의 포화/부족 상태 확인 가능
   
   ### 2-1. 포화 상태 확인. ex) 성북구 검색 시 성북구 내 대여소의 포화 상태 확인
   <img width="600" alt="exceed" src="https://user-images.githubusercontent.com/53183320/102006609-a853fd80-3d65-11eb-8abf-97724b7d873b.PNG">
   <img width="600" alt="exceed_gu" src="https://user-images.githubusercontent.com/53183320/102006615-ab4eee00-3d65-11eb-871b-3a9420f87803.PNG">
   
   ### 2-2. 부족 상태 확인. ex) 강서구 검색 시 강서구 내 대여소의 포화 상태 확인
   <img width="600" alt="shortage" src="https://user-images.githubusercontent.com/53183320/102006623-b30e9280-3d65-11eb-955f-17548fa25e04.PNG">
   <img width="600" alt="shortage_gu" src="https://user-images.githubusercontent.com/53183320/102006621-b1dd6580-3d65-11eb-9ec8-300bf18041b3.PNG">
   
   ### 2-3. 구별로 자전거 대여, 반납 개수를 한 눈에 쉽게 비교하기 위하여 막대 그래프로 표현
   <img width="600" alt="graph" src="https://user-images.githubusercontent.com/53183320/102006630-bb66cd80-3d65-11eb-8936-169fccef0d55.PNG">

##### 예외처리
   - 텍스트(구 이름) 입력 안하고 search버튼 클릭 시 오류메시지 출력
   <img width="200" alt="e1" src="https://user-images.githubusercontent.com/70579136/102008662-9417fc80-3d75-11eb-95c2-8af9a5f2c7e1.PNG">
   
   - 숫자, 영어, 기호, 초성이 하나라도 포함되어 있을 시 오류메시지 출력
<br>(순서대로 숫자, 기호, 영어, 초성, 혼합 입력 시 화면)<br>
<img width="200" alt="e2" src="https://user-images.githubusercontent.com/70579136/102008664-9712ed00-3d75-11eb-8c87-12ad85e092bf.PNG"><img width="200" alt="e3" src="https://user-images.githubusercontent.com/70579136/102008663-967a5680-3d75-11eb-8b8d-7514e985169d.PNG"><img width="200" alt="e4" src="https://user-images.githubusercontent.com/70579136/102008678-a003be80-3d75-11eb-9417-7ef246941fd2.PNG"><img width="200" alt="e5" src="https://user-images.githubusercontent.com/70579136/102008683-a1cd8200-3d75-11eb-8870-500571f718b0.PNG"><img width="200" alt="e6" src="https://user-images.githubusercontent.com/70579136/102008686-a42fdc00-3d75-11eb-87fe-b1e8ca17adb5.PNG">



### 3. 시간대별 대여소의 자전거 포화, 부족 상태 확인 및 가까운 대여소 추천 페이지 
   - 원하는 대여소의 대여소 번호를 입력
   <img width="600" src="https://user-images.githubusercontent.com/53183320/102007055-11894000-3d69-11eb-9f28-aa1d6624d4eb.PNG">
   
   - 원하는 시간대를 한 시간 단위로 선택
  <img width="600" src="https://user-images.githubusercontent.com/53183320/102007090-59a86280-3d69-11eb-8e38-09bcf88cfadf.PNG">
  
   - 모든 항목을 입력하고 go 버튼을 클릭
   <img width="600" src="https://user-images.githubusercontent.com/70579136/102007369-e3f1c600-3d6b-11eb-93e8-52492358f1bb.PNG">
   
   1) 선택한 시간대 확인<br>
   2) 입력한 대여소의 대여소 명 확인<br>
   3) 입력한 대여소의 자전거 포화, 부족 상태 확인<br>
   4) 입력한 대여소와 일정 거리 내에 있는 대여소가 가장 가까운 5개의 대여소 출력<br>
   5) 클릭 시 index.php 페이지로 이동
   
##### 예외처리
   - 대여소번호 입력 안하고 GO 버튼 클릭 시 오류메시지 출력
<img width="200" src="https://user-images.githubusercontent.com/70579136/101985840-bd7d4d80-3ccd-11eb-9234-8c08d429ac53.PNG">
   
   - 대여소 번호에 숫자외의 값이 들어가면 오류메시지 출력 (순서대로 한글, 영어, 기호 입력 시 화면)

<img width="200" src="https://user-images.githubusercontent.com/70579136/101985854-cbcb6980-3ccd-11eb-82c8-f2506a16e0a6.PNG"><img width="200" src="https://user-images.githubusercontent.com/70579136/101985856-d1c14a80-3ccd-11eb-9152-3938b25a9e58.PNG"><img width="200" src="https://user-images.githubusercontent.com/70579136/101985855-d0901d80-3ccd-11eb-99be-313514a53ed6.PNG"> 
   
   - 시간대 선택 안하고 GO 버튼 클릭 시 오류메시지 출력
<img width="200" src="https://user-images.githubusercontent.com/70579136/101985844-c110d480-3ccd-11eb-820f-abc8f541db10.PNG">   
   
   - 없는 대여소번호를 입력하거나 대여기록이 없는 대여소번호 입력 시 오류페이지로 이동
<img width="500" src="https://user-images.githubusercontent.com/70579136/101985858-d554d180-3ccd-11eb-91a3-6dd723c77352.PNG">


## 역할분담

 - 김은서 : AWS EC2, manager web, DB 
 - 김보연 : R, AWS S3 , web css
 - 이소윤 : OpenCV,  AWS S3 , web css
 - 홍민아 : AWS EC2, user web
