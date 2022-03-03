import{u as E,B as w,v as h}from"./handleArray.ba308474.js";import{r as C}from"./index.46b49780.js";import{d as S,R as i,g as _,r as F,o as V,c as x,w as d,j as e,k as t}from"./vendor.3998f262.js";const I=S({setup(q){const B=E(),g=i({icon:"cascades",zhName:"\u9662\u7CFB\u8868",enName:"department"}),l=i({deptData:[],pageTotal:0,isDisabled:!1,isShowSearched:!1}),p=i({id:"",currentPage:1,pageSize:10}),o=i({id:"",name:"",chairman:"",phone:""}),D=i({id:[{required:"true",trigger:"change",message:"\u8BF7\u8F93\u5165\u9662\u7CFB\u7F16\u53F7"},{pattern:/^10/,message:"\u9662\u7CFB\u7F16\u53F7\u8981\u4EE510\u5F00\u5934"},{min:4,max:4,message:"\u9662\u7CFB\u7F16\u53F7\u7684\u957F\u5EA6\u5E94\u4E3A4"},{pattern:/^10[0-9]{2}$/,message:"\u9662\u7CFB\u7F16\u53F7\u5FC5\u987B\u662F\u6B63\u6574\u6570"},{validator:(r,u,a)=>{let n=h(B.departmentData,"id");!l.isDisabled&&n.indexOf(u)!=-1?a(new Error("\u9662\u7CFB\u7F16\u53F7\u5DF2\u7ECF\u5B58\u5728")):a()}}],name:[{required:"true",message:"\u8BF7\u8F93\u5165\u9662\u7CFB\u540D\u79F0",trigger:["change","blur"]},{validator:(r,u,a)=>{let n=h(B.departmentData,"name");!l.isDisabled&&n.indexOf(u)!=-1?a(new Error("\u9662\u7CFB\u540D\u5B57\u5DF2\u7ECF\u5B58\u5728")):a()}}],chairman:[{required:"true",message:"\u8BF7\u8F93\u5165\u9662\u7CFB\u4E3B\u4EFB\u540D",trigger:["change","blur"]}],phone:[{pattern:/^((0\d{2,3}-\d{7,8})|(1[34578]\d{9}))$/,message:"\u8BF7\u8F93\u5165\u6B63\u786E\u7684\u624B\u673A\u53F7",trigger:["change","blur"]}]}),c=async(r=p.currentPage)=>{let u={path:g.enName,pageIndex:r,pageSize:p.pageSize};const{data:a}=await C(u);l.deptData=a.dataList,l.pageTotal=a.count};_(()=>c());const f=r=>l.isDisabled=r,b=r=>l.isShowSearched=r;return(r,u)=>{const a=F("el-table-column"),n=F("el-input"),m=F("el-form-item");return V(),x(w,{page:e(g),query:e(p),data:e(l).deptData,"page-total":e(l).pageTotal,"form-data":e(o),"form-rules":e(D),"get-data":c,onEmitIsDisabled:f,onEmitIsShowSearched:b},{filter:d(()=>[]),tableColumn:d(()=>[t(a,{prop:"id",label:"\u9662\u7CFB\u7F16\u53F7",width:"140",align:"center",sortable:!e(l).isShowSearched,"sort-orders":["ascending","descending"]},null,8,["sortable"]),t(a,{prop:"name",label:"\u9662\u7CFB\u540D\u5B57",width:"220",align:"center"}),t(a,{prop:"chairman",label:"\u4E3B\u4EFB\u540D",width:"140",align:"center"}),t(a,{prop:"phone",label:"\u4E3B\u4EFB\u624B\u673A\u53F7",width:"180",align:"center"})]),showDialog:d(()=>[t(m,{label:"\u9662\u7CFB\u7F16\u53F7",prop:"id"},{default:d(()=>[t(n,{modelValue:e(o).id,"onUpdate:modelValue":u[0]||(u[0]=s=>e(o).id=s),placeholder:"\u8BF7\u8F93\u5165\u7F16\u53F7",maxlength:"4","show-word-limit":"",disabled:e(l).isDisabled},null,8,["modelValue","disabled"])]),_:1}),t(m,{label:"\u9662\u7CFB\u540D\u5B57",prop:"name"},{default:d(()=>[t(n,{modelValue:e(o).name,"onUpdate:modelValue":u[1]||(u[1]=s=>e(o).name=s),placeholder:"\u8BF7\u8F93\u5165\u540D\u5B57",maxlength:"20","show-word-limit":""},null,8,["modelValue"])]),_:1}),t(m,{label:"\u4E3B\u4EFB\u540D",prop:"chairman"},{default:d(()=>[t(n,{modelValue:e(o).chairman,"onUpdate:modelValue":u[2]||(u[2]=s=>e(o).chairman=s),placeholder:"\u8BF7\u8F93\u5165\u4E3B\u4EFB\u540D",maxlength:"10","show-word-limit":""},null,8,["modelValue"])]),_:1}),t(m,{label:"\u4E3B\u4EFB\u624B\u673A\u53F7",prop:"phone"},{default:d(()=>[t(n,{modelValue:e(o).phone,"onUpdate:modelValue":u[3]||(u[3]=s=>e(o).phone=s),type:"tel",placeholder:"\u624B\u673A\u53F7",maxlength:"11"},null,8,["modelValue"])]),_:1})]),_:1},8,["page","query","data","page-total","form-data","form-rules"])}}});export{I as default};