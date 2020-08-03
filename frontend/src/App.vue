<template>
  <div id="app">
    <div class="container">
      <div class="heading">
        Is mercury in retrograde ??
      </div>
      <kinesis-container>
        <kinesis-element :strength="120">
          <div class="text">
            {{ temp }}
          </div>
          <img src="./rocket.png" alt="rocket" />
        </kinesis-element>

        <!-- background-circles-props -->
        <kinesis-element :strength="50" axis="y">
          <div class="circle circle-purple"></div>
        </kinesis-element>
        <kinesis-element :strength="80" axis="y">
          <div class="circle circle-purple1"></div>
        </kinesis-element>
        <kinesis-element :strength="80" axis="y">
          <div class="circle circle-purple2"></div>
        </kinesis-element>
        <kinesis-element :strength="80" axis="y">
          <div class="circle circle-purple3"></div>
        </kinesis-element>
      </kinesis-container>
    </div>
  </div>
</template>
<script>
import getinfo from "./services/getInfo";

export default {
  name: "App",

  data() {
    return {
      temp: "",
    };
  },

  async mounted() {
    this.temp = (await getinfo.status()).data;
  },
};
</script>

<style>
#app {
  text-align: center;
}
.heading {
  color: #f2eafa;
  font-size: 60px;
  position: absolute;
  text-align: center;
  bottom: 90%;
  left: 20%;
  right: 20%;
  top: 5%;
}
.text {
  color: #f2eafa;
  font-size: 40px;
}
.container {
  padding: 12rem 0;
  background-color: #00146b;
}

.circle {
  position: absolute;
  border-radius: 100%;
}

.circle.circle-purple {
  border: 10px solid #f2eafa;
  opacity: 0.1;
  width: 4vw;
  height: 4vw;
  left: 10%;
  top: 25%;
}

.circle.circle-purple1 {
  border: 15px solid #f2eafa;
  opacity: 0.1;
  width: 8vw;
  height: 8vw;
  right: -2%;
  bottom: 17%;
}
.circle.circle-purple2 {
  background-color: #f2eafa;
  opacity: 0.1;
  width: 5vw;
  height: 5vw;
  left: 20%;
  bottom: 17%;
}

.circle.circle-purple3 {
  border: 15px solid #f2eafa;
  opacity: 0.3;
  width: 3vw;
  height: 3vw;
  top: 80%;
  left: 60%;
}
</style>
