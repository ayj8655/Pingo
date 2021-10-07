<template >
  <div class="ai-back">
    <div class="top-box">
      <button id="yellow-button" @click="start" v-if="is_owner && !isStarted">start</button>

      <div class="link-box" v-if="!isStarted">
        <button id="small-yellow-button" v-if="!isInviting" @click="inviteButtonActivate">초대하기</button>
        <input  type="text" id="link" v-model="urlLink" v-if="isInviting">
        <button id="small-yellow-button" @click="inviteLink" v-if="isInviting">링크복사</button>
        <button id="small-yellow-button" @click="toLobby" >로비로</button>
        <div id="room-audio">
          <!-- 경로가 안잡혀서 여기로 둠 -->
          <audio controls autoplay loop src="/Forest-Trekking.m4a" type="audio.m4a" style="width: 12rem !important; height: 2rem;">
            <source >
          </audio>
        </div>
    </div>
    <div class="play-box">
      <div class="room-left">
        <p>회원</p>
        <div v-for="roomUser in roomUserList" :key='roomUser.user_id'>
          <div class="a-member" >{{roomUser.user_name}}</div>
        </div>

      </div>

      <div class="room-center" v-if="isStarted">
        <playRoom @to-room="toRoom" @leaveRoom="leaveRoom"/>
      </div>

      <div class="room-right">
        <chating :messageObjs="messageObjs"/>
      </div>
    </div>
  </div>
    <section>

      <Modal :isShow='isShow' @switchModal='switchModal'>
        <template v-slot:header>
          </template>
          <template v-slot:body>
            <div v-if="!isLocked" class="lock-room-box">
              <div id="lock-room-box" >
                <h1 style="font-size:3rem; color:#3883BC; " >Pingo!</h1>
                <input class="lock-input" type="text" name="" id="" placeholder="ID" v-model="invitedUser">
                <button id="blue-button" @click="login">login</button>
              </div>
            </div>

            <div v-if="isLocked" class="lock-room-box">
              <div id="lock-room-box">
                <img style="height:250px; width: 300px; margin-top:30px" src="/lock2.png" alt="lock">
                <input class="lock-input" type="text" v-model="invitedPassword">
                <button id="blue-button" @click="inputPassword">비번입력</button>
              </div>

            </div>

          </template>
          <template v-slot:footer>

          </template>
      </Modal>
    </section>
  </div>
</template>

<script>
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
// import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'
import chating from '../components/room/chating.vue'
import playRoom from '@/components/room/playRoom.vue'
import axios from 'axios'
import { useStore } from 'vuex'
import { domain } from '@/domain.js'

