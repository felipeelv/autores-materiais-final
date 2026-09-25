import estilo;

size(380,0);

real r=1.35;

pair O1=(2.45,4.70);
path c1=shift(O1)*scale(r)*unitcircle;
filldraw(c1,preenchimento,aresta);
pair T=O1+(r,0);
draw((T.x,T.y-1.75)--(T.x,T.y+1.75),destaque);
dot(T,eleveLaranja+4bp);
label("tangente",(6.0,5.08),eleveLaranja+fontsize(19pt));
label("1 ponto comum",(6.0,4.48),eleveCinza+fontsize(16pt));

pair O2=(2.45,1.55);
path c2=shift(O2)*scale(r)*unitcircle;
filldraw(c2,preenchimento,aresta);
draw((0.45,1.55)--(4.45,1.55),eleveAzul+1.7bp);
dot(O2+(-r,0),eleveAzul+4bp);
dot(O2+(r,0),eleveAzul+4bp);
label("secante",(6.0,1.93),eleveAzul+fontsize(19pt));
label("2 pontos comuns",(6.0,1.33),eleveCinza+fontsize(16pt));
