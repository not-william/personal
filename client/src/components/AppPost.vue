<template>
    <router-link
      :to="{name: 'image-from-post', params: {postId: post.id, imageOrder: 1}}"
      class="p-3 transition duration-100 hover:bg-gray-200 text-black"
    >
      <div>{{post.text}}</div>
      <div class="grid grid-cols-2 mt-2">
        <app-image 
          v-for="(image, index) in post.images"
          :key="image.id"
          :image="image"
          :postId="post.id"
          :imageOrder="index"
          :gridSpan="gridSpan(index)"
          :borderRoundClassProp="borderClass(index)"
        />
      </div>
    </router-link>
</template>

<script>
import AppImage from '@/components/AppImage'

export default {
  props: {
    post: {
      required: true,
      type: Object
    }
  },

  components: {
    'app-image': AppImage
  },

  methods: {
    gridSpan (index) {
      if (this.post.images.length == 3 && index == 0) {
        return 'row-span-2 h-80'
      }
      if (this.post.images.length == 2) {
        return 'row-span-2 h-80'
      }
      if (this.post.images.length == 1) {
        return 'row-span-2 col-span-2 h-80'
      }
      return 'h-40'
    },
    borderClass (index) {
      if (this.post.images.length == 3) {
        if (index == 0) {
          return 'rounded-tl-xl rounded-bl-xl'
        }
        if (index == 2) {
          return 'rounded-br-xl'
        }
      }
      if (this.post.images.length == 2) {
        if (index == 0) {
          return 'rounded-tl-xl rounded-bl-xl'
        }
        if (index == 1) {
          return 'rounded-tr-xl rounded-br-xl'
        }
      }
      if (this.post.images.length == 1) {
        return 'rounded-xl'
      }
      return false
    }
  }
}
</script>