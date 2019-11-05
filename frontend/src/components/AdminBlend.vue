<template>
  <v-container class="mx-auto">
    <h1>블렌드 상품 관리</h1><v-btn @click="createBlend()">+</v-btn>
    <v-row>
    <v-card
      class="ma-2"
      width="900" v-for="(item, i) in listData" v-bind:key="i">
      <v-col>
      <dis>
        <v-card-text class="text--primary">
          <!-- <p>{{item.id}}</p> -->
          <dis class="left">
            <v-flex v-for="(name,key) in listitems[i]" v-bind:key="key">
              <p style="font-family: 'Noto Serif KR', serif;">{{name.name}} {{listpercents[i][key]}}%</p>
            </v-flex>
          </dis>
        </v-card-text>
        <v-card-subtitle class="pb-0">
          <dis class="right">{{item.content}}</dis>
        </v-card-subtitle>
      </dis>
      <!-- <v-btn color="red lighten-2"
      dark @click="delete_blend(item.id)">delete</v-btn> -->
      <div class="text-center">
        <v-dialog
          v-model="flag_d"
          width="500"
        >
          <v-card>
            <v-card-title
              primary-title>
              배달 정보를 등록해주세요
            </v-card-title>

            <v-form>
             <v-container>
               <v-row>
                 <v-col cols="12" sm="6" md="3">
                   <v-text-field
                     label="년도"
                     v-model="year"
                    ></v-text-field>
                 </v-col>

                 <v-col cols="12" sm="6" md="3">

                   <v-text-field
                     label="월"

                     v-model="month"
                   ></v-text-field>
                 </v-col>

                 <v-col cols="12" sm="6" md="3">

                   <v-text-field
                     label="주 ex)1번째 주"
                     placeholder3=""
                     v-model="weeks"
                   ></v-text-field>
                 </v-col>
               </v-row>
               <p>이달의 블렌드 : </p>
               <v-card color="grey">
                 <p style="font-family: 'Noto Serif KR', serif;">{{blend}}</p>
               </v-card>
             </v-container>
           </v-form>

            <v-divider></v-divider>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="primary"
                text
                @click="flag_d =false"
              >
                취소
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn
                color="primary"
                text
                @click="go_delivery(year,month,weeks)"
              >
                배달 리스트 등록
              </v-btn>
            </v-card-actions>
          </v-card>

        </v-dialog>
        </div>
    </v-col></v-card>
    </v-row>
  </v-container>
</template>
<script>
import axios from 'axios'
import router from "../router"
import Swal from 'sweetalert2';

export default {
  data() {
    return {
      listData: [],
      listitems: [],
      listpercents:[],
      show: false,
      delivery : [],
      flag_d: false,
      blend: '',
      blend_id: 0,
      year: '',
      month: '',
      weeks: '',
    }
  },
  mounted() {
    this.allItem()
  },
  components: {

  },
  methods: {
    allItem() {
      const apiUrl = '/api'
      axios.get(`${apiUrl}/blend/`)
      .then((response) => {
        this.listData = response.data.list;
        // console.log(this.listData)
        this.listitems = response.data.items
        // console.log(response.data.items)
        this.listpercents=response.data.percents
        console.log(response.data)
      });
    },
    createBlend(){
      router.push({name:"createblend"})
    },
    deleteBlend(itemid) {
      const apiUrl = '/api'
      axios.get(`${apiUrl}/blend/delete/${itemid}/`
      ).then(res => {
        alert('블렌드 삭제!')
      })
    }
  }
}
</script>
<style>
  dis {
    width: 100%;
    height: 190px;
  }
  dis.left {
    width: 50%;
    float: left;
  }
  dis.right {
    width: 50%;
    float: right;
  }
</style>
