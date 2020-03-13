<template>
  <div class="home">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
export default {
  name: "Home",
  components: {
  },
  data() {
    return {
      msg: 'hello'
    };
  },
  methods: {
    getmessage() {
      const path = 'http://localhost:5000/home';
      axios.get(path).then((res) => {
        this.msg = res.data;
      }).catch((error) => {
        console.error(error);
      });
    },
  },
  created(){
    this.getmessage();
  },
};
</script>
