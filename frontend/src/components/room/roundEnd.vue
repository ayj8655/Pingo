<template>
<div class="score-board">
  <div class="score-box">
    <h2>{{ddd.para}}</h2>
    <h3>{{ddd.author}}</h3>
  </div>
</div>
</template>

<script>
import { ref } from '@vue/reactivity'
export default {
  name: 'roundEnd',
  mounted () {
    clearTimeout()
    // console.log('roundEnd mounted')
    setTimeout(this.toNextLevel, 3000)
  },
  unmounted () {
    clearTimeout()
  },
  setup (props, { emit }) {
    const auddjs = [
      {
        para: '중요한 것은 감동하고, 사랑하며, 소망하며, 요동하며 사는 것이다. 예술가가 되기 전에 사람이 돼라.',
        author: '로댕'
      },
      {
        para: '유능한 예술가는 모방하고 위대한 예술가는 훔친다.',
        author: '피카소'
      },
      {
        para: '우물쭈물하다가 내 이럴줄 알았지.',
        author: '버나드 쇼'
      },
      {
        para: '그림이란 숱한 비합리적 상상력에 의해서 만들어지는 천연색 사진이다.',
        author: '살바도르 달리'
      },
      {
        para: '진정한 화가는 캔버스를 두려워하지 않는다. 오히려 캔버스가 화가를 두려워한다..',
        author: '빈센트 반 고흐'
      },
      {
        para: '경험을 현명하게 사용한다면 어떤 일도 시간 낭비가 아니다.',
        author: '로댕'
      },
      {
        para: '가는 디자인 좋아야 오는 프로그램 좋다.',
        author: '★안영진☆'
      },
      {
        para: '입실체크 놓치지 말자',
        author: '천수승'
      },
      {
        para: '늦었다고 생각될 때가 진짜 늦은거다.',
        author: '박명수'
      },
      {
        para: '나는 고석환이다.',
        author: '김선우'
      }
    ]
    const idx = Math.floor(Math.random() * 10)
    const ddd = ref(auddjs[idx])
    const toNextLevel = () => {
      // store.dispatch('setPlayState')
      roundEndEnded()
      // console.log('to nxt level', store.state.playState)
    }

    const roundEndEnded = () => {
      emit('roundend-ended')
    }

    return {
      toNextLevel,
      roundEndEnded,
      ddd
    }
  }
}
</script>

<style>
</style>
