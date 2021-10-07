<template>
  <div id='back'>
      <div class="login-box">
        <p>AI와 그림 퀴즈 맞춰요</p>
        <input class="login-input" type="text" placeholder="Temporary Nickname" v-model="credentials.user_name" @keydown.enter="goToLobby">
        <br>
        <button id="blue-button" @click="goToLobby">Enter</button>
      </div>
  </div>

</template>

<script>
import axios from 'axios'
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { domain } from '@/domain.js'
export default {
  name: 'login',
  setup () {
    const reg = /^[0-9a-zA-zㄱ-ㅎㅏ-ㅣ가-힣]{3,8}$/
    const router = useRouter()
    const credentials = reactive({
      user_name: ''
    })

    const goToLobby = () => {
      const username = credentials.user_name.trim()
      if (username === '') {
        alert('아이디를 입력해주세요')
        return
      }
      if (!reg.test(username)) {
        alert('특수문자를 제외한 3~8자로 입력하세요')
        return
      }

      axios({
        method: 'POST',
        // url: 'http://J5B307.p.ssafy.io:8000/accounts/check_duplication/',
        // url: '/accounts/check_duplication/',
        url: domain + '/accounts/check_duplication/',
        data: {
          user_name: username
        }
      })
        .then((res) => {
          if (res.data.duplicate === 'fail') {
            alert('중복된 아이디입니다')
            return
          }
          return axios({
            method: 'POST',
            // url: 'http://J5B307.p.ssafy.io:8000/accounts/signup/',
            // url: '/accounts/signup/',
            url: domain + '/accounts/signup/',
            data: {
              user_name: username
            }
          })
        })
        .then((res) => {
          localStorage.setItem('user_name', res.data.user_name)
          localStorage.setItem('user_id', res.data.user_id)
          router.push('/lobby')
        })
        .catch((err) => {
          console.dir(err)
        })
    }
    return {
      goToLobby,
      credentials
    }
  }

}
</script>

<style>

.login-box{
  position: relative;
  top: 20%

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
