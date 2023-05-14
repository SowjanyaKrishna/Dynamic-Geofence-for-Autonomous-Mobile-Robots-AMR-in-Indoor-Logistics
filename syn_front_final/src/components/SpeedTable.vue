<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="Range"
      sort-by="id"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Speed Range Table</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
                New Item
              </v-btn>
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
                        v-model="editedItem.upperlimit"
                        label="upperlimit"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.lowerlimit"
                        label="lowerlimit"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.offset"
                        label="Offset"
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
        <v-btn v-on:click="Clearspeedrangetable()" rounded color="primary" dark>
          Clear SpeedTable in Db
        </v-btn>
      </div>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: "Id",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "UpperLimit", value: "upperlimit" },
      { text: "LowerLimit", value: "lowerlimit" },
      { text: "OffsetValue", value: "offset" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    Range: [],
    editedIndex: -1,
    editedItem: {
      id: 0,
      upperlimit: 0,
      lowerlimit: 0,
      offset: 0,
    },
    defaultItem: {
      id: 0,
      upperlimit: 0,
      lowerlimit: 0,
      offset: 0,
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
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
        .get("/api/getSpeedTabledata")
        .then((result) => {
          console.log(result.data);
          this.Range = result.data;
          console.log(this.Range);
        })
        .catch(console.error);
    },

    editItem(item) {
      this.editedIndex = this.Range.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.Range.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      this.Range.splice(this.editedIndex, 1);
      this.closeDelete();

      axios
        .delete("/api/deletespeed/"+this.editedItem.id)
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
    
   editsave(){
      console.log("Being edited");
       let data1 = {
        id: this.editedItem.id,
        upperlimit: this.editedItem.upperlimit,
        lowerlimit: this.editedItem.lowerlimit,
        offset: this.editedItem.offset,
      }; 
      console.log("data1",data1);
        axios
        .put("/api/editspeed",data1)
        .then((response) => (this.message = response.data))
        .catch.log(console.error);
    },

    save() {

      if (this.editedIndex > -1) {
        Object.assign(this.Range[this.editedIndex], this.editedItem);
        this.close();
        this.editsave();  
      } 
      else {
        this.Range.push(this.editedItem);
        this.close();
        console.log("Being clicked");
        let data = {
        id: this.editedItem.id,
        upperlimit: this.editedItem.upperlimit,
        lowerlimit: this.editedItem.lowerlimit,
        offset: this.editedItem.offset,
      }; 
        console.log(data);
        axios
          .post("/api/addspeeddata", data)
          .then((response) => (this.message = response.data))
          .catch(console.error);
          
      }
      
    },

    Clearspeedrangetable() {
      axios
        .get("/api/Clearspeedrangetable")
        .then((result) => {
          this.message = result.data.message;
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
</style>