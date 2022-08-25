# python_DataStructure

자료구조: 원래 그렇게 생기지 않았지만 그 모양으로 생겼다고 생각하는 

(자료구조) 리스트 List
- 일렬로 나열되어 있음
- 순서가 있음
- 추가: 원하는 위치
- 삭제: 원하는 위치

(자료구조) 스택 Stack
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

 __ 이름 __: public 
- 프로젝트 안에서 마음대로 불러 쓸 수 있는 오픈 마인드 변수, 함수
 __이름: private
- 클래스 밖을 나가면 아무도 못부르는 변수

웹개발
- 프론트엔드
- html: 웹 개발 제일 바깥 껍데기
- css: html을 꾸며주는 친구
- javascript(js): html & css를 제어하는 친구

튜플: tuple
- 값이 변경(생성, 삭제, 수정)이 되지 않는 (파이썬의)리스트
- ex) 회원의 주민등록번호
- [리스트], (튜플)

** 위워크 **

List, Stack, Queue -> 선형적 linear, 1:1 관계

트리: Tree
- 계층구조( 1(부모): N(자식)관계)
- 비선형적
- composed of node(root, parent, child), line
- 최대 2 child node == binary tree(이진트리)
- 포화 이진트리(Complete Binary Tree)는 자식이 있을거면 한 층이 다같이 있거나 아예 없음.
= 완벽한 세모

차세대, 고도화 프로젝트
- 차세대: 1.0 -> 2.0
- 고도화: 1.0 -> 1.1 

힙: Heap (무더기) -> 트리 업그레이드 버전
- child node가 parent node보다 클 경우 자리를 바꿈

힙의 기능
- Add
- 1) Tree와 동일하게 노드를 끝자리에 추가
- 2) while 부모 노드 있는지 확인
-       있으면,
-          if 부모 노드 값보다 새 노드 값이 더 크면
-              자리 바꿈
-          else:
-               break
-       없으면, break
- -> Pseudo code: 일반 언어와 프로그래밍 언어를 섞어 만든 코드
- 최대 힙의 delete
- 1) 루트 노드와 젤 끝 노드를 바꿔요
- 2) Tree처럼 젤 끝 노드를 delete
- Pseudo code: 
-     while 자식 노드가 있다
-       자식 노드들 < 타겟 노드
-           break
-       자식 노드들 > 타겟 노드
-           큰 노드와 자리 바꿔요
- 3) 자연스럽게 내림차순으로 정렬됨


상속 (Inheritance) - > only for 객체지향언어
: 자식 클래스가 부모 클래스에게 뭔가를 받을 때

메소드 오버라이딩(method overriding)
- 부모 클래스에게 상속받은 메소드를 자식 클래스가 입맛에 맞게 바꿔 쓸 수가 
