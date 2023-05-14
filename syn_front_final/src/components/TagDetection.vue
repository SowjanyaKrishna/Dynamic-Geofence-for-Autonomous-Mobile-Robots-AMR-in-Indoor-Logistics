<template>
  <v-card ref="stage" :config="stageSize">
    <div class="text-left">
      <v-btn v-on:click="TagDetection()" rounded color="primary" dark>
        Tag detection
      </v-btn>
      <v-spacer></v-spacer>
      <v-alert type="warning"> {{ action }} </v-alert>
    </div>
    <v-card>
      <div class="center">
        <v-spacer></v-spacer>
        <v-text-field
          v-model="zoneoffset"
          label="Zone Offset percentage"
          placeholder="Enter float value"
          class="my-field"
        ></v-text-field>
        <v-spacer></v-spacer>
        <v-btn
          id="test"
          v-on:click="OffsetPercentage()"
          rounded
          color="primary"
          dark
        >
          Save
        </v-btn>
      </div>
    </v-card>
    <v-card>

    </v-card>
    <v-spacer></v-spacer>
  </v-card>
</template>

<script>
import axios from "axios";
var width = window.innerWidth;
var height = window.innerHeight;

export default {
  data: () => ({
    zoneoffset: 0,
    img_src: null,
    action: null,
    co_ordinates: null,
    shrunk_cordinates: null,
    tag_point: null,
    container: "container",
    stageSize: {
      width: width,
      height: height,
    },
  }),

  methods: {
    TagDetection() {
      
      this.co_ordinates = 10;
      let get_= this;

      this.shrunk_cordinates = 100;
      let shrunk_ = this;

      this.tag_point = 5;
      let tag_ = this;

      axios.get("/api/TagDetection").then((result) => {
        this.action = result.data.warning;
        /*this.action = result.data.co_ordinates;
          this.action = result.data.shrunk_cordinates;
          this.action = result.data.tag_point;*/
      });
      setInterval(function () {
        get_.co_ordinates = Math.random() * 10
        console.log(get_.co_ordinates)

        shrunk_.shrunk_cordinates = Math.random() * 100
        console.log("SHRUNK", shrunk_.shrunk_cordinates)

        tag_.tag_point = Math.random() * 5
        console.log("TAG", tag_.tag_point)
      }, 1000);
      
    },

    OffsetPercentage() {
      let data = {
        zoneoffset: this.zoneoffset,
      };
      console.log(data);
      axios
        .post("/api/getZoneOffset", data)
        .then((response) => (this.message = response.data))
        .catch(console.error);

      setTimeout(function () {
        const elem = document.getElementById("test");
        elem.click();
      }, 5000);
    },
  },
};
</script>

<style></style>
