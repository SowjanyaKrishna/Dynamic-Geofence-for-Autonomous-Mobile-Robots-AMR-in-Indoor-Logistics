<template>
  <div>
    <v-stage ref="stage" :config="stageSize">
      <v-layer>
        <v-btn rounded color="primary" dark> Tag detection </v-btn>
        <v-text :config="configText" />
        <!--Tag data that informs the user position-->
        <v-rect :config="configRect" />
        <!-- Local coordinates that keeps changing every 5 seconds-->
        <v-line :config="configPoly" />
        <!--Global coordinates kept constant for now-->
        <v-line :config="configPolyglobal" />
      </v-layer>
      <v-layer ref="dragLayer"></v-layer>
    </v-stage>
  </div>
</template>

<script>
//import TagDetection from './TagDetection.vue';
import axios from "axios";
const width = window.innerWidth;
const height = window.innerHeight;
export default {
  data() {
    return {
      stageSize: {
        width: width,
        height: height,
      },
      configRect: {
        x: 95,
        y: 140,
        width: 20,
        height: 20,
        fill: "red",
      },
      configText: {
        text: null,
        fontSize: 20,
      },
      configPoly: {
        x: 150,
        y: 200,
        points: [40, 80, -30, 80, -30, -40, 90, -40],
        tension: Math.random(),
        closed: true,
        stroke: "black",
        fillLinearGradientStartPoint: { x: -50, y: -50 },
        fillLinearGradientEndPoint: { x: 50, y: 50 },
        fillLinearGradientColorStops: [0, "yellow", 1, "yellow"],
      },
      configPolyglobal: {
        x: 150,
        y: 200,
        points: [
          70.071067811865476, 110.071067811865476, -60.071067811865475,
          110.071067811865476, -60.071067811865477, -70.071067811865475,
          120.071067811865474, -70.071067811865477,
        ],
        tension: 0.2,
        closed: true,
        stroke: "black",
      },
      co_ordinates: null,
      shrunk_cordinates: null,
      tag_point: null,
    };
  },

  methods: {
    TagDetection() {
      this.configPoly.tension = 0.2;
      let get_ = this;

      this.configRect.x = 95;
      let get_x = this;

      this.configRect.y = 40;
      let get_y = this;

      this.configText.text = "";
      let get_text = this;

      axios.get("/api/TagDetection").then((result) => {
        this.action = result.data.warning;
        this.converted_co_ordinates = result.data.co_ordinates;
        this.safezone = result.data.shrunk_cordinates;
        this.tag = result.data.tag_point;
      });
      setInterval(function () {
        //this.configPoly.points = this.converted_co_ordinates;
        get_.configPoly.tension = Math.random();
        get_x.configRect.x = Math.random() * width;
        get_y.configRect.y = Math.random() * height;
        //get_text.configText.text = this.action;
        get_text.configText.text = Math.random().toString(36).slice(2)
        console.log(get_.configPoly.tension), console.log("data");
      }, 1000);
    },
  },
  beforeMount() {
    this.TagDetection();
  },
};
</script>
