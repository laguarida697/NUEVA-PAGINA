import gen
W,H=1920,1080
svg=f'<svg id="s" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'+gen.defs()
svg=svg.replace('</defs>','<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4eefc"/><stop offset="1" stop-color="#dcd0f2"/></linearGradient></defs>')
svg+=f'<rect width="{W}" height="{H}" fill="url(#bg)"/>'
svg+='<g id="M"><g transform="translate(0,0)">'+gen.mimi(0,0,1)+'</g></g>'
svg+='<g id="T"><g transform="translate(0,0)">'+gen.tito(0,0,1)+'</g></g></svg>'
html='''<!doctype html><meta charset="utf-8"><body style="margin:0;background:#000">'''+svg+'''
<script>
const $=id=>document.getElementById(id);const FEET=330;
function arms(g,aL,aR){g.querySelector('.armL').setAttribute('transform',`rotate(${aL} ${g.querySelector('.armL').dataset.px} ${g.querySelector('.armL').dataset.py})`);g.querySelector('.armR').setAttribute('transform',`rotate(${aR} ${g.querySelector('.armR').dataset.px} ${g.querySelector('.armR').dataset.py})`)}
function pose(id,x,y,dy,rot,sx,sy){$(id).setAttribute('transform',`translate(${x},${y+dy}) rotate(${rot}) scale(${sx},${sy}) translate(0,${-0})`)}
function render(t){
 const TAU=Math.PI*2, s=Math.sin, ab=Math.abs;
 let mx=620,tx=1300,y=690,sc=1.05;
 let mdy=0,tdy=0,mr=0,tr=0,msx=1,msy=1,tsx=1,tsy=1,mAL=0,mAR=0,tAL=0,tAR=0;
 const f=1.4;
 if(t<3){ // saludo
   const b=ab(s(t*TAU*.7)); mdy=-b*10; tdy=-b*10;
   mAR=-30+30*s(t*TAU*1.6); mAL=8*s(t*TAU*.8); tAL=-25+25*s(t*TAU*1.6+1); tAR=6*s(t*TAU*.8);
   mr=2*s(t*TAU*.7); tr=-2*s(t*TAU*.7);
 } else if(t<6){ // saltos
   const u=(t-3); const ph=u*f; const b=ab(s(ph*Math.PI)); mdy=-b*85; tdy=-ab(s(ph*Math.PI+.7))*85;
   msy=1+.05*(1-b)-.0; tsy=1+.05*(1-ab(s(ph*Math.PI+.7)));
   mAR=-45*b; mAL=45*b; tAL=-40*b; tAR=40*b; mr=3*s(u*TAU*.7); tr=-3*s(u*TAU*.7);
 } else if(t<9){ // baile lateral
   const u=t-6; mx+=70*s(u*TAU*.5); tx-=70*s(u*TAU*.5);
   mdy=-ab(s(u*TAU*1.0))*35; tdy=-ab(s(u*TAU*1.0+1))*35; mr=9*s(u*TAU*1.0); tr=-9*s(u*TAU*1.0);
   mAR=-35*s(u*TAU*1.0); mAL=35*s(u*TAU*1.0+1); tAL=-30*s(u*TAU*1.0); tAR=30*s(u*TAU*1.0+1);
 } else { // reverencia final
   const u=Math.min(1,(t-9)); const bow=s(u*Math.PI); msy=1-.07*bow; tsy=1-.07*bow; mr=6*bow; tr=-6*bow; mAR=-20*(1-u); tAL=-20*(1-u);
 }
 pose('M',mx,y,mdy,mr,sc*msx,sc*msy);pose('T',tx,y,tdy,tr,sc*tsx,sc*tsy);
 arms($('M'),mAL,mAR);arms($('T'),tAL,tAR);
}
window.render=render;
if(new URLSearchParams(location.search).has('t'))render(parseFloat(new URLSearchParams(location.search).get('t')));else{const t0=performance.now();(function f(n){render(((n-t0)/1000)%10);requestAnimationFrame(f)})(t0)}
</script>'''
open('referencia-movimiento.html','w').write(html)
