import estilo;

size(380,0);

void marcaParalelismo(pair a, pair b)
{
  pair inicio=a+0.36*(b-a);
  pair fim=a+0.58*(b-a);
  draw(inicio--fim, destaque, Arrow(8bp));
}

// Trapézio retângulo
pair A1=(3.15,5.25), B1=(7.35,5.25), C1=(6.35,6.70), D1=(3.15,6.70);
filldraw(A1--B1--C1--D1--cycle, preenchimento, aresta);
marcaParalelismo(A1,B1);
marcaParalelismo(D1,C1);
draw(A1+(0.28,0)--A1+(0.28,0.28)--A1+(0,0.28),eleveCinza+1.2bp);
draw(D1+(0,-0.28)--D1+(0.28,-0.28)--D1+(0.28,0),eleveCinza+1.2bp);
label("Retângulo",(1.25,5.98),eleveAzul+fontsize(18pt));

// Trapézio isósceles
pair A2=(3.05,2.80), B2=(7.45,2.80), C2=(6.55,4.20), D2=(3.95,4.20);
filldraw(A2--B2--C2--D2--cycle, preenchimento, aresta);
marcaParalelismo(A2,B2);
marcaParalelismo(D2,C2);
marcaSegmento(A2,D2,1,eleveLaranja);
marcaSegmento(B2,C2,1,eleveLaranja);
label("Isósceles",(1.25,3.50),eleveLaranja+fontsize(18pt));

// Trapézio escaleno
pair A3=(3.15,0.30), B3=(7.35,0.30), C3=(6.75,1.72), D3=(4.05,1.72);
filldraw(A3--B3--C3--D3--cycle, preenchimento, aresta);
marcaParalelismo(A3,B3);
marcaParalelismo(D3,C3);
label("Escaleno",(1.25,1.02),eleveCinza+fontsize(18pt));
