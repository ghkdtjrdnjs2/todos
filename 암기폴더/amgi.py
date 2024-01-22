# 뷰 설계 - 웹스토리보드
# 
# 모델설계 - 데이터의 구조 (데이터베이스) CRUD담당
# 
# 모델과 뷰를 연결해주는것 - controller 주소와 연관됨
# 
# controller - 주소제공, 뷰와 모델의 연결
# 
# MVC - Model View Controller 
# guestbook=[]
# 
# MVVM - Model View ViewModel
# 
# 사용자의 요청에 응답하는 서버 개발 : 백엔드 + 화면
# 프레임워크 - 필요한 기능들을 부품화해서 조립하는 방식
# 서버개발할 때 프레임워크 기반으로 개발
# templates - html,         static - css, js
# get은 querystring방식으로 서버에 값을 전달한다

# get       주소창 127.0.0.1:5000/name?irum=spring&nai=20 -> 보인다 querystring
# post      주소창 127.0.0.1:5000/name(   숨겨져있다   )
# 이둘의 형식은 urlencoded 형식이고 get은 데이터가 주소창에 나타나는거고 post는 데이터가 보이지않을뿐이다

# render-template -화면츌력 get
# redirect - 주소이동 post