import Modal from '../components/Modal.vue'
export default {
  components: { chating, playRoom, Modal },
  props: {
    password: {
      type: String
    }
  },
  setup (props) {
    const store = useStore()
    const route = useRoute()
    const router = useRouter()
    const roomSocket = computed(() => store.state.roomSocket)
    localStorage.setItem('room_id', route.params.room_id)
    const roomUserList = ref([])
    const isStarted = ref(false)
    const isLocked = ref(false)
    const isShow = ref(false)
    const isInviting = ref(false)
    const invitedUser = ref('')
    const invitedPassword = ref('')
    const messageObjs = ref([])
    const is_owner = computed(() => store.state.roomOwner.is_owner)
    var max_head = 0
    var now_head = 0
    // const urlLink = 'http://localhost:8000/room/' + localStorage.getItem('room_id')
    const urlLink = 'http://j5b307.p.ssafy.io' + '/room/' + localStorage.getItem('room_id')
    const room_id = localStorage.getItem('room_id')
    let m = null
    let l = null
    let p = null
    let s = null

    const inviteLink = () => {
      var obj = document.getElementById('link')
      obj.select() // 인풋 컨트롤의 내용 전체 선택
      document.execCommand('copy') // 복사
      obj.setSelectionRange(0, 0)
      alert('클립보드에 링크가 복사되었습니다.')
      isInviting.value = !isInviting.value
    }
    const inviteButtonActivate = () => {
      isInviting.value = !isInviting.value
    }

    const toLobby = () => {
      if (is_owner.value) {
        store.dispatch('setRoomOwner', { is_owner: false, name: '' })
      }
      router.push('/lobby')
    }

    const getRoomAndLobbyUsers = () => {
      if (roomSocket.value.readyState === 1) {
        store.dispatch('roomSend',
          {
            space: 'room',
            req: 'getRoomUsers'
          }
        )
      } else {
      }

      if (store.state.lobbySocket.readyState === 1) {
        store.dispatch('lobbySend',
          {
            space: 'lobby',
            req: 'getLobbyUsers'
          }
        )
      }
    }
    const enterRoom = () => {
      // axios.post('http://localhost:8000/paint_game/enter_room/', {
      axios.post(domain + '/paint_game/enter_room/', {
        user_id: localStorage.getItem('user_id'),
        room_id: route.params.room_id,
        room_password: props.password
      })
        .then((res) => {
          getRoomAndLobbyUsers()
        })
    }

    const enterRoom2 = () => {
      console.log(route.params)
      // axios.post('http://localhost:8000/paint_game/enter_room/', {
      axios.post(domain + '/paint_game/enter_room/', {
        user_id: localStorage.getItem('user_id'),
        room_id: route.params.room_id,
        room_password: invitedPassword.value
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
          isShow.value = !isShow.value
        })
    }

    const leaveRoom = () => {
      axios.delete(domain + '/paint_game/leave_room/', {
        data: {
          user_id: localStorage.getItem('user_id'),
          room_id: localStorage.getItem('room_id')
        }
      })
        .then((res) => {
          getRoomAndLobbyUsers()
          roomSocket.value.close()
          localStorage.removeItem('room_id')
          if (is_owner.value) {
            store.dispatch('setRoomOwner', { is_owner: false, name: '' })
            store.dispatch('lobbySend',
              {
                space: 'lobby',
                req: 'getRoomList'
              }
            )
          }
        })
        .catch((err) => {
          console.dir(err)
        })
    }

    const invited = () => {
      const user_id = localStorage.getItem('user_id')
      if (user_id === null) {
        alert('로그인이 필요합니다.')
        isShow.value = !isShow.value
      } else {
        enterRoom()
      }
    }

    const inputPassword = () => {
      // console.log(invitedPassword.value, p, 'invite & props')
      // console.log(props)
      if (invitedPassword.value === p) {
        enterRoom2()
      } else {
        alert('비밀번호가 틀립니다.')
      }
    }

    const start = () => {
      store.dispatch('roomSend', {
        space: 'room',
        req: 'gameStart',
        parameter: localStorage.getItem('user_name')
      })
    }

    const login = () => {
      const username = invitedUser._value
      // console.log('invitedUser', invitedUser)
      // console.log(username)

      if (username === '') {
        alert('아이디를 입력해주세요')
        return
      }
      axios({
        method: 'POST',
        // url: 'http://J5B307.p.ssafy.io:8000/accounts/check_duplication/',
        url: domain + '/accounts/check_duplication/',
        data: {
          user_name: username
        }
      })
        .then((res) => {
          // console.log('res2', res)
          if (res.data.duplicate === 'fail') {
            alert('중복된 아이디입니다')
            return
          }
          return axios({
            method: 'POST',
            // url: 'http://J5B307.p.ssafy.io:8000/accounts/signup/',
            url: domain + '/accounts/signup/',
            data: {
              user_name: username
            }
          })
        })
        .then((res) => {
          // console.log('login (67line)', res.data)
          localStorage.setItem('user_name', res.data.user_name)
          localStorage.setItem('user_id', res.data.user_id)
          return axios({
            method: 'GET',
            url: domain + '/paint_game/room_info/' + room_id
          })
        })
        .then((res) => {
          s = res.data.is_started
          l = res.data.is_locked
          p = res.data.room_password
          // console.log(res.data)
          m = res.data.max_head_counts
          return axios({
            method: 'GET',
            url: domain + '/paint_game/room_member/' + room_id + '/'
          })
        })
        .then((res) => {
          const n = res.data.length

          if (s) {
            alert('게임이 진행중입니다')
            router.push('/lobby')
          } else if (l) {
            isLocked.value = !isLocked.value
            // console.log(isLocked.value)
          } else if (m > n) {
            enterRoom()
            isShow.value = !isShow.value
          } else {
            alert('정원이 가득 찼습니다')
            router.push('/lobby')
          }
        })
        .catch((err) => {
          console.dir(err)
        })
    }

    const toRoom = () => {
      isStarted.value = false
    }

    if (roomSocket.value.url === undefined || roomSocket.value.readyState === 3) {
      store.commit('roomSocketConnect', route.params.room_id)
    }
    roomSocket.value.onopen = () => {
      getRoomAndLobbyUsers()
    }
    roomSocket.value.onclose = (e) => {
      // leaveRoom()
      router.push({ name: 'lobby' })
      localStorage.removeItem('room_id')
    }
    roomSocket.value.onmessage = (e) => {
      const data = JSON.parse(e.data)
      // console.log('room 125line', data)
      if (data.res === 'gameStart') {
        if (data.value.error === undefined) {
          store.commit('setKeywords', data.value)
          isStarted.value = !isStarted.value
        } else {
          console.log(data.value.error)
        }
      } else if (data.res === 'getRoomUsers') {
        roomUserList.value = data.value.map(e => e.user)
      } else if (data.res === 'chat') {
        messageObjs.value.push(data.value)
      }
    }

    onMounted(() => {
      invited()
    })

    onBeforeUnmount(() => {
      if (is_owner.value) {
        // 방장이 로비로 갈 경우 방폭
        store.dispatch('roomSend',
          {
            space: 'room',
            req: 'roomOwnerQuit'
          }
        )
      }
      leaveRoom()
    })

    window.onbeforeunload = () => {
      leaveRoom()
    }

    return {
      start,
      isStarted,
      invited,
      isShow,
      login,
      invitedUser,
      urlLink,
      inviteLink,
      isLocked,
      invitedPassword,
      inputPassword,
      roomUserList,
      toRoom,
      leaveRoom,
      isInviting,
      inviteButtonActivate,
      is_owner,
      messageObjs,
      toLobby

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
.top-box{
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  margin: auto;
  align-items: center;
}

.link-box{
  display: flex;
  align-items: center;
}

#link{
  height: 2rem;
  width: 11rem;
  border-radius: 5px;
  font-size: 0.7rem;
  border: none;
}

.draw{
  height: 800px;
  width: 800px;
  padding: auto;
  /* flex-grow: 2; */
  /* 캔버스 크기가 고정되어 안커짐 */
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
  align-items: flex-start;
  width: 1200px;
  height: 800px;
  margin: auto;
  flex-shrink: 2;
}

.room-left{
display: flex;
flex-direction: column;
height: 400px;
width: 200px;
background-color: white;
border-radius: 10px;
margin: 1rem;
margin-top: 7rem;
flex-shrink: 1;
overflow: scroll;
/* padding-top: 3rem; */
min-height: 300px;
}

.room-center{
height: 900px;
flex-basis: 500px;
width: 600px;
margin: 0;
}

.room-right{
display: flex;
flex-direction: column;
flex-shrink: 1;
height: 400px;
width: 400px;
flex-basis: 300px;
background-color: white;
border-radius: 10px;
margin: 1rem;
margin-top: 7em;
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
#room-audio{
  display: flex;
  align-items: center;
  margin: auto;
  margin: 10px;

}

.a-member{
  margin-top: 3px;
}
</style>
