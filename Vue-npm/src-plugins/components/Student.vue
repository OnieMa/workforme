<script>
export default {
  name: "StudentVue",
  data: function () {
    return {
      name: 'zhangsan',
      age: 12
    }
  }


}
</script>

<template>
  <div id="root">
    <h3>name : {{ name }} {{ age }}</h3>
  </div>
</template>
