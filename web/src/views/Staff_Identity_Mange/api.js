import { request } from '@/api/service'
export const urlPrefix = 'api/Nucleic_acid_testing/Staff_Model/'

export function GetList(query) {
  return request({
    url: urlPrefix,
    method: 'get',
    params: query
  })
}

export function AddObj(obj) {
  return request({
    url: urlPrefix,
    method: 'post',
    data: obj
  }).then(() =>{
    console.log("人员添加成功")
    request({
      url:urlPrefix,
      method:"post",
      data:{
        "update_datetime": "2022-11-03T06:22:27.562Z",
  "description": "string",
  "modifier": "string",
  "dept_belong_id": "string",
  "is_deleted": false,
  "name": "string",
  "identity": "string",
  "creator": 1
      }
    }).then(() =>{
      console.log("第二个接口调用完成")
    })
  })
}


export function AddObj2(obj) {
  return request({
    url: urlPrefix,
    method: 'post',
    data: {
      
    }
  })
}


export function UpdateObj(obj) {
  return request({
    url: urlPrefix + obj.id + '/',
    method: 'put',
    data: obj
  })
}

export function DelObj(id) {
  return request({
    url: urlPrefix + id + '/',
    method: 'delete',
    data: { id }
  })
}