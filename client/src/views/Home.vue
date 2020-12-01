<template>
  <div>
    <app-search />
    <app-timeline />
  </div>
</template>

<script>
// @ is an alias to /src
import AppTimeline from '@/components/AppTimeline'
import AppSearch from '@/components/AppSearch'

export default {
  name: 'home',
  components: {
    'app-timeline': AppTimeline,
    'app-search': AppSearch
  }
}
</script>
