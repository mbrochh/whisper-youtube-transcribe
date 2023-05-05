import{d,i as p,a as _,u as h,b as u,c as m,e as f,f as n,g as t,t as o,h as a,F as g,r as v,n as x,j as y,o as r,k as b,l as N,m as k,p as P,q as w,_ as j}from"./index-9612a744.js";import{N as S}from"./NoteDisplay-6698bc5f.js";const V={class:"m-4"},L={class:"mb-10"},T={class:"text-4xl font-bold mt-2"},B={class:"opacity-50"},C={class:"text-lg"},D={class:"font-bold flex gap-2"},H={class:"opacity-50"},z=t("div",{class:"flex-auto"},null,-1),F={key:0,class:"border-gray-400/50 mb-8"},M=d({__name:"PresenterPrint",setup(q){p(_),h(`
@page {
  size: A4;
  margin-top: 1.5cm;
  margin-bottom: 1cm;
}
* {
  -webkit-print-color-adjust: exact;
}
html,
html body,
html #app,
html #page-root {
  height: auto;
  overflow: auto !important;
}
`),u({title:`Notes - ${m.title}`});const l=f(()=>y.slice(0,-1).map(s=>{var i;return(i=s.meta)==null?void 0:i.slide}).filter(s=>s!==void 0&&s.noteHTML!==""));return(s,i)=>(r(),n("div",{id:"page-root",style:x(a(w))},[t("div",V,[t("div",L,[t("h1",T,o(a(m).title),1),t("div",B,o(new Date().toLocaleString()),1)]),(r(!0),n(g,null,v(a(l),(e,c)=>(r(),n("div",{key:c,class:"flex flex-col gap-4 break-inside-avoid-page"},[t("div",null,[t("h2",C,[t("div",D,[t("div",H,o(e==null?void 0:e.no)+"/"+o(a(b)),1),N(" "+o(e==null?void 0:e.title)+" ",1),z])]),k(S,{"note-html":e.noteHTML,class:"max-w-full"},null,8,["note-html"])]),c<a(l).length-1?(r(),n("hr",F)):P("v-if",!0)]))),128))])],4))}}),R=j(M,[["__file","/Users/martin/Projects/pugs/presentations/chatgpt-copilot-whisper/slidev/node_modules/@slidev/client/internals/PresenterPrint.vue"]]);export{R as default};
