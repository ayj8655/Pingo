<template>
    <div>
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
    const isShow = ref(true)
    const switchModal = ()=>{
      isShow.value = !isShow.value
    }
    // onMounted(() => {
    //   axios.get({
    //     url: ''
    //   }).then(res => {
    //     console.log(res)
    //   })
    // })
    const createRoom = () => {
      isShow.value = !isShow.value
      console.log(isShow)
      // axios.post({
      //   url: ''
      //   // 보류 socket
      // })
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
