<?php

?>
<!DOCTYPE html>
 <html lang = "ko">
 <head>
   <meta charset="utf-8">
   <title> 관리자 페이지</title>
   <style>
     h2 {
       text-align: center;
     }
     h3 {
       text-align: center;
       margin: 0 auto;
       border: 10px solid #dddddd;
       padding: 10px;
       width: 300px;
       box-sizing: 100px;
       background-color: white;
       line-height: 2.0;
     }
   </style>
 </head>
 <body>
   <h3>
     <u>WELCOME!!</u></p>
     주차장 서비스 이용하기
   <form method = "POST" action = "user_login.php" >
   <input type =  "submit" id = "btn1" value = "USER" />
   </form>
   <form method = "POST" action = "manager_login.php">
   <input type =  "submit" id = "btn2" value = "MANAGER" />
   </form>
   </h3>
 </body>
 </html>
