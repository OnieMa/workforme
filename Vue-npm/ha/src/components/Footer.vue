<script>
export default {
  name: "Footer",
  data() {
    return {
      isChecked: false
    }
  },
  methods: {
    toggleButton() {
      this.isChecked = !this.isChecked
      this.$emit('checkAll', this.isChecked)
    },
    clearAllok() {
      this.$emit("clearAllTodo")
    }
  },
  props: ["nums"]
}
</script>

<template>
  <div id="todoFooter">
    <input type="checkbox" id="c" @click="toggleButton">
    <label for="c">
      已确定 {{nums.ok}}/{{nums.all}}
    </label>
    <button class="main" @click="clearAllok"> 清除所有已完成</button>
  </div>
</template>

<style scoped>
.main {
  margin-left: auto;
  margin-right: auto;
  width: 300px;
  border-radius: 5px;
}

</style>