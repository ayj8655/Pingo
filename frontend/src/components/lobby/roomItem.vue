<template>
<div class="room-box">
  <p>{{room.room_id}}</p>
  <p>{{room.room_name}}</p>
  <p>{{room.room_owner}}</p>
  <p>{{room.problems}}</p>
</div>
</template>

<script>
export default {
  name: 'room',
  props: {
    room: {
      type: Object,
    }
  },

}
</script>

<style>
  .room-box {
    display: flex;
    align-content: space-between;
    justify-content:left;
    width: 18rem;
    height: 3rem;
    background-color: #FFF9BA;
    margin: 10px;
    box-shadow: 2px 2px 6px 0 #94906b;
    cursor: pointer;
    padding: 0.1rem;
  }

  .room-box:hover {
    display: flex;
    justify-content: left;
    width: 18.1rem;
    height: 3.1rem;
    background-color: #FFF9BA;
    margin: 10px;
    box-shadow: 2px 2px 6px 0 #94906b;
    cursor: pointer;
    transition: ;
  }

</style>
