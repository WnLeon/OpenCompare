<template>
  <div class="image-row">
    <img src="image1.jpg">
    <img src="image2.jpg">
    <img src="image3.jpg">
  </div>
  <div class="image-row">
    <img src="image4.jpg">
    <img src="image5.jpg">
    <img src="image6.jpg">
  </div>
  <div class="image-row">
    <img src="image7.jpg">
    <img src="image8.jpg">
    <img src="image9.jpg">
  </div>
<nav class="pagination-container">
      <label for="images-per-page">/Page</label>
      <select id="images-per-page" v-model="imagesPerPage" dataformatas="12">
        <option value="5">5</option>
        <option value="10">10</option>
        <option value="20">20</option>
        <option value="50">50</option>
        <option value="99">99</option>
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
</template>

<script>
export default {
  name: "test"
  const imagesPerPage = 3;
  const rows = [];

  for (let i = 0; i < images.length; i += imagesPerPage) {
    rows.push(images.slice(i, i + imagesPerPage));
}
}
</script>

<style scoped>
.image-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.image-row img {
  width: calc(33.33% - 10px);
  height: auto;
}
</style>