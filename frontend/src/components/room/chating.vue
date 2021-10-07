<template>
  <div>
    <div v-for="obj in messageObjs" :key="obj.send_time">
      {{obj.user_name}}
      {{obj.message}}
      {{obj.send_time}}
    </div>
    <input v-model="message" type="text" @keydown.enter="sendChatMessage()">
    <input v-model="dd.me" type="text">
  </div>
</template>

<script>
import { reactive, ref } from '@vue/reactivity'
import { useStore } from 'vuex'
export default {
  props: {
    messageObjs: {
      type: Array
    }
  },
  setup () {
    const dd = reactive({
      me: 'zz'
    })
    const store = useStore()
    const message = ref('')
    const username = localStorage.getItem('user_name')
    const sendChatMessage = () => {
      const now0 = new Date()
      const mObj = {
        user_name: username,
        message: message.value,
        send_time: now0.getHours() + ':' + now0.getMinutes()
      }
      store.dispatch('roomSend',
        {
          space: 'room',
          req: 'chat',
          value: mObj
        }
      )
      message.value = ''
    }
    return {
      dd,
      sendChatMessage,
      username,
      message
    }
  }
}
</script>

<style>

</style>
