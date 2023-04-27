<template>
  <baidu-map
  :center="center"
  :zoom="zoom"
  class="bm-view"
  :scroll-wheel-zoom="true"
  @ready="handler"
>
<el-button @click="open">点我开始预测</el-button>
  <bm-marker v-for="(item,index) in positionArr" :key="index" :position="item.markerPoint" :dragging="false"  @click="infoWindowOpen(index)">
    <bm-info-window
      :show="item.show"
      @close="infoWindowClose(index)"
      @open="infoWindowOpen(index)"
    >{{ item.name }}</bm-info-window>
  </bm-marker>
  <!-- 117.544668,34.906942 -->
  <!-- 缩放控件 -->
  <bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>
  <!-- 城市切换 -->
  <bm-city-list anchor="BMAP_ANCHOR_TOP_LEFT"></bm-city-list>
  <!-- 地图定位 -->
  <bm-geolocation anchor="BMAP_ANCHOR_BOTTOM_RIGHT" :showAddressBar="true" :autoLocation="true"></bm-geolocation>
</baidu-map>
</template>

<script>
import BaiduMap from 'vue-baidu-map/components/map/Map.vue'
import { crudOptions } from './crud' // 上文的crudOptions配置
import { d2CrudPlus } from 'd2-crud-plus'
import { AddObj, GetList, UpdateObj, DelObj,Get_Point,Start_Forecast,Get_Result } from './api' // 查询添加修改删除的http请求接口
export default {
components: {
  BaiduMap
},
data() {
  return {
    center: { lng: 117.544668, lat: 34.906942 }, // 地图的中心
    zoom: 15, // 缩放倍数
    // 后期获取后端传来的数组（未完成）
    positionArr: [
      {
        name: '我是核酸站点1', // 弹框内容
        show: true, // 控制是否展示
        markerPoint: {
          lng: 117.544660, lat: 34.906948 // 你想要的标记地点 推荐用这个官方拾取器 http://api.map.baidu.com/lbsapi/getpoint/index.html 
        }
      },
      {
        name: '我是核酸站点2', // 弹框内容
        show: true, // 控制是否展示
        markerPoint: {
          lng: 117.544650, lat: 34.906950 // 你想要的标记地点 推荐用这个官方拾取器 http://api.map.baidu.com/lbsapi/getpoint/index.html 
        }
      },
    ],
  }
},
methods: {
  handler({ BMap, map }) {
    this.center.lng = 117.544668
    this.center.lat = 34.906942
    this.zoom = 15
  },
  infoWindowClose(index) {
    this.positionArr[index].show = false
  },
  infoWindowOpen(index) {
    this.positionArr[index].show = true
  },
  getPostion(){
    request({
        url: urlPrefix,
        method: 'get',
        params: query
    })
  },
  open() {
      this.$alert('预测提交成功', '提示', {
        confirmButtonText: '确定',
      }).then(() =>{
        let result = Get_Result()
        result.then(res=>{
          this.positionArr = res['data']
          console.log("我是最后结果",res.data)
          console.log("我是赋值结果",this.positionArr)
        })
      });
    }
},
mounted(){
  let result = Get_Point()
        result.then(res=>{
          this.positionArr = res['data']
          console.log("create最后结果",res.data)
          console.log("create赋值结果",this.positionArr)
        })
  console.log("我是生命周期函数")
}
}

</script>

<style>
.bm-view {
width: 100%;
height: 80%;
}
</style>

