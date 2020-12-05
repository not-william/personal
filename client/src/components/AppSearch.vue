<template>
  <form>
    {{images}}
    <input type="text" placeholder='e.g. "wine" or "kyoto"' name="search" v-model="search"/>
  </form>
</template>

<script>
import axios from 'axios'
import _ from 'lodash';

export default {

  data () {
    return {
      search: null,
      images: null,
    }
  },

  watch: {
    search () {
      this.waitSearch()
    } 
  },

  methods: {
    waitSearch: _.debounce(async function () {
      let response = await axios.get('images?search=' + this.search)
      this.images = response.data.results 
    }, 500),

    async searchImages () {
      let response = await axios.get('images?search=' + this.search)
      this.images = response.data.results
    }
  }

}
</script>