<template>

  <button id="yellow-button" @click="start">start</button>

</template>

<script>
import {onMounted, ref} from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
export default {

  methods: {
    start(){
      // const router = userRouter()
      console.log(this.$route.params)
      const room_id = this.$route.params
      this.$router.push({name:'play', params: {room_id: room_id }})
    }
  }
  // setup() {
  //   const router = useRouter()
  //   const start = () => {
  //     const room_id = this.$route.params.room_id
  //     console.log(room_id)
  //     )
  //   }

  //   return {
  //     start
  //   }
  // }
}
</script>

<style>

</style>
