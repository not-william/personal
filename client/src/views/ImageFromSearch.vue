<template>
  <div>
    <app-image-modal
      :image="image"
      :text="image.post"
    />

    <a
      @click.prevent="goBack()"
      href="#"
      class="fixed left-0 z-50 top-0 ml-2 mt-2 opacity-60 hover:opacity-100"
    >
      <img src="@/assets/images/times-circle-solid.svg" class="w-10"/>
    </a>
  </div>
</template>

<script>
import AppImageModal from '@/components/AppImageModal'
import axios from 'axios'

export default {
  name: 'image-from-search',

  components: {
    'app-image-modal': AppImageModal
  },

  data () {
    return {
      image: null,
    }
  },

  methods: {
    goBack() {
      this.$router.go(-1)
      // this.$router.push({name: 'home'})
    }
  },

  async mounted () {
    let response = await axios.get('images/' + this.$route.params["imageId"])

    this.image = response.data
  }
}
</script>
