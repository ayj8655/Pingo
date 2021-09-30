<template>
<head>
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/all.css" integrity="sha384-DyZ88mC6Up2uqS4h/KRgHuoeGwBcD4Ng9SiP4dIRy0EXTlnuz47vAwmeGwVChigm" crossorigin="anonymous">
</head>
<div class="room-box">
  <div class="room-box-left">
    <p>{{room.room_id}}</p>
    <p>{{room.room_name}}</p>
    <p>{{room.room_owner}}</p>
    <p>{{room.problems}}</p>
  </div>

  <div class="room-box-right">
    <i class="fas fa-lock" v-if="room.is_locked"></i>
  </div>
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
    justify-content:left;
    width: 18rem;
    height: 3rem;
    background-color: #FFF9BA;
    margin: 10px;
    box-shadow: 2px 2px 6px 0 #94906b;
    cursor: pointer;
    padding: 0.1rem;
    align-items: center;
    justify-content: space-between;
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
  .room-box-left{
    display: flex;
    justify-content: left;
    margin-left: 1rem;
  }
  .room-box-right{
    display: flex;
    justify-content: right;
    margin-right: 1rem;
  }

</style>
