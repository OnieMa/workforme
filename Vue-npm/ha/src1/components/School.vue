<script>
// 引入一个混合
import mixin from "@/components/mixin";
export default {
  name: "SchoolVue",
  data: function () {
    return {
      newName: this.name + '.cn'
    }
  },
  mixins: [mixin],
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
    <h2 @click="alert">name : {{ newName }} {{ age + 5 }}</h2>
  </div>
</template>
