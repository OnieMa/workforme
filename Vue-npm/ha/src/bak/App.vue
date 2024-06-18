<script>
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
      ]
    }
  },
  methods: {
    addTodo(x) {
      this.todos.unshift(x)
    },
    changeTodo(id) {
      this.todos.forEach((todo) => {
        if (todo.id === id) {
          todo.done = !todo.done
        }
      });
    }
  },

}
</script>

<template>
  <div id="root" class="frame">
    <div class="todo">
      <Header :receive="addTodo"/>
      <List :todos="todos" :changeTodo="changeTodo"/>
      <Footer/>
    </div>
  </div>

</template>

<style>
.frame {
  border: 1px solid gray;
  padding: 10px;
  width: 500px;
  height: 1000px;
}
</style>