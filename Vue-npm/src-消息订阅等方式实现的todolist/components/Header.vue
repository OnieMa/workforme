<script>
import {nanoid} from "nanoid";
import 'animate.css'

export default {
  name: "Header",
  data() {
    return {
      name: "test",
      isShow: true
    }
  },
  props: ['receive'],
  methods: {
    add(e) {
      if (!e.target.value)
        return
      // 将输入包装为对象
      const todoObj = {
        id: nanoid(),
        todo: e.target.value,
        done: false,
      }
      this.receive(todoObj);
      e.target.value = ''
    }
  },
}
</script>

<template>
  <div id="todoHeader" class="main">
    <button @click="isShow=!isShow">测试动画</button>

    <transition-group
        name="animate__animated animate__bounce"
        enter-active-class="animate__swing"
        leave-active-class="animate__backOutUp"
    >
      <input key="2" v-show="isShow" type="text" placeholder="输入待办事项" v-model="name" @keyup.enter="add">
      <input key="1" v-show="isShow" type="text" placeholder="输入待办事项" v-model="name" @keyup.enter="add">
    </transition-group>
  </div>
</template>

<style>
.main {
  margin: 5px;
}

// 使用过渡的实现方式
.v-enter, .v-leave-to {
  transform: translateX(-100%);
}

.v-enter-active, .v-leave-active {
  transition: 0.5s linear;
}

.v-enter-to, .v-leave {
  transform: translateX(0px);
}


</style>