<template>
  <div>
    <div><h3>make Room</h3></div>
    <div>
        <label for="">방 이름: </label>
        <input type="text" placeholder="방 제목" value='this.data'>
        <br>
        <label for=""> 인원수: </label>
        <input type="number" placeholder="인원 제한" min="0" max="100" v-model="data.max_head_counts">
        <br>
        <label for="">판 수: </label>
        <input type="number" placeholder="몇판"  v-model="data.problem">
        <br>
        <!-- <label for="">비밀방?</label>
        <input type="checkbox" @click="togglePassword()" v-model="data.is_locked"> -->
        <br>
        <input type="password" v-model="data.room_password">
        <br>
        <button @click="roomMaking">방 만들기</button>
    </div>
  </div>
</template>

<script>
import { reactive, ref } from '@vue/reactivity'
import axios from 'axios'
import { useRouter } from 'vue-router'
export default {
  name: 'makeRoom',


  setup() {

    const data = reactive({
      room_number: "",
      room_password: "",
      problem: "",
      max_head_counts: "",
      is_locked: "",
      is_started: "",
    })
    console.log('data', data)
    const router = useRouter()
    const secret = ref(false)
    // const isShow = props.isShow
    const togglePassword = () => {
      data.is_locked.value = !data.is_locked.value
    }
    const roomMaking = () => {
      console.log('data', data)
      axios({
        method: 'POST',
        url: 'http://localhost:8000/paint_game/make_room/',
        data:{
          room_owner: localStorage.user_name,
          room_number: data.room_number,
          room_password: data.room_password,
          problem: data.problem,
          max_head_counts: data.max_head_counts,
          is_locked: data.is_locked,
          is_started: false,
        }

        // 보류 socket

      }).then((res)=>{
        // 방번호로 보내기
        // router.push('')
      }).catch((err)=>{
        console.log("방만들기 실패")
        console.log(err)
      })
    }

    return {
      data,
      secret,
      togglePassword,
      roomMaking

    }
  }


}
</script>

<style>

</style>
