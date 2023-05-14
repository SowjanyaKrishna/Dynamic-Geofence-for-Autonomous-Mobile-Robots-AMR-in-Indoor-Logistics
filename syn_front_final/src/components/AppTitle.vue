<template>
  <v-app-bar app clipped-left color="blue lighten-4">
    <v-toolbar-title>Dynamic Geofence App</v-toolbar-title>
    <template v-slot:extension>
      <v-tabs v-model="tab" align-with-title>
        <v-tabs-slider color="red"></v-tabs-slider>
        <v-tab> SpeedRange</v-tab>
        <v-tab-item>
          <SpeedTable />
        </v-tab-item>
        <v-tab> TagDetection </v-tab>
        <v-tab-item>
          <TagDetection />
        </v-tab-item>
        <v-tab> PolygonPlot</v-tab>
        <v-tab-item>
          <PolygonPlot />
        </v-tab-item>
        <v-tab> MqttTopics </v-tab>
        <v-tab-item>
          <MqttTopics />
        </v-tab-item>
      </v-tabs>
    </template>
  </v-app-bar>
</template>


<script>
import SpeedTable from "./SpeedTable";
import TagDetection from "./TagDetection";
import PolygonPlot from "./PolygonPlot";
import MqttTopics from "./MqttTopics";

export default {
  name: "App",

  components: {
    SpeedTable,
    TagDetection,
    PolygonPlot,
    MqttTopics,
  },

  data: () => ({
    tab: null,
  }),
};
</script>

<style scoped>
</style>