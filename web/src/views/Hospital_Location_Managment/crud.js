import { request } from "@/api/service";
import { BUTTON_STATUS_NUMBER } from "@/config/button";
import { urlPrefix as bookPrefix } from "./api";


export const crudOptions = vm => {
    return {
        pageOptions: {
            compact: true
        },
        options: {
            tableType: "vxe-table",
            rowKey: false, // 必须设置，true or false
            rowId: "id",
            height: "100%", // 表格高度100%, 使用toolbar必须设置
            highlightCurrentRow: false
        },
        rowHandle: {
            width: 140,
            view: {
                thin: true,
                text: "",
                disabled:false
            },
            edit: {
                thin: true,
                text: "",
                disabled:false
            },
            remove: {
                thin: true,
                text: "",
                disabled:false
            }
        },
        indexRow: {
            // 或者直接传true,不显示title，不居中
            title: "序号",
            align: "center",
            width: 100
        },
        viewOptions: {
            componentType: "form"
        },
        formOptions: {
            defaultSpan: 24, // 默认的表单 span
            width: "35%"
        },
        columns: [{
                title: "ID",
                key: "id",
                show: true,
                disabled: true,
                width: 90,
                form: {
                    disabled: true
                }
            },
            {
                title: "医院名称",
                key: "name",
                type: "input",
                search: {
                    component: {
                        props: {
                            clearable: true
                        }
                    }
                },
            },
            {
                title: "经度",
                key: "jingdu",
                type: "input",
            },
            {
                title: "纬度",
                key: "weidu",
                type: "input",
            },
        ].concat(vm.commonEndColumns()),
        editTemplate:{
            jingdu:{
                title:"经度",
                component:{
                    name:"el-input"
                }
            },
            weidu:{
                title:"纬度",
                component:{
                    name:"el-input"
                }
            }
        }
    };
};