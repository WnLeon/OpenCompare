<template>
  <div>
    <div class="container">
      <vf-layout class="image-row" justify="space-around">
        <img
          v-for="(image, index) in paginatedImages1"
          :key="index"
          :src="image"
          style="object-fit: cover"
        />
      </vf-layout>
      <vf-layout class="image-row" justify="space-around">
        <img
          v-for="(image, index) in paginatedImages2"
          :key="index"
          :src="image"
          style="object-fit: cover"
        />
      </vf-layout>
      <vf-layout class="image-row" justify="space-around">
        <img
          v-for="(image, index) in paginatedImages3"
          :key="index"
          :src="image"
          style="object-fit: cover"
        />
      </vf-layout>
    </div>
    <div class="page">
      <v-paginate
        :pageCount="pageCount"
        :click-handler="changePage"
        first-button-text="First"
        last-button-text="Last"
        prev-text="Prev"
        next-text="Next"
        first-last-button="True"
        container-class="pagination"
        page-class="page-item"
        page-link-class="page-link"
        prev-class="page-item"
        prev-link-class="page-link"
        next-class="page-item"
        next-link-class="page-link"
        page-range="5"
      />
      <span>Page</span>
      <input type="number" name="page" v-model="inputValue" />
      <button @click="updateValue">GO</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import vPaginate from "vuejs-paginate-next";

export default {
  components: {
    vPaginate,
  },
  data() {
    return {
      images: [],
      currentPage: 1,
      imagesPerPage: 9,
    };
  },
  computed: {
    paginatedImages1() {
      const startIndex = (this.currentPage - 1) * this.imagesPerPage;
      // const endIndex = startIndex + this.imagesPerPage;
      return this.images.slice(startIndex, startIndex + this.imagesPerPage / 3);
    },
    paginatedImages2() {
      const startIndex = (this.currentPage - 1) * this.imagesPerPage;
      // const endIndex = startIndex + this.imagesPerPage;
      return this.images.slice(
        startIndex + this.imagesPerPage / 3,
        startIndex + this.imagesPerPage / 3 + this.imagesPerPage / 3
      );
    },
    paginatedImages3() {
      const startIndex = (this.currentPage - 1) * this.imagesPerPage;
      const endIndex = startIndex + this.imagesPerPage;
      return this.images.slice(
        startIndex + this.imagesPerPage / 3 + this.imagesPerPage / 3,
        endIndex
      );
    },
    pageCount() {
      return Math.ceil(this.images.length / this.imagesPerPage);
    },
  },
  methods: {
    changePage(pageIndex) {
      this.currentPage = pageIndex;
    },
    updateValue() {
      this.currentPage = this.inputValue;
    },
    async fetchImages() {
      try {
        const response = await axios.get("/api/images");
        this.images = response.data.images;
      } catch (error) {
        console.log(error);
      }
    },
  },
  watch: {
    imagesPerPage: function (newVal, oldVal) {
      const newPage = Math.ceil((oldVal * this.currentPage) / newVal);
      this.currentPage = newPage;
    },
  },
  async mounted() {
    await this.fetchImages();
  },
};
</script>

<style lang="css">
/* Adopt bootstrap pagination stylesheet. */
@import "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css";

.container {
  position: relative;
  width: 80%;
  height: 80%;
  max-width: 3840px;
  max-height: 2160px;
}

.page {
  display: inline-flex;
  text-align: center;
  width: 100%;
  bottom: 0;
  height: 38px;
  padding: 10px 30%;
  color: black;
}
.page a,
.page button,
.page a:visited,
.page b,
.page > input {
  background: #fff;
  padding: 0 16px;
  border: 1px solid #ddd;
  display: inline-block;
  height: 36px;
  line-height: 36px;
  margin: 0 4px 0 5px;
  font-size: 14px;
  border-radius: 3px;
}
.page > input {
  width: 40px;
  padding: 0 5px;
  text-align: center;
  margin: 0;
}
/* .page a:hover, */
.page b {
  background: #63b504;
  border: 1px solid #63b504;
  color: #fff;
  text-decoration: none;
}
.page span {
  padding: 5px 10px;
}

.image-row {
  display: flex;
  justify-content: space-around;
  margin-bottom: 20px;
}

.image-row img {
  width: calc(33.33% - 20px);
  height: auto;
}
</style>
