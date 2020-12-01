<template>
  <div class="fixed inset-0 bg-gray-600 flex">
    <div class="mx-auto flex">
      <img 
        :src="'http://localhost:8000' + image.file"
        class="max-h-screen"
      />
      <div style="height: max-content;" class="bg-white p-6 m-3">
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
    }
  }
}
</script>