<template>
  <el-container class="outer">
    <el-aside width="400px">
      <h1>Find your place in Europe.</h1>
      <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis gravida mi sem, at aliquet neque interdum nec. Duis convallis semper cursus. Vestibulum efficitur lorem erat. Cras sed dui vel mi rhoncus vestibulum sed eget urna. Nullam sapien metus, rhoncus in nunc quis, imperdiet sagittis risus.</p>
    </el-aside>

    <el-main>    
      <el-carousel height="50vh" trigger="click">
        <el-carousel-item v-for="(img, i) in images" :key="i">
          <el-image :src="getImageUrl(img)" fit="contain"/>
        </el-carousel-item>
      </el-carousel>
    </el-main>
  </el-container>
</template>

<script>

export default {
  components: {
  },
  data() {
    return {
      images: ['benjamin-davies-Oja2ty_9ZLM-unsplash.jpg', 'chris-karidis-nnzkZNYWHaU-unsplash.jpg', 'stefan-widua-iPOZf3tQfHA-unsplash.jpg']
    }
  },
  methods: {
    getImageUrl(url) {
      return require('../static/' + url)
    }
  }
}
</script>

<style lang="scss">
.el-aside {
  padding: 1rem;
  h1 {
    margin: 0;
    font-weight: 300;
    font-size: 2.5rem;
    color: #303133;
  }
  p {
    color: #606266;
  }
}

.el-carousel {
  width: 100%;
  border-radius: .25rem;
}
</style>
