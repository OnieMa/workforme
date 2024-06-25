<script>
import pubsub from "pubsub-js";

export default {
  name: "Item",
  data() {
    return {
      lists: 'hallo',
      isShow: true
    }
  },
  props: ["task"],
  methods: {
    delTask(id) {
      console.log(id)
    },
    editTask(todo) {
      if (todo.hasOwnProperty('isEdit')) {
        todo.isEdit = true
      } else {
        this.$set(todo, 'isEdit', true);
      }
      this.$nextTick(function () {
        this.$refs.inputEdit.focus()
      });
    },
    noEdit(todo) {
      todo.isEdit = false
    },
  },

}
</script>

<template>
  <div id="todoItem">
    <div class="rowStyle">
      <!--      <input type="checkbox" :checked="task.done" @change="changeTodo(task.id)">{{ task.todo }}-->
      <input type="checkbox" v-model="task.done">
      <span v-show="!task.isEdit">{{ task.todo }}</span>
      <input v-show="task.isEdit" type="text" :value="task.todo" ref="inputEdit">
      <button class="keepRight" @click="delTask(task.id)">del</button>
      <button class="keepRight" @click="editTask(task)" @blur="noEdit(task)">edit</button>
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