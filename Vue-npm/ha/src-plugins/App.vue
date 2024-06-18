<script>
import SchoolVue from "./components/School.vue";
import StudentVue from "./components/Student.vue";


export default {
  name: "App",
  data() {
    return {
      msg: "hello",
      stuAge: 20

    }
  },
  components: {
    School: SchoolVue,
    Student: StudentVue
  },
  methods: {
    showDOM() {
      this.stuAge += 1
    }
  },
}
</script>

<template>
  <div>
    <h1 v-text="msg" ref="title"></h1>
    <button @click="showDOM" ref="btu">点我展示</button>
    <!--    ref 可以获取子组件的vm-->
    <School ref="sch" name="xi'an" :age='90'/>
    <hr>

    <School name="stuName-哈喽" :age="stuAge"/>
    <hr>
    <Student/>
  </div>
</template>

<style scoped>

</style>