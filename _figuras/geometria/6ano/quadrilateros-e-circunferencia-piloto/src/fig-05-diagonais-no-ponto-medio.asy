import estilo;

size(380,0);

pair A=(0.9,0.55), B=(7.0,0.55), C=(8.15,4.15), D=(2.05,4.15);
pair M=(A+C)/2;

filldraw(A--B--C--D--cycle, preenchimento, aresta);
draw(A--C,eleveLaranja+1.5bp);
draw(B--D,eleveAzul+1.5bp);

marcaSegmento(A,M,1,eleveLaranja);
marcaSegmento(M,C,1,eleveLaranja);
marcaSegmento(B,M,2,eleveAzul);
marcaSegmento(M,D,2,eleveAzul);

vertice(A,"$A$",SW);
vertice(B,"$B$",SE);
vertice(C,"$C$",NE);
vertice(D,"$D$",NW);
dot(M,eleveCinza+4.0bp);
label("$M$",M,N,eleveCinza+fontsize(17pt));

label("$AM=MC$",(2.3,4.72),eleveLaranja+fontsize(17pt));
label("$BM=MD$",(6.1,4.72),eleveAzul+fontsize(17pt));
