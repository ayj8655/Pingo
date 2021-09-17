<template>
  <div>
    <div><h3>make Room</h3></div>
    <div>
        <label for="">방 이름: </label>
        <input type="text" placeholder="방 제목" value='this.data'>
        <br>
        <label for=""> 인원수: </label>
        <input type="number" placeholder="인원 제한" value="5" min="0" max="100">
        <br>
        <label for="">판 수: </label>
        <input type="number" placeholder="몇판" value="6">
        <br>
        <label for="">비밀방?</label>
        <input type="checkbox" @click="togglePassword()">
        <br>
        <input type="password">
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
      name: '',
      number: '',
    })
    const router = useRouter()
    const secret = ref(false)
    // const isShow = props.isShow
    const togglePassword = () => {
      this.secret = !this.secret
    }
    const roomMaking = (data) => {
      axios({
        method: "POST",
        url: "",
        data: data
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
