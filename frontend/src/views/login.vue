<template>
  <div id='back'>
      <div class="login-box">
        <p>AI와 그림 퀴즈 맞춰요</p>
          <input class="login-input" type="text" placeholder="Temporary Nickname" v-model="credentials.user_name" @keydown.enter="goToLobby">
          <!-- <button @click="checkDuplication">중복검사</button> -->
          <br>
          <button id="blue-button" @click="goToLobby">Enter</button>
      </div>
  </div>

</template>

<script>
import axios from 'axios'
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
export default {
  name: 'login',
  setup () {
    const router = useRouter()
    const credentials = reactive({
      user_name: ''
    })
    const checkDuplication = () => {
      console.log('아이디 중복 검사')
      // axios({
      //   method: 'POST',
      //   url: 'http://localhost:8000/accounts/check_duplication/',
      //   data: {
      //     user_name: credentials.user_name,
      //   }

      // }).then((res) => {
      //   console.log(res)
      // })
    }
    console.log('credential', credentials.user_name)

    const goToLobby = () => {

      const username = credentials.user_name.trim()
      if ( username === ''){
        alert('아이디를 입력해주세요')
        return
      }


      console.log('아이디 중복 검사')
      axios({
        method: 'POST',
        url: 'http://localhost:8000/accounts/check_duplication/',
        data: {
          user_name: username,
        }
        }).then((res) => {
          console.log(res.data)
          if(res.data.duplicate === 'fail'){
            alert('중복된 아이디입니다')
            return
          }

      axios({
        method: 'POST',
        url: 'http://localhost:8000/accounts/signup/',
        data: {
          user_name: username,
        }
      }).then((res) => {
        console.log('data.data', res.data)
        localStorage.setItem('user_name', res.data.user_name)
        localStorage.setItem('user_id', res.data.user_id)
        router.push('/lobby')
        }).catch((err) => {
          console.log(err)
          alert(err)
          router.push('/login')
        })
      // router.push('lobby')

      }).catch((err) => {
        console.log(err)
        alert(err)
        router.push('/login')
      })

    }
    // 백엔드에 닉네임 중복인지 아닌지 요청보내기

    return {
      goToLobby,
      credentials,
      router,
      checkDuplication
    }
  }

}
</script>

<style>

.login-box{
  position: relative;
  top: 50%

}

.login-box p {
  height: 3rem;
  font-size: 3rem;
  font-weight: bolder;
}

.login-input{

  height: 3rem;
  width: 18rem;
  border-radius: 0.5rem;
  border: none;
  font-size: 1.3rem;
  justify-content: center;
  margin: 0 auto 1.5rem 0;
}
/* .login-button{
  height: 3rem;
  width: 18rem;
  border-radius: 0.5rem;
  border: none;
  font-size: 1.3rem;
} */
</style>
