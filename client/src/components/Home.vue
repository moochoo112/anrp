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
            <th>Kenteken</th>
            <label >{{ items[0].kenteken }}</label>
          </tr>
          <tr>
            <th>Eerste kleur</th>
            <td>{{ items[0].eerste_kleur }}</td>
          </tr>
          <tr>
            <th>Tweede kleur</th>
            <td>{{ items[0].tweede_kleur }}</td>
          </tr>
          <tr>
            <th>Merk</th>
            <td>{{ items[0].merk }}</td>
          </tr>
           <tr>
            <th>Handelsbenaming</th>
            <td>{{ items[0].handelsbenaming }}</td>
          </tr>
           <tr>
            <th>Voertuigsoort</th>
            <td>{{ items[0].voertuigsoort }}</td>
          </tr>
           <tr>
            <th>Inrichting</th>
            <td>{{ items[0].inrichting }}</td>
          </tr>
           <tr>
            <th>Lengte</th>
            <td>{{ items[0].lengte }}</td>
          </tr>
           <tr>
            <th>Vervaldatum apk</th>
            <td>{{ items[0].vervaldatum_apk }}</td>
          </tr>
        </table>
      </div>
      <div class="information__photo">
        <p>Last seen</p>
        <div v-if="items">
          <img id="image" :src="imageUrl"/>
          <table style="width:100%">
            <tr>
              <th>Location</th>
              <td>{{ location }}</td>
            </tr>
            <tr>
              <th>Date</th>
              <td>{{ date }}</td>
            </tr>
            <tr>
              <th>Time</th>
              <td>{{ time }}</td>
            </tr>
          </table>
          <button type="button" class="downloadbtn" @click="download">Download PDF</button>
        </div>
      </div>
    </div>

    <footer class="footer" toggleable="sm" type="light" variant="light">
      <p id="title">Full credits go to Kimberly van Gelder, Cheyen Alberts
      & Jaap van Dalen 😉</p>
    </footer>
    <!-- </b-navbar> -->

  </div>
</template>

<script>
import axios from 'axios';
import JSPDF from 'jspdf';

const doc = new JSPDF();

export default {
  components: {

  },
  data() {
    return {
      licenseplate: '',
      fields: ['kenteken', 'eerste_kleur', 'tweede_kleur', 'kenteken', 'merk', 'handelsbenaming', 'voertuigsoort', 'inrichting', 'lengte', 'vervaldatum_apk'],
      items: null,
      date: null,
      time: null,
      location: null,
      isHidden: false,
      // eslint-disable-next-line global-require
      imageUrl: require('../assets/image-not-found.jpg'),
    };
  },
  methods: {
    download() {
      doc.text(20, 20, `Kenteken: ${this.items[0].kenteken}`);
      doc.text(20, 30, `First colour: ${this.items[0].eerste_kleur}`);
      doc.text(20, 40, `Second colour: ${this.items[0].tweede_kleur}`);
      doc.text(20, 50, `Brand: ${this.items[0].merk}`);
      doc.text(20, 60, `Trade name: ${this.items[0].handelsbenaming}`);
      doc.text(20, 70, `Vehicle type: ${this.items[0].voertuigsoort}`);
      doc.text(20, 80, `Design: ${this.items[0].inrichting}`);
      doc.text(20, 90, `Length: ${this.items[0].lengte}`);
      doc.text(20, 100, `Expiration APK: ${this.items[0].vervaldatum_apk}`);
      doc.addPage();
      doc.addImage(this.imageUrl, 'JPEG', 15, 40, 180, 140);
      doc.text(20, 200, `Date: ${this.date}`);
      doc.text(20, 210, `Time: ${this.time}`);
      doc.text(20, 220, `Location: ${this.location}`);
      doc.save('information.pdf');
    },
    checkImage(kenteken) {
      try {
        // eslint-disable-next-line global-require
        this.imageUrl = require(`../../../server/image/${kenteken}.jpg`); // eslint-disable-line import/no-dynamic-require
      } catch (e) {
        // eslint-disable-next-line global-require
        this.imageUrl = require('../assets/image-not-found.jpg');
      }
    },
    getInfo() {
      const path = `https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken=${this.licenseplate.toUpperCase()}`;
      axios.get(path)
        .then((res) => {
          if (res.data.length === 0) {
            console.log('The data set is empty');
            alert('There is no data found for this numberplate try again');
            window.location.reload();
          } else {
            this.items = res.data;

            this.checkImage(this.items[0].kenteken);
            const payload = { kenteken: this.items[0].kenteken };
            this.getImageInfo(payload);
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getImageInfo(payload) {
      const path = 'http://localhost:5000/';
      axios.post(path, payload)
        .then((res) => {
          const splitData = res.data.split(' ');
          const [, date, time] = splitData.filter((e) => e);
          const [H, M] = time.split(':');
          this.date = date;
          this.time = `${H}:${M}`;
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
  border: none;
  font-size: 32px;
  font-weight: 600;
}
.downloadbtn{
  background-color: #2292AB;
  float: right;
  border: none;
  font-size: 20px;
  font-weight: 600;
  color: white;
  border-radius: 4px;
}
.btn:hover, .downloadbtn:hover{
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
  margin-top: 48px;
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
.information__text p{
  font-size: 32px;
}
.information__text table tr{
  border-bottom: 1px solid #000;
}
.information__photo{
  border-left: 2.5px solid #414141;
  color: #414141 !important;
  font-weight: 600;
  font-size: 20px;
  padding-left: 64px;
  padding-right: 64px;
  width: 50%;
  height: 600.391px;
  padding-bottom: 64px;
}
.information__photo p{
  font-size: 32px;
}
.information__photo img{
  width: 100%;
  border-radius: 8px;
  height: 28vw;
  object-fit: cover;
  border: 1px solid #000;
}

.footer{
  margin-bottom: 0px;
  padding: 8px 64px;
  background-color: #f2f2f2;
  width: 100%;
  font-size: 24px;
  box-shadow: 0px -4px 16px #e0e0e0;
  text-align:center;
}
.footer p{
  margin-bottom: 0px;
}
</style>
