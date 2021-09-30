<template>
    <div id="back" class="lobby-frame">
      <!-- <div> <h3>Lobby</h3></div> -->
      <section class="lobby-left-box">
        <section>
          <button id="yellow-button" @click="createRoom">방만들기</button>
        </section>
        <section class="lobby-left">


        </section>

      </section>

      <section class="lobby-right">
        <!-- <h1>오른쪽</h1> -->
        <!-- <h1>{{roomList}}</h1> -->
        <ul>
          <roomItem v-for="room in roomList[0]"
          :key='room.room_id'
          :room='room'
          @click="moveRoom(room)"/>


        </ul>



      </section>


      <section>
      <Modal :isShow='isShow' @switchModal='switchModal'>
        <template v-slot:header>
        </template>

        <template v-slot:body>
          <div v-if="roomMaking">
            <h1>방만들기</h1>
            <makeRoom @refreshRoom="refreshRoom" />
          </div>
          <div v-if="password && isLocked">
            <h1>비번입력</h1>
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
import { computed, onMounted, onBeforeMount, ref, reactive } from 'vue'
import makeRoom from '../components/lobby/makeRoom.vue'
import lockRoom from '../components/lobby/lockRoom.vue'
import roomItem from '../components/lobby/roomItem.vue'
import Modal from '@/components/Modal.vue'
import { useRouter } from 'vue-router'
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
    var roomList = ref([])
    const userList = ref([])
    const isShow = ref(false)
    const roomMaking = ref(false)
    const isLocked = ref(false)
    const password = ref(false)
    const switchModal = ()=>{
      isShow.value = !isShow.value
      console.log(roomMaking.value, password.value, isLocked.value)
      if(roomMaking.value === true){roomMaking.value = !roomMaking.value}
      if(password.value === true){password.value = !password.value}
      if(isLocked.value === true){isLocked.value = !password.value}
    }

    onMounted(()=> {
      axios({
        method: 'GET',
        url: 'http://localhost:8000/paint_game/room_list/',

      }).then((res) => {
        console.log(roomList)
        roomList.value.push(res.data)
      }).catch((err) => {
        console.log(err)
      })
    })
    const createRoom = () => {
      isShow.value = !isShow.value
      roomMaking.value = !roomMaking.value
      console.log(isShow)
    }

    const refreshRoom = () => {
      axios({
        method: 'GET',
        url: 'http://localhost:8000/paint_game/room_list/',

      }).then((res) => {
        roomList.push(res)

      }).catch((err) => {
        console.log(err)
      })
    }

    computed(() => {
      axios({
        method: 'GET',
        url: 'http://localhost:8000/paint_game/room_list/',

      }).then((res) => {
        roomList.push(res)

      }).catch((err) => {
        console.log(err)
      })
    })

    const moveRoom = ((room) => {
      localStorage.setItem('room_id', room.room_id)
      console.log('room', room)
      if(room.is_started === true){
        alert('게임이 진행중일 때는 입장할 수 없습니다.')

      }

      else if(room.is_locked === true){(isLocked.value = true) && (isShow.value = !isShow.value)
      && (password.value = !password.value) }
      else {axios({
        method: 'POST',
        url: "http://localhost:8000/paint_game/enter_room/",
        data: {
          user_id: localStorage.getItem('user_id'),
          room_id: room.room_id
        }
      }).then((res) => {
        console.log(res)
      }).then(
        router.push({name:'room',
                    params: {room_id: room.room_id }})
      )


    }})



    return {
      roomList,
      createRoom,
      isShow,
      isLocked,
      password,
      switchModal,
      userList,
      refreshRoom,
      roomItem,
      moveRoom,
      roomMaking
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

.lobby-left{
  background-color: white;
  max-width: 400px;
  flex-basis: 400px;
  flex: 1 1 100%;
  box-sizing: border-box;
  border-radius: 5px;
  margin: 10px;


}

.lobby-right{
  background-color: white;

  flex-basis: 100px;
  flex: 1 1 100%;
  box-sizing: border-box;
  border-radius: 5px;
  margin: 10px;
  display: flex;
  justify-content: space-between;
}
</style>
