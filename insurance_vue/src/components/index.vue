<template>
  <div class="Risk">
      <div class="text">
          <h1> please select the <span>risk type</span>
          <br>from the list below:</h1>
          <div class="select">
               <dropdown  :data="data" :cbChanged="changed"> </dropdown>
          </div>
        </div>
     </div>
</template>


<script>
  import Dropdown from "hsy-vue-dropdown";
  import * as router from "vue-router";
  const data=[{
    label: 'Car',
    value: 1
  }, {
    label: 'House',
    value: 2
  }, {
    label: 'farm',
    value: 3
  }, {
    label: 'church',
    value: 4
  }, {
    label: 'other',
    value: 5
  }];

  export default {

      name: "index",
      data(){
        return {
          selected:0,
          data
        }
      },
    methods: {
      changed: function(selected){
        this.selected = selected[0].value;
        console.log("selected = ",this.selected);
        if (this.selected === 1){
          this.$router.push('addCarRisk');
        }
      }
    }
  }
</script>

<style scoped>
  .Risk{
    position: relative;
    z-index: 1;
    border-radius: 30px;
    margin-top: -500px;
    margin-left: 40px;
    font-size: 20px;
    font-family:"Agency FB" ;
  }

  .select{
    margin-top: 50px;
    opacity: 0.9;
  }

  span{
    color:#ec971f;
    background-color:#1b3249;
    font-stretch: extra-condensed;
  }
</style>
