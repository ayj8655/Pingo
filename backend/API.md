# Backend APIs

! 웹소켓과 관련된 실시간 통신이 필요한 부분은 일단 생략함... 어떻게 하는지 몰라....

* 임시 로그인

		POST: accounts/signup
* 방 목록 받아오기
		
		GET: paint_game/room_list
* 방 만들기

		POST: paint_game/make_room
* 방 입장하기
		
		POST: paint_game/enter_room
* 방 참여인원 리스트 받아오기

		GET: paint_game/room_member/{room_id}
* 게임 시작하기

		PUT: paint_game/start_game/{room_id}
* 제시어 받아오기

		GET: paint_game/word/{room_id}
* 그림 보내서 점수 받아오기

		POST: paint_game/scoring - db에 게임 참가자 테이블에 score 칼럼 넣는게 좋을지도
* 게임 참가자 순위 받아오기

		GET: paint_game/ranking
* 전체 랭킹 받아오기

		GET: paint_game/ranking	 
