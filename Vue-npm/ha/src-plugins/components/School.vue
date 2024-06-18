<script>
// 引入一个混合
export default {
  name: "SchoolVue",
  data: function () {
    return {
      newName: this.name + '.cn'
    }
  },
  props: {
    name: {
      type: String,
      required: true,
    },
    age: {
      type: Number,
      default: 30
    }
  }

}
</script>

<template>
  <div id="root">
    <input type="text" v-fbind="this.name"></input>
    <h2>name : {{ newName | mySlice }} {{ age + 5 }}</h2>
    <button @click="hello">点我测试hello</button>
  </div>
</template>
