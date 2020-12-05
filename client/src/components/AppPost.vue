<template>
    <router-link :to="{name: 'image-from-post', params: {postId: post.id, imageOrder: 1}}" class="p-3 transition duration-100 hover:bg-gray-200 text-black min-height-full">
      <div>{{post.text}}</div>
      <div class="grid grid-cols-2 mt-2">
        <app-image 
          v-for="(image, index) in post.images"
          :key="image.id"
          :image="image"
          :postId="post.id"
          :imageOrder="index"
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
  }
}
</script>