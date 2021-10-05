<template >
  <div class="ai-back">
    <button id="yellow-button" @click="start" v-if="!isStarted">start</button>
    <input type="text" id="link" v-model="urlLink">
    <button @click="inviteLink">초대링크</button>
    <div class="play-box">
      <div class="room-left">
        <p>회원</p>
      </div>
      <div class="room-center" v-if="isStarted">
        <playRoom/>
      </div>
      <!-- <div id="timerBox">
        <p>{{settime.value}}</p>
      </div> -->
      <div class="room-right">
        <p>채팅</p>
      </div>
    </div>
    <section >
      <Modal :isShow='isShow' @switchModal='switchModal'>
        <template v-slot:header>
          </template>
          <template v-slot:body>
            <div>
              <input type="text" name="" id="" v-model="invitedUser">
              <button @click="login">login</button>
            </div>

          </template>
          <template v-slot:footer>
          </template>
      </Modal>
    </section>
    <!-- <div :class="['chat-only', isStarted && 'chat-and-draw']" >
      그림판
      <div class="draw" v-if="isStarted">
        <draw/>
      </div>
      <div :class="['big-chat', isStarted && 'chat']" >
        <chating />
      </div>
    </div>-->
  </div>
  <!-- 시작버튼(누르면 없어지고 제시어 등장) -->
</template>

<script>
import { onBeforeUnmount, onMounted, reactive, ref } from 'vue'
// import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'
import chating from '../components/room/chating.vue'
import playRoom from '@/components/room/playRoom.vue'
import axios from 'axios'
import { useStore } from 'vuex'
import Modal from '../components/Modal.vue'
export default {
  components: { chating, playRoom, Modal },
  setup () {
    const route = useRoute()
    const router = useRouter()
    const store = useStore()
    localStorage.setItem('room_id', route.params.room_id)
    const isStarted = ref(false)
    const isShow = ref(false)
    const invitedUser = ref('')
    var max_head = 0
    var now_head = 0
    const urlLink = 'http://localhost:8000/paint_game/enter_room/' + localStorage.getItem('room_id')

    const inviteLink =() => {
      var obj = document.getElementById("link");
      obj.select(); //인풋 컨트롤의 내용 전체 선택
      document.execCommand("copy"); //복사
      obj.setSelectionRange(0, 0);



    }
    const enterRoom = () => {
      axios.post('http://localhost:8000/paint_game/enter_room/', {
        user_id: localStorage.getItem('user_id'),
        room_id: route.params.room_id
      })
        .then((res) => {
          if (store.state.lobbySocket.readyState === 1) {
            store.dispatch('lobbySend',
              {
                space: 'lobby',
                req: 'getUserList'
              }
            )
          }
        })
    }

    const leaveRoom = () => {
      axios.delete('/paint_game/leave_room/', {
        data: {
          user_id: localStorage.getItem('user_id'),
          room_id: localStorage.getItem('room_id')
        }
      })
        .then((res) => {
          console.log(res)
          localStorage.removeItem('room_id')
          store.dispatch('lobbySend',
            {
              space: 'lobby',
              req: 'getUserList'
            }
          )
        })
        .catch((err) => {
          console.dir(err)
        })
    }
    const invited = () => {
      const user_id = localStorage.getItem('user_id')
      if(user_id===null){
        alert(isShow.value)
        isShow.value = !isShow.value
      }else{enterRoom()}

    }


    const start = () => {
      isStarted.value = !isStarted.value
      store.dispatch('roomSend', {
        space: 'room',
        req: 'gameStart'
      })
    }

    // const settime = ref(1500)
    // const sec = ref('')

    // const timer = setInterval(function () {
    //   sec.value = parseInt(settime.value / 100)

    //   document.getElementById('timerBox').innerHTML = sec.value + '초'
    //   settime.value -= 10

    //   if (settime.value <= 0) {
    //     clearInterval(timer)
    //     document.getElementById('timerBox').innerHTML = '종료'
    //   }
    // }, 100)
    store.commit('roomSocketConnect', route.params.room_id)
    store.state.roomSocket.onmessage = (e) => {
      const data = JSON.parse(e.data)
      console.log('room 43line', data)
    }
    const room_id = localStorage.getItem('room_id')
    const roomLimit = () => {
      axios({
        method: 'GET',
        url: '/paint_game/room_info/' + room_id
      }).then((res) => {
        console.log('roominfo', res.data.max_head_counts)
        const m = res.data.max_head_counts
        store.commit('FULL_LIMIT' , m)
      })
        return
    }
    const fullRoom = () => {
      axios({
        method: 'GET',
        url: '/paint_game/room_member/' + room_id + '/'
      }).then((res) => {
        console.log('res3', res)
        console.log('length', res.data.length)
        const n = res.data.length
        store.commit('NOW_LIMIT', n)
      })
        return
    }


    const login = () => {
      const username = invitedUser._value
      console.log('invitedUser', invitedUser)
      console.log(username)
      if (username === '') {
        alert('아이디를 입력해주세요')
        return
      }
      axios({
        method: 'POST',
        // url: 'http://J5B307.p.ssafy.io:8000/accounts/check_duplication/',
        url: '/accounts/check_duplication/',
        data: {
          user_name: username
        }
      })
        .then((res) => {
          console.log('res2', res)
          if (res.data.duplicate === 'fail') {
            alert('중복된 아이디입니다')
            return
          }
          return axios({
            method: 'POST',
            // url: 'http://J5B307.p.ssafy.io:8000/accounts/signup/',
            url: '/accounts/signup/',
            data: {
              user_name: username
            }
          })
        })
        .then((res) => {
          console.log('login (67line)', res.data)
          localStorage.setItem('user_name', res.data.user_name)
          localStorage.setItem('user_id', res.data.user_id)
          var number1 = roomLimit()
          var number2 = fullRoom()


        }).then((res) => {
        // console.log('num1, num2' , number1, number2)
        console.log('limit and full',store.state.maxhead, store.state.nowhead)
        if(store.state.maxhead > store.state.nowhead){enterRoom()}
        else{
          // router.push('/lobby')
          alert()
          }

          isShow.value = !isShow.value
        })
        .catch((err) => {
          console.dir(err)
        })
    }



    onMounted(() => {
      invited()



    })
    onBeforeUnmount(() => {
      leaveRoom()
    })

    window.onbeforeunload = () => {
      leaveRoom()
    }




    return {
      start,
      isStarted,
      // timer,
      // setInterval,
      // settime,
      invited,
      isShow,
      login,
      invitedUser,
      fullRoom,
      roomLimit,
      urlLink,
      inviteLink,
      max_head,
      now_head,

    }
  }
}
</script>

