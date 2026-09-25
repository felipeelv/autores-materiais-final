import estilo;

size(380,0);

pair O=(4.25,3.70);
real r=2.55;
path contorno=shift(O)*scale(r)*unitcircle;

filldraw(contorno, preenchimento, destaque);

pair esquerda=O+(-r,0);
pair direita=O+(r,0);
pair R=O+r*dir(43);
pair C=O+r*dir(220);
pair D=O+r*dir(320);

draw(esquerda--direita,eleveLaranja+1.6bp);
draw(O--R,eleveAzul+1.6bp);
draw(C--D,eleveCinza+1.5bp);
draw(arc(O,r,88,142),eleveAzul+3.0bp);

dot(O,eleveAzul+4bp);
label("$O$",O,NW,eleveCinza+fontsize(16pt));
label("raio",O+0.55*r*dir(43),NW,eleveAzul+fontsize(16pt));
label("diâmetro",O+(0,-0.28),S,eleveLaranja+fontsize(16pt));
label("corda",(C+D)/2,S,eleveCinza+fontsize(16pt));
label("arco",O+r*dir(115),N,eleveAzul+fontsize(16pt));
label("círculo",O+(0,-1.45),eleveAzul+fontsize(17pt));

label("circunferência",(4.25,7.15),eleveLaranja+fontsize(18pt));
draw((4.25,6.88)--(4.25,6.35),eleveLaranja+1.2bp,Arrow(8bp));
