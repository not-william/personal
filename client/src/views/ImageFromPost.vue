<template>
  <div>
    <app-image-modal
      :image="post.images[imageOrder - 1]"
      :text="post.text"
    />

    <a
      v-if="imageOrder > 1"
      @click.prevent="incrementOrder(-1)"
      href="#"
      class="fixed left-0 z-50 top-1/2 ml-2 opacity-60 hover:opacity-100"
     >
      <img src="@/assets/images/arrow-circle-left-solid.svg" class="w-10"/>
    </a>

    <a
      v-if="imageOrder < post.images.length"
      @click.prevent="incrementOrder(1)"
      href="#"
      class="fixed right-0 z-50 top-1/2 mr-2 opacity-60 hover:opacity-100"
    >
      <img src="@/assets/images/arrow-circle-right-solid.svg" class="w-10"/>
    </a>

    <a
      @click.prevent="showTimeline()"
      href="#"
      class="fixed left-0 z-50 top-0 ml-2 mt-2 opacity-60 hover:opacity-100"
    >
      <img src="@/assets/images/times-circle-solid.svg" class="w-10"/>
    </a>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import AppImageModal from '@/components/AppImageModal'

export default {
  name: 'image-from-post',

  components: {
    'app-image-modal': AppImageModal
  },

  data () {
    return {
      post: null,
      imageOrder: null
    }
  },

  methods: {
    async getPost() {
      let response = await axios.get(`posts/${this.$route.params.postId}`)
      this.post = response.data
    },

    incrementOrder(step) {
      if (this.imageOrder == 1 && step == -1) {
        return
      }
      if (this.imageOrder == this.post.images.length + 1 && step == 1) {
        return
      }
      this.imageOrder += step
      this.$router.push({ name: 'image-from-post', params: { postId: this.post.id, imageOrder: this.imageOrder } })
    },

    showTimeline() {
      this.$router.push({name: 'home'})
    },
  },

  watch: {
    post () {
      const im = []
      im[this.imageOrder] = new Image();
      im[this.imageOrder].src = this.post.images[this.imageOrder - 1].file
      for (let i = 0; i < this.post.images.length; i++) {
        if (i == this.imageOrder - 1) {
          continue
        }
        im[i] = new Image();
        im[i].src = this.post.images[i].file
      }
    }
  },

  mounted () {
    this.imageOrder = parseInt(this.$route.params.imageOrder)
    this.getPost()
    
  }
}
</script>
