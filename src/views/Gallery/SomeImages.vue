<!--<1>-->
<template>
  <div>
    <div v-for="image in images" :key="image">
      <img :src="image" />
    </div>
  </div>
</template>

<script>
export default {
  name: "SomeImages",
  data() {
    return {
      images: [],
    };
  },
  mounted() {
    // Fetch the image URLs from the Flask API
    fetch("/api/images")
      .then((response) => response.json())
      .then((data) => {
        this.images = data.images;
      });
  },
};
</script>

<!--<2>-->
<!--<template>-->
<!--  <div>-->
<!--    <img :src="getImageUrl('1.png')" alt="You Want Image" />-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--export default {-->
<!--  methods: {-->
<!--    getImageUrl(imageName) {-->
<!--      return `http://localhost:5000/static/images/${imageName}`;-->
<!--    },-->
<!--  },-->
<!--};-->
<!--</script>-->

<!--<3>-->
<!--<template>-->
<!--  <div class="iframe_box">-->
<!--    <div-->
<!--      class="load"-->
<!--      v-loading.fullscreen.lock="loading"-->
<!--      element-loading-text="拼命加载中"-->
<!--    ></div>-->
<!--    <div>-->
<!--      <iframe-->
<!--        id="iframe"-->
<!--        :src="bdTokenUrl"-->
<!--        width="100%"-->
<!--        height="100%"-->
<!--        ref="iframeDom"-->
<!--        frameborder="0"-->
<!--      ></iframe>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->
<!--<script>-->
<!--export default {-->
<!--  name: "iframe-2",-->
<!--  data() {-->
<!--    return {-->
<!--      bdTokenUrl: "Image-gallery/image_gallery.html",-->
<!--    };-->
<!--  },-->
<!--  mounted() {-->
<!--    /**-->
<!--     * iframe-宽高自适应显示-->
<!--     */-->
<!--    const oIframe = document.getElementById("iframe");-->
<!--    const deviceWidth = document.documentElement.clientWidth;-->
<!--    const deviceHeight = document.documentElement.clientHeight;-->
<!--    oIframe.style.width = Number(deviceWidth) - 220 + "px"; //数字是页面布局宽度差值-->
<!--    oIframe.style.height = Number(deviceHeight) - 120 + "px"; //数字是页面布局高度差-->
<!--  },-->
<!--};-->
<!--</script>-->
