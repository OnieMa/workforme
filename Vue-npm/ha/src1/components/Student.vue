<script>
export default {
  name: "StudentVue",
  data: function () {
    return {
      name: 'zhangsan',
      age: 12
    }
  },
  methods: {
    alert() {
      alert(this.name);
    }
  }

}
</script>

<template>
  <div id="root">
    <h3 @click="alert">name : {{ name }} {{ age }}</h3>
  </div>
</template>
