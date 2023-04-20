<template>
  <div class="container">
    <vf-layout justify="space-between">
      <div>
        <vf-layout-item>
          <img
            v-for="(image, index) in images.slice(0, 33)"
            :key="index"
            :src="image"
          />
        </vf-layout-item>
        <vf-layout-item>
          <img
            v-for="(image, index) in images.slice(34, 66)"
            :key="index"
            :src="image"
          />
        </vf-layout-item>
        <vf-layout-item>
          <img
            v-for="(image, index) in images.slice(67, 99)"
            :key="index"
            :src="image"
          />
        </vf-layout-item>
      </div>
    </vf-layout>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ImageLayout",
  data() {
    return {
      images: [],
    };
  },
  methods: {
    async fetchImages() {
      try {
        const response = await axios.get("/api/images");
        this.images = response.data.images;
      } catch (error) {
        console.log(error);
      }
    },
  },
  async mounted() {
    await this.fetchImages();
  },
};
</script>

<style>
.container {
  width: 100%;
  max-width: 1500px;
  margin: 10px auto;
}
</style>
