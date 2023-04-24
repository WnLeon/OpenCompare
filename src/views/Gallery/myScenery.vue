<!-- myBeauty.vue -->
<template>
  <MultiImages />
  <image-list :imagesapi="parentVar"></image-list>
</template>

<script>
import ImageList from "../../components/MultiPagesImages.vue";
import MultiImages from "./MultiImages.vue";
export default {
  components: {
    ImageList,
    MultiImages,
  },
  data() {
    return {
      parentVar: "/api/imagesfengjing",
    };
  },
};
</script>
