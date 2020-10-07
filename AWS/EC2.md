# AWS - EC2 서버 구축
```
  EC2 인스턴스 시작

먼저 VPC의 퍼블릭 서브넷에서 Amazon EC2 인스턴스를 생성합니다. 


EC2 인스턴스 시작

1.AWS Management 콘솔에 로그인한 다음 https://console.aws.amazon.com/ec2/에서 Amazon EC2 콘솔을 엽니다. 


2.다음과 같이 EC2 대시보드를 선택한 다음, 인스턴스 시작을 선택합니다. 



3.다음과 같이 Amazon Linux AMI를 선택합니다. 



중요

Amazon Linux 2 AMI에는 이 자습서에 필요한 소프트웨어 패키지가 없으므로 선택하지 마십시오. 


4.다음과 같이 t2.small 인스턴스 유형을 선택한 다음, Next: Configure Instance Details(다음: 인스턴스 세부 정보 구성)를 선택합니다. 



5.Configure Instance Details(인스턴스 세부 정보 구성) 페이지에서 다음과 같이 이러한 값을 설정하고 다른 값은 기본값으로 유지합니다. 


•Network: 프라이빗 서브넷과 퍼블릭 서브넷을 포함하는 VPC 생성에서 생성된 vpc-identifier | tutorial-vpc와 같이 DB 인스턴스에 대해 선택한 퍼블릭 및 프라이빗 서브넷이 있는 VPC를 선택합니다. 


•Subnet: 퍼블릭 웹 서버에 대해 VPC 보안 그룹 생성에서 생성된 subnet-identifier | Tutorial public | us-west-2a와 같이 기존 퍼블릭 서브넷을 선택합니다. 


•퍼블릭 IP 자동 할당: Enable(활성화)을 선택합니다. 


인스턴스 세부 정보 구성  


6.[Next: Add Storage]를 선택합니다. 


7.스토리지 추가 페이지에서 기본값을 유지하고 다음: 태그 추가를 선택합니다. 


8.태그 추가 페이지에서 다음과 같이 태그 추가를 선택한 다음 키에 Name을 입력하고 값에 tutorial-web-server를 입력합니다. 

태그 인스턴스  


9.[Next: Configure Security Group]을 선택합니다. 


10.Configure Security Group(보안 그룹 구성) 페이지에서 다음과 같이 Select an existing security group(기존 보안 그룹 선택)을 선택합니다. 그런 다음  퍼블릭 웹 서버에 대해 VPC 보안 그룹 생성에서 생성한 tutorial-securitygroup과 같은 기존 보안 그룹을 선택합니다. 선택한 보안 그룹에 SSH(Secure Shell) 및 HTTP 액세스에 대한 인바운드 규칙이 포함되어 있는지확인합니다. 

보안 그룹 구성  


11.Review and Launch(검토 및 시작)을 선택합니다. 


12.다음과 같이 [Review Instance Launch] 페이지에서 설정을 확인한 다음 [Launch]를 선택합니다. 

인스턴스 시작 검토  


13.다음과 같이 기존 키 페어 선택 또는 새 키 페어 생성 페이지에서 새 키 페어 만들기를 선택하고 키 페어 이름을 tutorial-key-pair로 설정합니다. [Download Key Pair]를 선택하고 로컬 시스템에 키 페어 파일을 저장합니다. 이 키 페어 파일을 사용하여 EC2 인스턴스에 연결하게 됩니다. 

기존 키 페이 선택 또는 새 키 페어 생성  


14.EC2 인스턴스를 시작하려면 [Launch Instances]를 선택합니다. 다음과 같이 [Launch Status] 페이지에서, 새 EC2 인스턴스의 식별자(예: i-0288d65fd4470b6a9)를 기록해 둡니다. 

​시작 상태  


15.View Instances(인스턴스 보기)를 선택하여 인스턴스를 찾습니다. 


16.인스턴스의 Instance Status(인스턴스 상태)가 running(실행 중)으로 읽힐 때까지 기다린 다음 계속합니다. 


  
  
```

```
ec2에서 wamp 설치
https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/WindowsGuide/install-WAMP.html - Window  wamp 설치 방법
```

#ec2 인스턴스 생성 
![port](https://user-images.githubusercontent.com/70589857/95282167-d44d9100-0893-11eb-9517-a24cfc68df35.png)






![EC2](https://user-images.githubusercontent.com/70589857/95281340-dd3d6300-0891-11eb-83aa-08954ae9ed42.PNG)

# 참고할 만한 사이트
https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateWebServer.html
