import estilo;

size(380,0);

pair A=(0.7,0.6);
pair B=(7.7,0.9);
pair C=(6.8,4.4);
pair D=(1.5,3.8);

filldraw(A--B--C--D--cycle, preenchimento, aresta);
fill(A--B--C--cycle, eleveLaranja+opacity(0.08));
draw(A--C, destaque);
draw(B--D, auxiliar);

vertice(A,"$A$",SW);
vertice(B,"$B$",SE);
vertice(C,"$C$",NE);
vertice(D,"$D$",NW);

label("$\triangle ABC$",(5.2,1.8),eleveLaranja+fontsize(18pt));
label("$\triangle ACD$",(2.7,2.9),eleveAzul+fontsize(18pt));
