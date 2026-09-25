import estilo;
size(380,0);

pair A=(0.9,0.55), B=(7.0,0.55), C=(8.15,4.15), D=(2.05,4.15);

filldraw(A--B--C--D--cycle, preenchimento, aresta);

marcaSegmento(A,B,1,eleveLaranja);
marcaSegmento(D,C,1,eleveLaranja);
marcaSegmento(A,D,2,eleveAzul);
marcaSegmento(B,C,2,eleveAzul);

draw(arc(A,0.72,0,72.3),destaque);
draw(arc(C,0.72,180,252.3),destaque);

draw(arc(B,0.65,72.3,180),eleveAzul+1.4bp);
draw(arc(B,0.82,72.3,180),eleveAzul+1.1bp);
draw(arc(D,0.65,-107.7,0),eleveAzul+1.4bp);
draw(arc(D,0.82,-107.7,0),eleveAzul+1.1bp);

vertice(A,"$A$",SW);
vertice(B,"$B$",SE);
vertice(C,"$C$",NE);
vertice(D,"$D$",NW);
