<template>
  <div class="fixed inset-0 bg-gray-600 flex">
    <div class="mx-auto flex flex-wrap">
      <img 
        :src="image.file"
        id="image"
        style="margin-bottom: 10000px;"
        class="max-h-screen object-contain"
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
  mounted () {
    function loaded() {
      var h = imageObj.clientHeight
      const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0)
      console.log(vh)
      console.log(h)
      var margin = (vh - h) / 2
      console.log(margin)
      imageObj.style.marginTop = String(margin) + 'px'
    }

    let imageObj = document.getElementById('image')

    if (imageObj.complete) {
      loaded()
    } else {
      imageObj.addEventListener('load', loaded)
      imageObj.addEventListener('error', function() {
          //
      })
    }

    window.onresize = loaded;
  }
}
</script>
