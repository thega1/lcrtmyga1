<template>
  <div>
    <el-card class="card">
      <el-input placeholder="请输入疫情等级(1-10)" class="input"></el-input>
      <el-button @click="open" class="button">提交</el-button>
    </el-card>
  </div>
</template>

<script>
export default{
  data(){
    return{

    }
  },
  methods:{
    open() {
      this.$alert('提交成功', '提示', {
        confirmButtonText: '确定',
      }).then(() =>{
        console.log("chneggong")
      });
    }
  }
}

</script>

<style lang="scss">
.card{
  width: 60%;
  height: 200px;
  margin-top: 10%;
  margin-left: 20%;

}
.input{
  margin-top: 10%;
  margin-left: 10%;
  width: 60%;
}
.button{
  margin-left: 30px;
}
</style>
