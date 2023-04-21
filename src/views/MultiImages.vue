<!-- MultiImages.vue -->
<template>
  <div>
    <image-list></image-list>
  </div>
</template>

<script>
import ImageList from "../components/MultiPagesImages.vue";
export default {
  components: {
    ImageList,
  },
};
</script>

<style>
.bar {
  text-align: center;
  width: 100%;
  background-color: hsl(90, 2%, 25%);
  display: relative;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}
</style>
