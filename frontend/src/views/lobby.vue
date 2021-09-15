 <template>
    <div>
      <div> <h3>Lobby</h3></div>
      <button @click="createRoom">방만들기</button>
    </div>
</template>

<script>
import axios from 'axios'
import { onMounted } from 'vue'
export default {
  name: 'Lobby',
  components: {

  },
  setup () {
    const roomList = []
    onMounted(() => {
      axios.get({
        url: ''
      }).then(res => {
        console.log(res)
      })
    })
    const creatRoom = () => {
      axios.post({
        url: ''
        // 보류 socket
      })
    }

    return {
      roomList,
      creatRoom
    }
  }
}
</script>

<style>

</style>
