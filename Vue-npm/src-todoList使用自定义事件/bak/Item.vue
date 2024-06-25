<script>
export default {
  name: "Item",
  data() {
    return {
      lists: 'hallo'
    }
  },
  props: ["task",'changeTodo'],

}
</script>

<template>
  <div id="todoItem">
    <div class="rowStyle">
      <input type="checkbox" :checked="task.done" @change="changeTodo(task.id)">{{ task.todo }}
      <button class="keepRight">del</button>
    </div>
  </div>

</template>

<style scoped>
.keepRight {
  float: right;
}
.rowStyle{
  height: 25px;
  line-height: 30px;
  padding: 5px;
  border: 1px solid #ddd;
  margin: 2px;
}
</style>