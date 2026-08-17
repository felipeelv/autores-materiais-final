import estilo;

size(380,0);

pair O=(4.35,5.65);
real r=1.45;
path circ=shift(O)*scale(r)*unitcircle;
filldraw(circ,preenchimento,destaque);
draw(O+(-r,0)--O+(r,0),eleveAzul+1.6bp);
label("diâmetro $d$",O+(0,-0.32),S,eleveAzul+fontsize(17pt));

label("$C\approx3{,}14d$",(4.35,3.45),eleveCinza+fontsize(21pt));

real x0=0.35;
real y=1.75;
real d=2.45;
real resto=0.14*d;

draw((x0,y)--(x0+d,y),eleveAzul+3bp);
draw((x0+d,y)--(x0+2*d,y),eleveLaranja+3bp);
draw((x0+2*d,y)--(x0+3*d,y),eleveAzul+3bp);
draw((x0+3*d,y)--(x0+3*d+resto,y),eleveLaranja+3bp);

for(real x : new real[] {x0,x0+d,x0+2*d,x0+3*d,x0+3*d+resto})
  draw((x,y-0.22)--(x,y+0.22),eleveCinza+1bp);

label("$d$",(x0+0.5*d,y-0.30),S,eleveAzul+fontsize(17pt));
label("$d$",(x0+1.5*d,y-0.30),S,eleveLaranja+fontsize(17pt));
label("$d$",(x0+2.5*d,y-0.30),S,eleveAzul+fontsize(17pt));
label("$0{,}14d$",(x0+3*d+resto+0.08,y+0.55),E,eleveLaranja+fontsize(18pt));
draw((x0+3*d+resto-0.02,y+0.38)--(x0+3*d+0.5*resto,y+0.08),
     eleveLaranja+1.0bp,Arrow(6bp));
