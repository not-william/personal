<template>
  <div class="px-3">
    <div class="m-5 mb-0 float-right">
      <form>
        <label for="search">
          <img src="@/assets/images/search-solid.svg" class="h-5 inline opacity-60 mb-1 mr-2" />
        </label>
        <input class="p-2 pr-9 text-md inline" type="text" placeholder='e.g. "wine" or "kyoto"' name="search" id="search" v-model="searchString" @keydown.enter.prevent/>
        <a v-if="searchString" href="#" @click.prevent="searchString=''">
          <img src="@/assets/images/times-circle-solid.svg" class="h-5 inline opacity-60 mb-1 relative right-7 hover:opacity:80" />
        </a>
      </form>
    </div>
    <div class="clear-both"></div>
    <app-timeline v-if="!images && !fromRoute"/>
    <app-timeline-search :images="images" :search="search" v-if="images" />
  </div>
</template>

<script>
// @ is an alias to /src
import AppTimeline from '@/components/AppTimeline'
import axios from 'axios'
import _ from 'lodash'
import AppTimelineSearch from '../components/AppTimelineSearch.vue'

export default {
  name: 'home',
  components: {
    'app-timeline': AppTimeline,
    'app-timeline-search': AppTimelineSearch,
  },

  data () {
    return {
      search: null,
      searchString: null,
      images: null,
      fromRoute: false,
    }
  },

  watch: {
    searchString () {
      if (this.searchString.length > 0) {
        this.waitSearch()
      } else {
        this.images = null
      }
    } 
  },

  methods: {
    waitSearch: _.debounce(async function () {
      if (this.fromRoute) {
        this.fromRoute = false
        return
      }
      this.search = this.searchString
      this.$router.push({ name: 'search', params: { 'search': this.search } })
      this.searchImages()
    }, 500),

    async searchImages () {
      let response = await axios.get('images?search=' + this.search)
      if (this.searchString.length > 0) {
        this.images = response.data.results
      }
    }
  },

  beforeMount () {
    if (this.$route.params.search) {
      console.log("before mount")
      this.fromRoute = true
      this.searchString = this.$route.params.search
      this.search = this.$route.params.search 
      this.searchImages()
    }
  }
}
</script>
