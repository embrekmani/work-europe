<template>
  <div>
    <Navigation />
    <nuxt />
  </div>
</template>

<script>
import Navigation from '~/components/Navigation.vue';

export default {
  components: {
    Navigation
  },
  head() {
    return {
      title: 'Work Europe',
      meta: [
        { hid: 'description', name: 'description', content: 'The job board for location agnostic EU workers.' }
      ]
    }
  }
}
</script>


<style>
html, body {
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  scroll-behavior: smooth;
}

.el-container.outer {
  max-width: 1216px;
  margin: 0 auto;
}
</style>
