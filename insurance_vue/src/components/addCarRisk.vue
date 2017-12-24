<template>
<div class="Risk">
  <h1> enter the information about your car:</h1>
  <form method="post">
    <label>
      <h2> the Date on your Purchase contract </h2> <input type="date" v-model="newCar.attr.date" placeholder="date"/>

      <h2> the car model </h2>
      <input type="text" v-model="newCar.attr.model" placeholder="model"/>

      <h2> the car serial number </h2>
      <input type="number" v-model="newCar.attr.serial_number" placeholder="serial number"/>

      <h2> the car color </h2>
      <input type="color" v-model="newCar.attr.color" placeholder="color"/>

      <h2> the manufacturer</h2>
      <select v-model="newCar.attr.manufacturer" class="selectionclass">
        <option v-for="option in options" v-bind:value="option.value">
          {{ option.text }}
        </option>
      </select>

    </label>
    <br>

    <input type="submit" v-on:click="sendData" class="sub"/>
  </form>
</div>
</template>

<script>
  import axios from 'axios';
  import * as Vue from "vue-resource";
    export default {
      name: "addCarRisk",
      data() {

        return {
          selected: 'A',
          options: [
            {text: 'BMW', value: 'BMW'},
            {text: 'AUDI', value: 'AUDI'},
            {text: 'RangeRover', value: 'RangeRover'},
            {text: 'Kia', value: 'Kia'},
            {text: 'TOYOTA', value: 'TOYOTA'},
            {text: 'INFINITI', value: 'INFINITI'},
            {text: 'JAGUAR', value: 'JAGUAR'},
            {text: 'FORD', value: 'FORD'},
          ],

          newCar:{ riskName: "car", attr: {
              date: "",
              color: "RED",
              model: "",
              manufacturer: "",
              serial_number: ""
            }},
          new:{riskName: "car",
            attributes:{}
          },
          Cars: [],
        }
      },

      methods: {
        sendData: function (e) {
          e.preventDefault();
          var data = this.newCar;
          this.$http.post('http://127.0.0.1:8000/api/insurance/',data)
            .then((response) => {
              console.log("added successfully  ");
            }, (response) => {
              console.log("error  ",this.newCar);
            });
        },
      }
    }
</script>

<style scoped>
  .Risk{
    border-radius: 5px;
    position: relative;
    z-index: 1;
    border-radius: 30px;
    margin-top: -610px;
    margin-left: 40px;
    font-size: 20px;
    font-family:"Agency FB" ;
  }
  .Risk h1{
    color: #ec971f;
  }
  .Risk h2{
    padding: 0px;
    margin-top: 5px;
    margin-bottom: 0px;
  }
  input[type=text],input[type=number],input[type=date], .selectionclass, input[type=submit] {
    width: 30%;
    padding: 10px ;
    margin: 8px 0;
    display: inline-block;
    border: 2px solid #ec971f;
    border-radius: 5px;
    box-sizing: border-box;
    height: 40px;
  }
  .sub{
    background-color: #ec971f;
    color: #122b40;
    margin: 20px;
  }
</style>
