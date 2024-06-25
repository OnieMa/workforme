<template>
  <div id="root" class="frame">
    <div class="todo">
      <SchoolVue name="121"></SchoolVue>
    </div>
  </div>
</template>
<script>
import SchoolVue from "./components/School.vue";
export default {
  name: "App",
  components: {SchoolVue},
  data() {
    return {
    }
  },
  computed: {

  },
  methods: {

  },
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