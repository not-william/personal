<template>
  <div class="fixed inset-0 bg-gray-600 flex">
    <div class="mx-auto flex flex-wrap">
      <img 
        :src="image.file"
        id="image"
        style="margin-bottom: 10000px;"
        class="max-h-screen inline object-contain"
      />
      <div style="height: max-content;" class="bg-white inline p-6 mt-3 ml-3">
        <div v-if="text" class="mb-4 text-lg">
          {{ text }}
        </div>
        <div v-if="image.location" class="flex mb-4 text-gray-800">
          <img src="@/assets/images/map-marker-alt-solid.svg" class="h-5 mr-2 opacity-80" style="margin-top: 2px;"/>
          {{ image.location }}
        </div>
        <div v-if="image.f_number" class="flex mb-2 text-gray-600 text-sm">
          <img src="@/assets/images/aperture.svg" class="h-4 mr-2 opacity-80" style="margin-top: 2px;"/>
          1/{{ image.f_number }}
        </div>
        <div v-if="image.shutter_speed" class="flex mb-2 text-gray-600 text-sm">
          <img src="@/assets/images/stopwatch.svg" class="h-4 mr-2 opacity-80" style="margin-top: 2px;"/>
          1/{{ image.shutter_speed }}s
        </div>
        <div v-if="image.focal_length" class="flex mb-2 text-gray-600 text-sm">
          <img src="@/assets/images/camera-lens.svg" class="h-4 mr-2 opacity-80" style="margin-top: 2px;"/>
          {{ image.focal_length }}mm
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      imgLoaded: false
    }
  },
  props: {
    image: {
      required: true,
      type: Object
    },
    text: {
      required: false,
    },
    search: {
      required: false,
      default: false,
    },
  },

  methods: {
    loaded () {
      this.imgLoaded = true
      var h = this.imageObj.clientHeight
      const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0)
      var margin = (vh - h) / 2
      this.imageObj.style.marginTop = String(margin) + 'px'
    }
  },
  mounted () {
    this.imageObj = document.getElementById('image')

    if (this.imageObj.complete) {
      this.loaded()
    } else {
      this.imageObj.addEventListener('load', this.loaded)
      this.imageObj.addEventListener('error', function() {
          //
      })
    }

    window.onresize = this.loaded;
  }
}
</script>
