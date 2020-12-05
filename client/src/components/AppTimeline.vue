<template>
  <div>
    <div class="grid grid-cols-1 md:grid-cols-2">
      <app-post
        v-for="post in posts"
        :key="post.id"
        :post="post"
      />
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import AppPost from '@/components/AppPost'
  // import AppImageModal from '@/components/AppImageModal'

  export default {
    data () {
      return {
        posts: []
      }
    },

    methods: {
      async getPosts() {
        let response = await axios.get('posts/')

        this.posts = response.data.results
      }
    },

    mounted () {
      this.getPosts()
    },

    components: {
      // 'app-image': AppImage
      'app-post': AppPost,
      // 'app-image-modal': AppImageModal,
    }
  }
</script>