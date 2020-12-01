<template>
  <div>
    <router-link :to="{name: 'image', params: {postId: postId, imageOrder: imageOrder}}" >
      <img
        :src="'http://localhost:8000' + image.file + ':sm'"
        class="border border-grey-10 border-t-0 border-r-0 hover:opacity-80 transition duration-100"
        :class="borderRoundClass"
      />
    </router-link>
  </div>
</template>

<script>
export default {
  computed: {
    borderRoundClass() {
      switch (this.imageOrder) {
        case 0:
          return 'rounded-tl-xl';
        case 1:
          return 'rounded-tr-xl';
        case 2:
          return 'rounded-bl-xl';
        case 3:
          return 'rounded-br-xl';
        default:
          console.log("Invalid image order")
          return null;
      }
    }
  },
  props: {
    image: {
      required: true,
      type: Object
    },
    postId: {
      required: true,
    },
    imageOrder: {
      required: true,
    }
  }
}
</script>