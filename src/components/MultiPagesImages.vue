<template>
  <div>
    <div class="container">
      <vf-layout justify="space-between">
        <div>
          <vf-layout-item>
            <img
              v-for="(image, index) in paginatedImages1"
              :key="index"
              :src="image"
            />
          </vf-layout-item>
          <vf-layout-item>
            <img
              v-for="(image, index) in paginatedImages2"
              :key="index"
              :src="image"
            />
          </vf-layout-item>
          <vf-layout-item>
            <img
              v-for="(image, index) in paginatedImages3"
              :key="index"
              :src="image"
            />
          </vf-layout-item>
        </div>
      </vf-layout>
    </div>
    <nav class="pagination-container">
      <label for="images-per-page">/Page</label>
      <select id="images-per-page" v-model="imagesPerPage">
        <option value="12">12</option>
        <option value="21">21</option>
        <option value="45">45</option>
      </select>
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
        page-range="3"
      >
      </v-paginate>
    </nav>
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
      imagesPerPage: 12,
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
        startIndex + this.imagesPerPage / 3 + 1,
        startIndex + this.imagesPerPage / 3 + 1 + this.imagesPerPage / 3
      );
    },
    paginatedImages3() {
      const startIndex = (this.currentPage - 1) * this.imagesPerPage;
      const endIndex = startIndex + this.imagesPerPage;
      return this.images.slice(
        startIndex + this.imagesPerPage / 3 + 1 + this.imagesPerPage / 3 + 1,
        endIndex
      );
    },
    pageCount() {
      return Math.ceil(this.images.length / this.imagesPerPage);
    },
    pageRow() {
      return Math.ceil(this.images.imagesPerPage / 5);
    },
    perRowImages() {
      const startIndex = (this.currentPage - 1) * this.imagesPerPage;
      const startIndex_1 = startIndex + this.imagesPerPage;
      const endIndex_1 = startIndex_1 + this.pageRow;
      return this.images.slice(startIndex_1, endIndex_1);
    },
  },
  methods: {
    changePage(pageIndex) {
      this.currentPage = pageIndex;
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

/* Write your own CSS for pagination */
.pagination {
}
.page-item {
}
.pagination-container {
  display: flex;
  align-items: center;
  height: 100%;
  font-size: 16px;
}

.image-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.image-row img {
  width: calc(33.33% - 10px);
  height: auto;
}

.container {
  width: 100%;
  max-width: 1500px;
  margin: 10px auto;
}
</style>
