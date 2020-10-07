# RDS

```
 -VPC 설정해야함

```

# VPC
```
공용 인터넷이 아닌 웹 서버에서만 DB 인스턴스를 사용할 수 있어야 하므로 퍼블릭 및 프라이빗 서브넷이 모두 있는 VPC를 생성합니다. 퍼블릭 서브넷에서웹 서버를 호스팅하므로 웹 서버에서 퍼블릭 인터넷에 액세스할 수 있습니다. DB 인스턴스는 프라이빗 서브넷에서 호스팅됩니다. 동일한 VPC에서 호스팅되므로웹 서버에서는 DB 인스턴스에 연결할 수 있지만, 퍼블릭 인터넷에서는 DB 인스턴스에 액세스할 수 없어 보다 강화된 보안이 가능합니다. 

VPC 및 서브넷을 생성하는 방법

1.https://console.aws.amazon.com/vpc/에서 Amazon VPC 콘솔을 엽니다. 

2.AWS Management 콘솔의 오른쪽 상단 모서리에서 VPC를 생성할 리전을 선택합니다. 이 예에서는 미국 서부(오레곤) 리전을 사용합니다.

3.왼쪽 상단 모서리에서 [VPC Dashboard]를 선택합니다. VPC 생성을 시작하려면 VPC 마법사 시작을 선택합니다. 

4.[Step 1: Select a VPC Configuration] 페이지에서 [VPC with Public and Private Subnets]를 선택한 후 [Select]를 선택합니다. 

5.[Step 2: VPC with Public and Private Subnets] 페이지에서 다음 값을 설정합니다. 

•IPv4 CIDR block: 10.0.0.0/16

•IPv6 CIDR block: No IPv6 CIDR Block 

•VPC name: tutorial-vpc

•Public subnet's IPv4 CIDR: 10.0.0.0/24

•가용 영역: us-west-2a

•Public subnet name: Tutorial public

•Private subnet's IPv4 CIDR: 10.0.1.0/24

•가용 영역: us-west-2a

•Private subnet name: Tutorial Private 1 

•Instance type: t2.small

중요

콘솔에 인스턴스 유형 상자가 표시되지 않으면 대신 NAT 인스턴스 사용을 선택합니다. 이 링크는 오른쪽에 있습니다. 
t2.small 인스턴스 유형이 표시되지 않으면 다른 인스턴스 유형을 선택할 수 있습니다.


•Key pair name: No key pair

•Service endpoints: Skip this field. 

•Enable DNS hostnames: Yes

•Hardware tenancy: Default

6.작업을 마쳤으면 [Create VPC]를 선택합니다. 

```

# 참고사이트
https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateVPC.html#CHAP_Tutorials.WebServerDB.CreateVPC.VPCAndSubnets -VPC


https://aws.amazon.com/ko/getting-started/hands-on/create-mysql-db/ - RDS
