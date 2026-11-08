import{t as e}from"./rolldown-runtime.Bi-D_2cA.mjs";import{F as t,H as n,L as r,O as i,S as a,W as o,c as s,s as c,u as l,x as u,y as d}from"./react.CRh4czJk.mjs";import{G as f,c as p,kn as m,pt as h}from"./framer.lDuYyaD_.mjs";function g(e,t,n){return((e*7+t*13+e*t*5)*2654435761>>>0)%n}function _(e,t,n,r){let i=r*r;if(e===`dance-spark`)return-Math.round(g(t,n,i)*1200/i);if(e===`double-slow`)return-((n%2*190+t*120+n*55)*1.6%1920);let a=((t-n)*187.5%750+750)%750;return a===0?0:a-750}function v(e){return e===`dance-spark`?`danceSpark`:e===`double-slow`?`doubleSlow`:`ghostFlow`}function y(e){return e===`dance-spark`?1200:e===`double-slow`?1920:750}function b(e){let{variant:n=`ghost-flow`,grid:i=`4x4`,dotColor:s=`#0099ff`,gap:f=14/3,size:p=20,pauseOffscreen:h=!0,pauseOnCanvas:g=!0,duration:b=0,onComplete:C,style:w}=e,T=a(null),[E,D]=d(!0),[O,k]=d(!1),A=a(!1);u(()=>{if(!h){D(!0);return}let e=new IntersectionObserver(e=>{let t=e[0];t&&r(()=>D(t.isIntersecting))},{threshold:0});return T.current&&e.observe(T.current),()=>{e.disconnect()}},[h]);let j=g&&m.current()===m.canvas,M=!j&&(!h||E);u(()=>{A.current=!1,r(()=>k(!1))},[n,i,s,f,p,h,g,b]),u(()=>{if(b<=0||O||!M||o===void 0)return;let e=o.setTimeout(()=>{A.current||(A.current=!0,r(()=>k(!0)),C&&C())},b*1e3);return()=>o.clearTimeout(e)},[b,M,O,C]);let N=t(()=>{let e=i===`3x3`?3:4,t=e>1?f:0,r=v(n),a=y(n),o=[];for(let i=0;i<e;i++)for(let l=0;l<e;l++){let u=_(n,i,l,e);o.push(/*#__PURE__*/ c(`span`,{"aria-hidden":!0,style:{position:`absolute`,top:i*t,left:l*t,width:x,height:x,borderRadius:`50%`,backgroundColor:s,opacity:.3,animationName:r,animationDuration:`${a}ms`,animationTimingFunction:`linear`,animationIterationCount:`infinite`,animationDelay:`${u}ms`,animationPlayState:O||j?`paused`:E?`running`:`paused`}},`${i}-${l}`))}return o},[n,i,s,f,E,j,O]),P=x+Math.max(0,(i===`3x3`?3:4)-1)*f,F=P>0?P:S;return/*#__PURE__*/ l(`div`,{ref:T,role:`img`,"aria-label":`Animated dot grid`,style:{position:`relative`,overflow:`hidden`,padding:2,width:p,height:p,opacity:1,transition:`none`,...w},children:[/*#__PURE__*/ c(`style`,{children:`
@keyframes ghostFlow {
  0%, 18% { opacity: 1; }
  35% { opacity: 0.6; }
  50%, 100% { opacity: 0.3; }
}
@keyframes doubleSlow {
  0%, 100% { opacity: 0.3; }
  8% { opacity: 0.72; }
  16%, 24% { opacity: 1; }
  34%, 50% { opacity: 0.3; }
  58% { opacity: 0.58; }
  66%, 74% { opacity: 0.96; }
  84% { opacity: 0.48; }
}
@keyframes danceSpark {
  0%, 6% { opacity: 1; }
  18% { opacity: 0.45; }
  24%, 100% { opacity: 0.3; }
}
            `}),/*#__PURE__*/ c(`div`,{style:{position:`relative`,width:F,height:F,transform:`scale(${(p-4)/F})`,transformOrigin:`top left`},children:N})]})}var x,S;function C(){return(C=e((()=>{n(),s(),i(),h(),x=2,S=16,f(b,{grid:{type:p.Enum,title:`Grid`,options:[`4x4`,`3x3`],optionTitles:[`4×4`,`3×3`],defaultValue:`4x4`},variant:{type:p.Enum,title:`Variant`,options:[`ghost-flow`,`double-slow`,`dance-spark`],optionTitles:[`Ghost Flow`,`Double Slow`,`Dance Spark`],defaultValue:`ghost-flow`},dotColor:{type:p.Color,title:`Dot Color`,defaultValue:`#0099ff`},gap:{type:p.Number,title:`Gap`,defaultValue:14/3,min:0,max:20,step:.1,unit:`px`},size:{type:p.Number,title:`Size`,defaultValue:20,min:8,max:200,step:1,unit:`px`},pauseOffscreen:{type:p.Boolean,title:`Pause off-screen`,defaultValue:!0},pauseOnCanvas:{type:p.Boolean,title:`Pause on Canvas`,defaultValue:!0},duration:{type:p.Number,title:`Duration`,description:`0 = loops forever`,defaultValue:0,min:0,max:60,step:.1,unit:`s`},onComplete:{type:p.EventHandler,title:`On Complete`}})})))()}export{C as n,b as t};