import { request } from '@/api/service'
export const urlPrefix = 'api/Nucleic_acid_testing/Emergency_dispatch_Need_ModelView/'
// 核酸检测点信息表接口(feiqi)
export const Message = 'api/Nucleic_acid_testing/Points_Message_Model'
// 模型接口
export const Moxing = 'api/Nucleic_acid_testing/Points_Message_Model'
// 核酸检测点原信息接口
export const point_message = 'api/point_message'


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
// 上面四个没有用

// 获取原有核酸检测点信息
export function Get_Point(query) {
  return request({
    url: point_message,
    method: 'get',
    params: query
  })
}

// 向模型发送数据
export function Start_Forecast(query) {
  return request({
    url: Moxing,
    method: 'post',
    params: query
  })
}

// 获取预测结果
export function Get_Result(query) {
  return request({
    url: Moxing,
    method: 'get',
    params: query
  })
}