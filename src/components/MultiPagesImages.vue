<template>
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
      page-range="3"
    />
    <span>Page</span>
    <input type="number" name="page" v-model="inputValue" />
    <button @click="updateValue">GO</button>
  </div>
</template>
<script>
import axios from "axios";
import vPaginate from "vuejs-paginate-next";
// const imagesapi = "/api/imagesmeinv";

export default {
  props: {
    imagesapi: String,
  },
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
    getimagesapi() {
      return `${this.imagesapi}`;
    },
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
        const response = await axios.get(this.getimagesapi);
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
/* @import "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"; */

.container,
.container-fluid,
.container-lg,
.container-md,
.container-sm,
.container-xl,
.container-xxl {
  text-align: center;
  position: relative;
  height: 100%;
  max-width: 1200px;
  padding-right: var(--bs-gutter-x, 0.75rem);
  padding-left: var(--bs-gutter-x, 0.75rem);
  margin-right: auto;
  margin-left: auto;
}

.page {
  overflow: auto;
  white-space: nowarp;
  display: inline-flex;
  text-align: center;
  height: 38px;
  padding: 10px 0 20px;
  color: black;
}
.page li {
  display: inline;
  line-height: 22px;
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
  padding: 10px 10px 20px;
}

.page button:active {
  z-index: 3;
  color: #fff;
  background-color: #0d6efd;
  border-color: #0d6efd;
}

.page-link {
  padding: 0.375rem 0.75rem;
  position: relative;
  display: block;
  color: #0d6efd;
  text-decoration: none;
  background-color: #fff;
  border: 1px solid #dee2e6;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out,
    border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}
@media (prefers-reduced-motion: reduce) {
  .page-link {
    transition: none;
  }
}
.page-link:hover {
  z-index: 2;
  color: #0a58ca;
  background-color: #e9ecef;
  border-color: #dee2e6;
}
.page-link:focus {
  z-index: 3;
  color: #0a58ca;
  background-color: #e9ecef;
  outline: 0;
  box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
}
.page-item.active .page-link {
  z-index: 3;
  color: #fff;
  background-color: #0d6efd;
  border-color: #0d6efd;
}

.page-item.disabled .page-link {
  color: #6c757d;
  pointer-events: none;
  background-color: #fff;
  border-color: #dee2e6;
}
.page-item:first-child .page-link {
  border-top-left-radius: 0.25rem;
  border-bottom-left-radius: 0.25rem;
}
.page-item:last-child .page-link {
  border-top-right-radius: 0.25rem;
  border-bottom-right-radius: 0.25rem;
}

.page-item:not(:first-child) .page-link {
  margin-left: -1px;
}
.pagination-lg .page-link {
  padding: 0.75rem 1.5rem;
  font-size: 1.25rem;
}
.pagination-lg .page-item:first-child .page-link {
  border-top-left-radius: 0.3rem;
  border-bottom-left-radius: 0.3rem;
}
.pagination-lg .page-item:last-child .page-link {
  border-top-right-radius: 0.3rem;
  border-bottom-right-radius: 0.3rem;
}
.pagination-sm .page-link {
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
}
.pagination-sm .page-item:first-child .page-link {
  border-top-left-radius: 0.2rem;
  border-bottom-left-radius: 0.2rem;
}
.pagination-sm .page-item:last-child .page-link {
  border-top-right-radius: 0.2rem;
  border-bottom-right-radius: 0.2rem;
}

.image-row {
  width: 1200px;
  display: flex;
  justify-content: space-around;
  margin: 10px 0;
}

.image-row img {
  width: calc(33.33% - 20px);
  height: auto;
}
</style>
