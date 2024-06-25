<script>
import pubsub from 'pubsub-js'
export default {
  name: "StudentVue",
  data: function () {
    return {
      name: 'zhangsan',
      age: 12
    }
  },
  methods: {
    sendStuName() {
      this.$bus.$emit('hello', this.name)
    },
    sendStuAge(){
      pubsub.publish('getData',"dhsjhfgshjg")
    }
  },
  mounted() {

  }


}
</script>

<template>
  <div id="root">
    <h3>name : {{ name }} {{ age }}</h3>
    <button @click="sendStuName">把学生名字给school</button>
    <button @click="sendStuAge">把学生age给school</button>
  </div>
</template>
