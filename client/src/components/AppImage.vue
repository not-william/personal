<template>
  <div
    :class="gridSpan"
  >
    <router-link :to="imageTo">
      <img
        :src="image.file + ':sm'"
        class="object-cover h-full border border-grey-10 border-t-0 border-r-0 hover:opacity-80 transition duration-100"
        :class="borderRoundClass"
      />
    </router-link>

  </div>
</template>

<script>
export default {
  computed: {
    borderRoundClass() {
      if (this.borderRoundClassProp) {
        return this.borderRoundClassProp
      }

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
    },

    imageTo() {
      if (this.postId) {
        return {name: 'image-from-post', params: {postId: this.postId, imageOrder: this.image.order}}
      } else {
        return {name: 'image-from-search', params: {imageId: this.image.id}}
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
    },
    gridSpan: {
      required: false,
      default: ''
    },
    borderRoundClassProp: {
      required: false,
      default: false,
    }
  }
}
</script>