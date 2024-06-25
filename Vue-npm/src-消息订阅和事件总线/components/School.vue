<script>
import Student from "@/components/Student.vue";
import pubsub from 'pubsub-js'
export default {
  name: "SchoolVue",
  components: {Student},
  data() {
    return {
      schoolName: 'huadong',
      schoolAddr: 'yulin',
      stu: {
        name: ''
      }
    }
  },
  methods: {
    death() {
      this.$destroy();
    }
  },
  mounted() {
    this.$bus.$on("hello", (data) => {
      this.stu.name = data
    })
    this.pubId = pubsub.subscribe("getData", function (a,b) {
      console.log(a,b)
    });
  },
  beforeMount() {
    this.$bus.$off('hello')
    pubsub.unsubscribe(this.pubId)
  }
}
</script>

<template>
  <div id="root">
    <h2>schoolName : {{ schoolName }}</h2>
    <hr>
    <Student/>
    <button @click="death">死掉</button>
  </div>
</template>
