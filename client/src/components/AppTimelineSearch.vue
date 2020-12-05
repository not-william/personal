<template>
  <div class="p-5">
    <div class="text-lg mb-2">Results for <i class="ml-1">{{search}}</i></div>
    <div 
      v-if="images.length > 0"
      class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4"
    >
      <app-image
        v-for="image in images"
        :key="image.id"
        :image="image"
        :search="true"
        class="mr-1 mb-1"
      />
    </div>
    <div v-if="images.length == 0">
      No results
    </div>
  </div>
</template>

<script>
  import AppImage from '@/components/AppImage'
  // import AppImageModal from '@/components/AppImageModal'

  export default {
    props: {
      images: {
        required: true,
      },
      search: {
        required: true
      }
    },


    components: {
      'app-image': AppImage
    }
  }
</script>