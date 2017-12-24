<template>
  <div  id="app">

    <div class=" container">

      <agile class="agile" :arrows="false" :speed="750" :dots="false"
             :timing="'linear'" :fade="true"
             :autoplay="true" :pauseOnHover="false">

        <div class="slide slide--1 slide1"></div>
        <div class="slide slide--2 slide2"></div>
        <div class="slide slide--1 slide3"></div>
        <div class="slide slide--2 slide4"></div>
        <div class="slide slide--1 slide5"></div>

      </agile>


      <ul class="navbar">
        <li>
          <router-link to="index" > Home </router-link>
        </li>

        <li>
          <router-link to="viewRisks">view Risks </router-link>
        </li>
        <li>
          <router-link to="#">About us </router-link>
        </li>
      </ul>

      <router-view> </router-view>

    </div>

</div>


</template>

<script>
import index from "./components/index.vue";
import addCarRisk from "./components/addCarRisk"
import viewRisks from "./components/view.vue";
import Dropdown from "hsy-vue-dropdown";


export default {
  name: 'app',
  components: {
    index,viewRisks,addCarRisk
  }
}
</script>

<style>
  body{

    background-repeat: no-repeat;
    background-size:cover ;
    margin: 0;}

  .active{
    background-color: #1b3249;
  }
  .container{
    position: absolute;
    padding: 0px;
    margin: 0px;
    height: 100%;
    width: 100%;


  }
   .navbar {
     position: fixed;

     width:100%;
    top:0px;
    list-style-type: none;
    margin: 0;
    padding-left: 12px;
    overflow: hidden;
    background-color: #122b40;
     opacity: 0.8;
     z-index: 100;
  }

   .navbar li {
     font-family:"Agency FB" ;
     font-size: xx-large;
     float: left;
  }

   .navbar li a {
     display: block;
    color: white;
    text-align: center;
    padding: 15px 20px;
     margin: 0px;
     text-decoration: none;
    font-size: x-large;
  }

  .navbar li a:hover {
    color: #ec971f;
    font-size: 24px;
  }
  .agile {
    &__dots {
      bottom: 0;
      display: none;
      left: 210px;
      position: absolute;
      width: 300px;

    }

    &__dot {
      margin-bottom: 10px;
      display: none;

      button {
        background-color: transparent;
        border: 1px solid #fff;
        margin-top: 10px;
        display: none;

        &:hover {
          background-color: #fff;
        }
      }

      &--current {
        display: none;
        button {

          background-color: #fff;
        }
      }
    }
  }



  .slide {
    position:fixed;
    background-size: cover;
    height:662px;
    width: 100%;
    z-index: -1;
  }

  .slide1 {
    background-image: url("assets/img/1.jpg");
    background-position: center;
  }
  .slide2 {
    background-image: url("assets/img/2.jpg");
    background-position: center;
  }
  .slide3 {
    background-image: url("assets/img/3.jpg");
    background-position: center;
  }
  .slide4 {
    background-image: url("assets/img/4.jpg");

    background-position: center;
  }
  .slide5 {
    background-image: url("assets/img/5.jpg");
  }

</style>
