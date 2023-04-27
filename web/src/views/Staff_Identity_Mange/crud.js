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
                show: false,
                disabled: true,
                width: 90,
                form: {
                    editDisabled: false,
                    disabled: true,
                    rules: [
                        // 表单校验规则
                        { required: false, message: "医院名称必填" }
                    ],
                }
            },
            {
                title: "姓名",
                key: "name",
                sortable: true,
                treeNode: true,

                search: {
                    component: {
                        props: {
                            clearable: true
                        }
                    }
                },
                type: "input",
            },
            {
                title: "身份",
                key: "identity",
                type: "input",
            },
            
        ].concat(vm.commonEndColumns()),
        
        addTemplate:{
            
            name:{
                title:"姓名",
                component:{
                    name:"el-input"
                }
            },
            identity:{
                title:"身份",
                component:{
                    name:"el-input"
                }
            }
        }
        
    };
};