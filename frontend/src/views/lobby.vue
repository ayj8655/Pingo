<template>
    <div id="back" class="lobby-frame">
      <!-- <div> <h3>Lobby</h3></div> -->
      <section class="lobby-left-box">
        <section>
          <button id="yellow-button" @click="createRoom">방만들기</button>
        </section>
        <section>
          <button id="blue-button" @click="tutorial" v-if="!isTutorial">튜토리얼</button>
          <button id="blue-button" @click="tutorial" v-if="isTutorial">방목록으로</button>
        </section>
        <div>
          <!-- <audio controls autoplay loop src="/victory.m4a" type="audio.m4a" style="width: 18rem">
            <source >
          </audio> -->
        </div>
        <section class="lobby-left">
          <div v-for="user in userList" :key="user.user_id">
            <div class="nickname">
              <i class="far fa-smile-wink"></i>
              <p>{{user.user_name}}</p>
            </div>
          </div>
        </section>

      </section>
      <section class="lobby-right">
        <div class="iframe-box" v-show="isTutorial">
          <!-- youtube 링크에서 'watch?v=' 부분을 'embed/'로 바꾸면 x-frame option 없이 불러올 수 있다 -->
          <iframe src="https://www.youtube.com/embed/X8v1GWzZYJ4" type="text/html" width="500px" height="300px" frameborder="0"></iframe>
        </div>
        <div v-show="!isTutorial">
          <ul>
            <roomItem v-for="room in roomList"
            :key='room.room_id'
            :room='room'
            @click="moveRoom(room)"/>
          </ul>
        </div>
      </section>
      <section>
        <Modal :isShow='isShow' @switchModal='switchModal'>
          <template v-slot:header>
          </template>
          <template v-slot:body>
            <div v-if="roomMaking">
              <makeRoom/>
            </div>
            <div v-if="password && isLocked">

              <lockRoom />
            </div>
          </template>
          <template v-slot:footer>
          </template>
        </Modal>
      </section>
    </div>
</template>

<script>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import makeRoom from '../components/lobby/makeRoom.vue'
import lockRoom from '../components/lobby/lockRoom.vue'
import roomItem from '../components/lobby/roomItem.vue'
import Modal from '@/components/Modal.vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { domain } from '@/domain.js'
export default {
  name: 'Lobby',
  components: {
    makeRoom,
    Modal,
    roomItem,
    lockRoom

  },
  setup () {
    const router = useRouter()
    const store = useStore()
    const roomList = ref([])
    const userList = ref([])
    const isShow = ref(false)
    const roomMaking = ref(false)
    const isLocked = ref(false)
    const password = ref(false)
    const lobbySocket = store.state.lobbySocket
    const isTutorial = ref(false)
    const videoUrl = ref('https://www.youtube.com/')
    // x-frame origin 해결하기

    const getLobbyUsers = () => {
      if (lobbySocket.readyState === 1) {
        store.dispatch('lobbySend',
          {
            space: 'lobby',
            req: 'getLobbyUsers'
          }
        )
      }
    }

    const switchModal = () => {
      isShow.value = !isShow.value
      console.log(roomMaking.value, password.value, isLocked.value)
      if (roomMaking.value === true) { roomMaking.value = !roomMaking.value }
      if (password.value === true) { password.value = !password.value }
      if (isLocked.value === true) { isLocked.value = !password.value }
    }

    const createRoom = () => {
      isShow.value = !isShow.value
      roomMaking.value = !roomMaking.value
    }
    const tutorial = () => {
      isTutorial.value = !isTutorial.value
    }

    const moveRoom = (room) => {
      store.dispatch('resetGame')
      localStorage.setItem('room_id', room.room_id)
      axios({
        method: 'GET',
        url: domain + '/paint_game/room_info/' + room.room_id
      })
      .then((res) => {
        console.log('move data',res.data)
        localStorage.setItem('is_locked', res.data.is_locked)
        localStorage.setItem('is_started', res.data.is_started)
        localStorage.setItem('max_head_counts', res.data.max_head_counts)
        return axios({
          method: 'GET',
          url: domain + '/paint_game/room_headcount/' + room.room_id
        })
        .then((res) => {
          console.log('현재원', res.data.headcount)
          const max = localStorage.getItem('max_head_counts')
          console.log('정원', max)
          if(res.data.headcount >= max){
            alert('정원이 가득 찼습니다.')
          }
          else if (room.is_started === true) {
            alert('게임이 진행중일 때는 입장할 수 없습니다.')
          }
          else if (room.is_locked === true) {
            (isLocked.value = true) && (isShow.value = !isShow.value) && (password.value = !password.value)
          }
          else {
            router.push({ name: 'room', params: { room_id: room.room_id } })
          }


        })
      })

    }

    lobbySocket.onmessage = (e) => {
      const data = JSON.parse(e.data)
      // console.log('lobby 131line', data)
      if (data.res === 'getLobbyUsers') {
        userList.value = data.value
      } else if (data.res === 'getRoomList') {
        roomList.value = data.value
      }
    }
    lobbySocket.onopen = () => {
      getLobbyUsers()
    }
    lobbySocket.onclose = () => {
      console.log('로비소켓 끊김')
    }
    onMounted(() => {
      getLobbyUsers()
      axios({
        method: 'GET',
        // url: '/paint_game/room_list/'
        url: domain + '/paint_game/room_list/'
      }).then((res) => {
        roomList.value = res.data
      }).catch((err) => {
        console.dir(err)
      })
    })
    return {
      roomList,
      createRoom,
      isShow,
      isLocked,
      password,
      switchModal,
      userList,
      roomItem,
      moveRoom,
      roomMaking,
      videoUrl,
      isTutorial,
      tutorial
    }
  }
}
</script>

<style scoped>
.lobby-frame {
  box-sizing: border-box;
    min-height: 600px;
    min-width: 900px;
    flex-grow: 1;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 35px 40px;
    padding-top: 15px !important;
}

.lobby-left-box{

  display: flex;
  flex-direction: column;
}

#audio-box{
  width: ;
}

.iframe-box {
  display: flex;
  margin: auto;

}

.lobby-left{
  overflow: scroll;
  background-color: white;
  max-width: 400px;
  flex-basis: 400px;
  flex: 1 1 100%;
  box-sizing: border-box;
  border-radius: 5px;
  margin: 10px;
  min-height: 650px;
}

.lobby-right{
  overflow: scroll;
  background-color: white;
  flex-basis: 20rem;
  flex: 1 1 100%;
  box-sizing: border-box;
  border-radius: 5px;
  margin: 10px;
  display: flex;
  justify-content: space-between;
  height: 100%;
}

.nickname{
  display: flex;
  font-display: row;
  align-items: center;
  height: 2rem;

}
.nickname i{
  margin-left: 2rem;
  margin-right: 0.5rem;
}
</style>
