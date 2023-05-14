<template>
  <div>
    <v-data-table
      v-model="selected"
      :headers="headers"
      :items="Id"
      :items-per-page="10"
      :single-select="singleSelect"
      @input="rowselection()"
      show-select
      item-key="id"
      sort-by="id"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>MQTT Table</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
                New Item
              </v-btn>
              <v-switch
                v-model="singleSelect"
                label="Single select"
                class="pa-3"
              ></v-switch>
            </template>

            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.AGVName"
                        label="AGVName"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.AGVTopic"
                        label="AGVTpoic"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.GeofenceId"
                        label="GeofenceId"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.NaiseTag"
                        label="NaiseTag"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.id"
                        label="id"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">
                  Cancel
                </v-btn>
                <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5"
                >Are you sure you want to delete this item?</v-card-title
              >
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDelete"
                  >Cancel</v-btn
                >
                <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                  >OK</v-btn
                >
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>

      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
        <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize"> Reset </v-btn>
      </template>
    </v-data-table>
    <v-card>
        <div class="text-right">
            <v-btn v-on:click="Connect()" rounded color="success" dark>
                Connect
            </v-btn>
        </div>
    </v-card>
  </div>
</template>



<script>
import axios from "axios";

export default {
  data: () => ({
    action: null,
    dialog: false,
    dialogDelete: false,
    singleSelect: true,
    headers: [
      {
        text: "Id",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "AGVName", value: "AGVName" },
      { text: "AGVTopic", value: "AGVTopic" },
      { text: "GeofenceId", value: "GeofenceId" },
      { text: "NaiseTag", value: "NaiseTag" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    Id: [],
    selected: [],

    editedIndex: -1,
    editedItem: {
      id: 0,
      AGVName: '',
      AGVTopic: '',
      GeofenceId: '',
      NaiseTag: '',
      
    },
    defaultItem: {
      id: 0,
      AGVName: '',
      AGVTopic: '',
      GeofenceId: '',
      NaiseTag: '',
    
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },
    msg() {
      const selectedRow = this.selected[0];
      return selectedRow
        ? `${selectedRow.id} ${selectedRow.AGVName} ${selectedRow.GeofenceId} ${selectedRow.NaiseTag}`
        : "no data selected";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  created() {
    this.initialize();
  },

  methods: {
    initialize() {
      axios
        .get("/api/getMqttTabledata")
        .then((result) => {
          console.log(result.data);
          this.Id = result.data;
          console.log(this.Id);
        })
        .catch(console.error);
    },

    editItem(item) {
      this.editedIndex = this.Id.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    rowselection() {
      let data = {
        clickedid: this.selected.map((e) => e.id),
      };
      console.log(data);
      console.log(this.selected.map((e) => e.id));
      axios.post("/api/mqttselectedrow", data);
    },

    deleteItem(item) {
      this.editedIndex = this.Id.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      this.Id.splice(this.editedIndex, 1);
      this.closeDelete();

      axios
        .delete("/api/deletemqtt/"+this.editedItem.id)
        .then((response) => (this.message = response.data))
        .catch.log(console.error);
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    editsave() {
      console.log("Being edited");
      let data2 = {
        id: this.editedItem.id,
        AGVName: this.editedItem.AGVName,
        AGVTopic: this.editedItem.AGVTopic,
        GeofenceId: this.editedItem.GeofenceId,
        NaiseTag: this.editedItem.NaiseTag,
      };
      console.log("data2", data2);
      axios
        .put("/api/editmqtt", data2)
        .then((response) => (this.message = response.data))
        .catch.log(console.error);
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.Id[this.editedIndex], this.editedItem);
        this.close();
        this.editsave();
      } else {
        this.Id.push(this.editedItem);
        this.close();
        console.log("Being clicked");
        let data2 = {
          id: this.editedItem.id,
          AGVName: this.editedItem.AGVName,
          AGVTopic: this.editedItem.AGVTopic,
          GeofenceId: this.editedItem.GeofenceId,
          NaiseTag: this.editedItem.NaiseTag,
        };
        console.log(data2);
        axios
          .post("/api/tablemqtt", data2)
          .then((response) => (this.message = response.data))
          .catch(console.error);
      }
    },
    Connect()
    {
      console.log("Being clicked");
      let hello = {

      };
      console.log(hello);
      axios
        .post("/api/Connect", hello)
        .then((response) => {
          (this.message = response.hello)
        })
        .catch(console.error);
    },
  },
};
</script>

<style>
.my-img {
  width: 30%;
}
.my-field {
  width: 20%;
}
</style>