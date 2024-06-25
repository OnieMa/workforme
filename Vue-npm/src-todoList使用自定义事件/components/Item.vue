<script>
export default {
  name: "Item",
  data() {
    return {
      lists: 'hallo'
    }
  },
  props: ["task"],
  methods: {
    delTask(id) {
      console.log(id)
    }
  },

}
</script>

<template>
  <div id="todoItem">
    <div class="rowStyle">
      <!--      <input type="checkbox" :checked="task.done" @change="changeTodo(task.id)">{{ task.todo }}-->
      <input type="checkbox" v-model="task.done">
      {{ task.todo }}
      <button class="keepRight" @click="delTask(task.id)">del</button>
    </div>
  </div>

</template>

<style scoped>
.keepRight {
  float: right;
}

.rowStyle {
  height: 25px;
  line-height: 30px;
  padding: 5px;
  border: 1px solid #ddd;
  margin: 2px;
}
</style>