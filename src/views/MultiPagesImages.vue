<template>
  <div>
    <div v-for="image in paginatedImages" :key="image">
      <img :src="image" />
    </div>
    <paginate
      :page-count="totalPages"
      :click-handler="changePage"
      prev-text="Prev"
      next-text="Next"
      container-class="pagination"
      page-class="page-item"
      page-link-class="page-link"
      prev-class="page-item"
      prev-link-class="page-link"
      next-class="page-item"
      next-link-class="page-link"
    />
  </div>
</template>

<script>
import axios from "axios";
import Paginate from "vuejs-paginate";

export default {
  components: {
    Paginate,
  },
  data() {
    return {
      images: [],
      currentPage: 1,
      imagesPerPage: 10,
    };
  },
  computed: {
    paginatedImages() {
      const startIndex = (this.currentPage - 1) * this.imagesPerPage;
      const endIndex = startIndex + this.imagesPerPage;
      return this.images.slice(startIndex, endIndex);
    },
    totalPages() {
      return Math.ceil(this.images.length / this.imagesPerPage);
    },
  },
  methods: {
    changePage(pageIndex) {
      this.currentPage = pageIndex;
    },
    fetchImages() {
      axios
        .get("/api/images")
        .then((response) => {
          this.images = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.fetchImages();
  },
};
</script>