<style>
.ai-back{
  /* background-image: url(/image1.jfif) !important ; */
  background-image: url(/ai.jpg) !important ;
  height: 100%;
  width: 100%;
  background-repeat : repeat;
  background-size : cover;
  background-position: center;
}

.chat-only{
  display: block;

}
.chat-and-draw{
  display: flex;
  justify-content: center;
  flex-direction: row;
}
.draw{
  height: 800px;
  width: 800px;
  padding: auto;
  /* flex-grow: 2; */
  /* 캔버스 크기가 고정되어 안커짐 */
}
.big-chat{
  height: 800px;
  width: 500px;
  background-color: #fff;
  border-radius: 15px;
  margin: auto;
}
.chat{
  height: 600px;
  width: 300px;
  background-color: #fff;
  border-radius: 15px;
  margin: 0;
  /* flex-grow: 1; */
}
.play-box{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 1300px;
  height: 100%;
  margin: auto;
}

.room-left{
height: 670px;
width: 300px;
background-color: white;
border-radius: 5px;
margin: 3rem;
/* padding-top: 3rem; */

}

.room-center{
height: 900px;
flex-basis: 900px;
width: 700px;
}

.room-right{
height: 670px;
width: 300px;
background-color: white;
border-radius: 5px;
margin: 3rem;

}


.word{
  height: 3rem;
  width: 18rem;
  border-radius: 0.5rem;
  border: none;
  font-size: 1.3rem;
  background: #FFF9BA;
  color: #3883BC;
  font-weight: bold;
  margin: 10px;
  align-content: center;
}
.word p {
  font-size: 1.4rem !important;
  margin: 0.6rem;
}
</style>
