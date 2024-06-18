<template>
  <div id="root" class="frame">
    <div class="todo">
      <Header :receive="addTodo"/>
      <List :todos="todos"/>
      <Footer v-on:checkAll="setChecked" :nums="nums" @clearAllTodo="clearAllTodo"/>
    </div>
  </div>

</template>
<script>
import pubsub from "pubsub-js";
import Footer from "@/components/Footer.vue";
import Header from "@/components/Header.vue";
import List from "@/components/List.vue";

export default {
  name: "App",
  components: {Header, Footer, List},
  data() {
    return {
      todos: [
        {
          id: '0001',
          todo: 'eat',
          done: true
        },
        {
          id: '0002',
          todo: 'drink',
          done: false
        },
        {
          id: '0003',
          todo: 'car',
          done: true
        }
      ],
      isAllChecked: false,
    }
  },
  computed: {
    nums() {
      const allTodolen = this.todos.length
      const okTodo = this.todos.reduce((count, obj) => {
        return count + (obj.done ? 1 : 0);
      }, 0);
      return {
        all: allTodolen,
        ok: okTodo
      }
    }
  },
  methods: {
    addTodo(x) {
      this.todos.unshift(x)
    },
    setChecked(ischecked) {
      console.log(this)
      this.isAllChecked = ischecked
      this.todos.forEach((todo) => {
        todo.done = this.isAllChecked;
      });
    },
    clearAllTodo() {
      this.todos = this.todos.filter(todo => {
        return !todo.done
      })
    }
  },
  mounted() {
    pubsub.subscribe('edit',(s,b)=>{

    })
  }
}
</script>

<style>
.frame {
  border: 1px solid gray;
  padding: 10px;
  width: 500px;
  height: 1000px;
}
</style>