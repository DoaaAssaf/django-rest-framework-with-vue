<template>
  <div class="Risk">


    <table>
      <tr>
        <th>risk name</th>
        <th>address</th>
        <th>Zip</th>
        <th>space</th>
        <th>floor</th>
        <th>Manufacturer</th>
        <th>Model</th>
        <th>date</th>
        <th>Serial Number</th>
        <th>Color</th>
        <th>amount</th>
        <th>peso</th>

      </tr>
      <tr v-for="ris in risks">
        <td>{{ris.riskName}} </td>
        <td>{{ris.attr.address}}</td>
        <td>{{ris.attr.zip}}</td>
        <td>{{ris.attr.space}}</td>
        <td>{{ris.attr.floor}}</td>
        <td>{{ris.attr.manufacturer}}</td>
        <td>{{ris.attr.model}}</td>
        <td>{{ris.attr.date}}</td>
        <td>{{ris.attr.serial_number}}</td>
        <td>{{ris.attr.color}}</td>
        <td>{{ris.attr.amount}}</td>
        <td>{{ris.attr.peso}}</td>
        <td> </td>
      </tr>
    </table>
  </div>
</template>


<script>
    export default {
      name: "risk",
            created : function () {
        this.$http.get("http://127.0.0.1:8000/api/insurance").then(function (response) {
          this.risks=response.data;
          console.log("this risksss ",this.risks);
          this.risks1 = response.body.entries;
          console.log(response.body.entries);
        });
      },

      data(){
        return {
          risks1:[
          ],
          risks: [
          ]
        }
      }
    }
</script>

<style scoped>

  .Risk{
    background-color: #ec971f;
    width:90% ;
    margin-left: 70px;
    position: relative;
    z-index: 1;
    border-radius: 30px;
    margin-top: -500px;
    font-size: 20px;
    font-family:"Agency FB" ;
  }
 h1{
   color: crimson;
   align-content: center;
 }

  table{
    border-collapse: collapse;
    padding: 10px;
    text-align: center;
    width: 92%;
    margin-left: 50px;
  }

  tr{
    border-bottom: 1px solid #122b40;
    padding:3px ;
    margin-top: 5px;
  }
  tr:hover {background-color:#f5f5f5;}
</style>
