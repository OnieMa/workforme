<script>
import {nanoid} from "nanoid";

export default {
  name: "Header",
  data() {
    return {
      name: "test"
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
      e.target.value=''


    }
  },
}
</script>

<template>
  <div id="todoHeader" class="main">
    <input type="text" placeholder="输入待办事项" v-model="name" @keyup.enter="add">
  </div>
</template>

<style scoped>
.main {
  margin: 5px;
}
</style>