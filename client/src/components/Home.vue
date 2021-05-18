<template>
  <div>
    <b-navbar class="navbar" toggleable="sm" type="light" variant="light">
        <b-nav-text id="title">Kichja</b-nav-text>
        <b-nav-text>ANPR</b-nav-text>
    </b-navbar>
    <!-- </b-navbar> -->

    <div class="container">
      <b-form-text>Enter dutch numberplate</b-form-text>
      <b-form-input id="licenseplate" class="licenseplate" v-model="licenseplate" maxlength="6" >
      </b-form-input>
      <button type="button" class="btn btn-primary" @click="getInfo">Check plate</button>
    </div>
    <!-- </b-container> -->

    <hr>

    <div class="information">
      <div class="information__text">
        <p>Information</p>
        <table v-if="items" style="width:100%">
          <tr>
            <th>kenteken</th>
            <label >{{ items[0].kenteken }}</label>
          </tr>
          <tr>
            <th>eerste_kleur</th>
            <td>{{ items[0].eerste_kleur }}</td>
          </tr>
          <tr>
            <th>tweede_kleur</th>
            <td>{{ items[0].tweede_kleur }}</td>
          </tr>
          <tr>
            <th>merk</th>
            <td>{{ items[0].merk }}</td>
          </tr>
           <tr>
            <th>handelsbenaming</th>
            <td>{{ items[0].handelsbenaming }}</td>
          </tr>
           <tr>
            <th>voertuigsoort</th>
            <td>{{ items[0].voertuigsoort }}</td>
          </tr>
           <tr>
            <th>inrichting</th>
            <td>{{ items[0].inrichting }}</td>
          </tr>
           <tr>
            <th>lengte</th>
            <td>{{ items[0].lengte }}</td>
          </tr>
           <tr>
            <th>vervaldatum_apk</th>
            <td>{{ items[0].vervaldatum_apk }}</td>
          </tr>
        </table>
      </div>
      <div class="information__photo">
        <p>Last seen</p>
        <img src="https://static.autoblog.nl/images/wp2017/rijksweg-combo-31.jpg" alt="auto">
        <table style="width:100%">
          <tr>
            <th>Location</th>
            <td>Egmond</td>
          </tr>
          <tr>
            <th>Date</th>
            <td>2 january 2021</td>
          </tr>
          <tr>
            <th>Time</th>
            <td>13:21</td>
          </tr>
        </table>
      </div>
    </div>

    <div class="footer" toggleable="sm" type="light" variant="light">
      <b-footer-text id="title">Full credits go to Kimberly van Gelder, Cheyen Alberts
      & Jaap van Dalen 😉</b-footer-text>
    </div>
    <!-- </b-navbar> -->

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
      items: null,
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
          console.log(this.items[0].kenteken);
          this.isHidden = true;
          console.log(res.data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {

  },
};
</script>
<style>
.navbar{
  font-size: 32px;
  background-color: #F2F2F2;
  box-shadow: 0px 4px 16px #616161;
  margin-bottom: 64px;
}
.navbar #title{
  color: #414141;
  font-weight: 700;
  margin-right: 16px;
}
.navbar .navbar-text{
  color: #2292AB;
  font-weight: 400;
}

.container{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.container .form-text{
  color: #414141 !important;
  font-weight: 600;
  margin-right: 16px;
  font-size: 32px;
  margin-bottom: 16px;
}

.titleHome{
  text-align:center;
  font-family: "Courier New", monospace;
  font-size: 4vw;
  margin-bottom: 5vw;
  color: #004682;
}
.btn{
  background-color: #2292AB;
  float: center;
  font-size: 1.5vw;
  border: none;
  font-size: 32px;
  font-weight: 600;
}
.btn:hover{
  background-color: #1c788c;
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
  margin-bottom: 16px;

  width: 510px;
  border: 5px solid red;
  border-radius: 15px;
  outline: none;
}

hr{
  background-color: #414141;
  height: 1px;
  margin-bottom: 0;
}

.information{
  display: flex;
  align-items: stretch;
  justify-content: space-between;
}
.information__text{
  color: #414141 !important;
  font-weight: 600;
  margin-right: 16px;
  font-size: 20px;
  margin-bottom: 16px;
  padding-left: 64px;
  padding-right: 64px;
  width: 50%;
}
.information__photo{
  border-left: 2px solid #414141;
  color: #414141 !important;
  font-weight: 600;
  font-size: 20px;
  margin-bottom: 16px;
  padding-left: 64px;
  padding-right: 64px;
  width: 50%;
}
.information__photo img{
  width: 100%;
  border-radius: 8px;
  height: 28vw;
  object-fit: cover;
  border: 1px solid #000;
}

.footer{
  margin-top: 64px;
  margin-bottom: 0px;
  padding: 8px 64px;
  background-color: #f2f2f2;
  width: 100%;
  font-size: 24px;
  box-shadow: 0px -4px 16px #e0e0e0;
}
</style>
