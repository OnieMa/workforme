<script>
import Item from "@/components/Item.vue";

export default {
  name: "List",
  components: {Item},
  props:['todos',]
}
</script>

<template>
  <div id="todoList" class="todoList">
    <ul>
      <li class="li">
        <Item class="li" v-for="todoObj in todos" :key="todoObj.id" :task="todoObj"/>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.todoList{
  height: 300px;
  padding: 10px;
  border: #42b983 1px solid;
  margin: 2px;
}
.li{
  list-style: none;
}
</style>