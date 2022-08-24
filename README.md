# python_DataStructure

1. (자료구조) 리스트 List
- 일렬로 나열되어 있음
- 순서가 있음
- 추가: 원하는 위치
- 삭제: 원하는 위치

2. (자료구조) 스택 Stack
- 일렬로 나열되어 있음
- 순서가 있음
- 추가: 제일 위에
- 삭제: 제일 위에

배열: [1,2,3,4]
- 배열 + insert(), del, remove(): 리스트 역할
- 배열 + pop(), append(): 스택 역할

큐(Queue): 스택의 업그레이드 버전 -> 결국은 리스트라는 말
- 순서 상관 있음
- 추가(삽입 enqueue): 뒤에서 ex.)지하철 줄서는 순서
- 삭제(제거 dequeue): 앞에서 ex.)지하철 타는 순서

선형 큐(Linear Queue)
- 꽉 찼다 = isfull(), 비었다 = isEmpty() 
- 빨간 화살표(front) 보다 파란색 화살표(rear)가 한칸 전에 있으면 
- 빨간 화살표 && 파란 화살표가 같은 곳울 가리킬때
- 
원형 큐(Circular Queue)
- enqueue: 파란 화살표(rear)가 가르카는 곳에 추가
- dequeue: 빨간 화살표(front)가 가르키는 곳을 삭제

init(): 초기화 >> Front, Rear를 제일 앞자리(0) 설정


생성자의 역할 2가지
1) 객체 생성
2) 객체의 태어날때부터 가져야하는 정보를 초기화
ex) 자동차의 색상, 사람의 혈액형, 카메라의 화소, 붕어빵의 앙금,...
- 역할 1번만 할 때: 생성자를 내 손으로 안 만듦
- 역할 1번 & 2번 할 때: 생성자를 직접 만듦

self
- 객체 자신
- 클래스 외부에서 클래스 함수를 부를 때 누가 불렀는지 확인하는 

__이름__: public 
- 프로젝트 안에서 마음대로 불러 쓸 수 있는 오픈 마인드 변수, 함수
__이름: private
- 클래스 밖을 나가면 아무도 못부르는 변수

0. 웹개발
- 프론트엔드
- html: 웹 개발 제일 바깥 껍데기
- css: html을 꾸며주는 친구
- javascript(js): html & css를 제어하는 친구

- 7일차: (자료구조)큐, 선택정렬
- 8일차: 클래스, 생성자// 튜플
- 9일차: (자료구조)트리
- 10일차: 트리, (자료구조)힙
