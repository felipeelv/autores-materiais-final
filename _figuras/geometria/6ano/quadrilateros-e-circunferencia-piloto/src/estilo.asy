settings.tex="xelatex";
settings.render=4;

texpreamble("\usepackage{fontspec}");
texpreamble("\usepackage{unicode-math}");
texpreamble("\usepackage{amsmath}");
texpreamble("\setmainfont[Path=../fonts/roboto/]{Roboto-VF.ttf}");
texpreamble("\setmathfont{latinmodern-math.otf}");

defaultpen(fontsize(18pt));

pen eleveAzul = rgb(0.10,0.35,0.48);
pen eleveAzulClaro = rgb(0.84,0.93,0.96);
pen eleveLaranja = rgb(0.94,0.40,0.10);
pen eleveCinza = rgb(0.35,0.42,0.46);
pen eleveCinzaClaro = rgb(0.78,0.82,0.84);

pen aresta = eleveAzul+1.5bp;
pen auxiliar = eleveCinza+1.0bp+dashed;
pen destaque = eleveLaranja+1.8bp;
pen preenchimento = eleveAzulClaro+opacity(0.62);

void vertice(pair ponto, string nome, align posicao)
{
  dot(ponto, eleveAzul+3.5bp);
  label(nome, ponto, posicao, eleveCinza+fontsize(16pt));
}

void marcaSegmento(pair a, pair b, int quantidade=1, pen p=eleveLaranja)
{
  pair u=unit(b-a);
  pair v=rotate(90)*u;
  pair meio=(a+b)/2;
  real separacao=0.14;
  for(int i=0; i < quantidade; ++i) {
    real deslocamento=(i-(quantidade-1)/2.0)*separacao;
    pair centro=meio+deslocamento*u;
    draw(centro-0.12*v--centro+0.12*v, p+1.5bp);
  }
}
