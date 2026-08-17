import estilo;

size(380,0);

path moldura=box((0,0),(8.4,5.8));
path retangulos=shift(3.15,2.65)*scale(2.45,1.55)*unitcircle;
path losangos=shift(5.25,2.65)*scale(2.45,1.55)*unitcircle;

filldraw(moldura, eleveAzulClaro+opacity(0.25), aresta);
filldraw(retangulos, eleveAzul+opacity(0.10), eleveAzul+1.4bp);
filldraw(losangos, eleveLaranja+opacity(0.10), eleveLaranja+1.4bp);

label("Paralelogramos",(4.2,5.35),eleveAzul+fontsize(20pt));
label("Retângulos",(2.15,3.45),eleveAzul+fontsize(17pt));
label("Losangos",(6.25,3.45),eleveLaranja+fontsize(17pt));
label("Quadrados",(4.2,2.45),eleveCinza+fontsize(18pt));
