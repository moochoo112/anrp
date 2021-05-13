<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1 class="titleHome">Automatic Number Plate Recognition System</h1>
      </div>
    </div>
      <b-form-input id="licenseplate" class="licenseplate" v-model="licenseplate" maxlength="6" >
      </b-form-input>

    <button type="button" class="btn btn-primary" @click="getInfo">Volgende</button>

    <b-table v-show="isHidden" class="table" :items="items" :fields="fields"></b-table>
  </div>

</template>

<script>
import axios from 'axios';

export default {
  components: {

  },
  data() {
    return {
      licenseplate: '',
      fields: ['kenteken', 'eerste_kleur', 'tweede_kleur', 'kenteken', 'merk', 'handelsbenaming', 'voertuigsoort', 'inrichting', 'lengte', 'vervaldatum_apk'],
      items: [],
      isHidden: false,
    };
  },
  methods: {
    test() {
      alert(this.licenseplate);
    },
    getInfo() {
      const path = `https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken=${this.licenseplate.toUpperCase()}`;
      axios.get(path)
        .then((res) => {
          this.items = res.data;
          this.isHidden = true;
          console.log(res.data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getImages() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then(() => { })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getImages();
  },
};
</script>
<style>
.titleHome{
    text-align:center;
    font-family: "Courier New", monospace;
    font-size: 4vw;
    margin-bottom: 5vw;
    color: #004682;
  }.btn{
    background-color: #004682;
    float: right;
    font-size: 1.5vw;
  }
  .table{
    margin-top: 10vw;
  }
  .licenseplate {
  color: #333;
  background-color: #fff;
  background-image: url('~@/assets/nl.png');
  background-repeat: no-repeat;
  background-size: contain, cover;

  font-family: 'Segoe UI', Arial, sans-serif;
  font-size: 100px;
  line-height: 110px;
  font-weight: bold;
  text-transform: uppercase;
  text-align: center;

  padding-left: 60px;
  padding-bottom: 10px;

  width: 510px;
  border: 5px solid red;
  border-radius: 15px;
  outline: none;
  margin-left: 20%;

}
</style>
