<template>
  <div>
    <router-link v-if="postId" :to="{name: 'image-from-post', params: {postId: postId, imageOrder: image.order}}" >
    
      <img
        :src="image.file + ':sm'"
        class="border border-grey-10 border-t-0 border-r-0 hover:opacity-80 transition duration-100"
        :class="borderRoundClass"
      />
    </router-link>
    <router-link v-if="!postId" :to="{name: 'image-from-search', params: {imageId: image.id}}">
      <img
        :src="image.file + ':sm'"
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
      if (!this.search) {
        switch (this.image.order) {
          case 1:
            return 'rounded-tl-xl';
          case 2:
            return 'rounded-tr-xl';
          case 3:
            return 'rounded-bl-xl';
          case 4:
            return 'rounded-br-xl';
          default:
            return 'rounded-xl';
        }
      } else {
        return 'rounded-xl'
      }
    }
  },
  props: {
    image: {
      required: true,
      type: Object
    },
    postId: {
      required: false,
    },
    search: {
      required: false,
      default: false,
    }
  }
}
</script>