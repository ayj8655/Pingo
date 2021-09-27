<template>
    <div id="back">
      <div> <h3>Lobby</h3></div>
      <button @click="createRoom">방만들기</button>
      <section>
      <Modal :isShow='isShow' @switchModal='switchModal'>
        <template v-slot:header>
        </template>

        <template v-slot:body>
          <h1>방만들기</h1>
          <makeRoom/>
        </template>
        <template v-slot:footer>
        </template>
      </Modal>
      <h1>{{roomList}}</h1>

      </section>

    </div>
</template>

<script>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import makeRoom from '../components/makeRoom.vue'
import Modal from '@/components/Modal.vue'
export default {
  name: 'Lobby',
  components: {
    makeRoom,
    Modal

  },


  setup () {


    const roomList = []
    const isShow = ref(false)
    const switchModal = ()=>{
      isShow.value = !isShow.value
    }
    onMounted(()=> {
      axios({
        method: 'GET',
        url: 'http://localhost:8000/paint_game/room_list/',

      }).then((res) => {
        roomList.push(res)
      }

      )
    })
    const createRoom = () => {
      isShow.value = !isShow.value
      console.log(isShow)

    }

    return {
      roomList,
      createRoom,
      isShow,
      switchModal
    }
  }
}
</script>

<style>

</style>
