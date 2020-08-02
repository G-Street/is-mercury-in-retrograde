<template>
  <div id="app">
    <kinesis-container>
      Here, you can put
      <kinesis-element :strength="10">
        whatever
      </kinesis-element>
      <kinesis-element :strength="20">
        content!
      </kinesis-element>
    </kinesis-container>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>
