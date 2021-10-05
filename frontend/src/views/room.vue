<template >
  <div class="ai-back">
    <button id="yellow-button" @click="start" v-if="!isStarted">start</button>
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
import { onBeforeUnmount, onMounted, ref } from 'vue'
// import axios from 'axios'
import { useRoute } from 'vue-router'
import chating from '../components/room/chating.vue'
import playRoom from '@/components/room/playRoom.vue'
import axios from 'axios'
import { useStore } from 'vuex'
export default {
  components: { chating, playRoom },
  setup () {
    const route = useRoute()
    const store = useStore()
    localStorage.setItem('room_id', route.params.room_id)
    const isStarted = ref(false)
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
    const start = () => {
      isStarted.value = !isStarted.value
      store.dispatch('roomSend', {
        space: 'room',
        req: 'gameStart'
      })
    }

    const settime = ref(1500)
    const sec = ref('')

    const timer = setInterval(function () {
      sec.value = parseInt(settime.value / 100)

      document.getElementById('timerBox').innerHTML = sec.value + '초'
      settime.value -= 10

      if (settime.value <= 0) {
        clearInterval(timer)
        document.getElementById('timerBox').innerHTML = '종료'
      }
    }, 100)
    store.commit('roomSocketConnect', route.params.room_id)
    store.state.roomSocket.onmessage = (e) => {
      const data = JSON.parse(e.data)
      console.log('room 43line', data)
    }

    onMounted(() => {
      enterRoom()
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
      timer,
      setInterval,
      settime
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
