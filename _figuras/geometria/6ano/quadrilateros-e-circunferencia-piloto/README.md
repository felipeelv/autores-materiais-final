# Piloto Asymptote — Geometria · 6º ano · BL1

Teste isolado do novo fluxo de figuras para o capítulo **Quadriláteros e circunferência**. O modelo aprovado em TikZ e as regras do `Geometria/AUTOR.md` não foram substituídos; o piloto permanece separado para avaliação.

## Resultado

- capítulo paralelo com três aulas de 205, 171 e 188 palavras;
- oito perguntas visuais, cada uma com fonte `.asy` própria;
- saída vetorial em SVG, saída de impressão em PDF e fallback transparente em PNG;
- rótulos em Roboto Regular, incorporada ao piloto para manter a renderização reproduzível;
- fórmulas em Latin Modern Math, preservando os símbolos matemáticos;
- prévias de 300 px sobre fundo branco revisadas visualmente;
- manifesto genérico separando a especificação do Autor da decisão técnica do Orquestrador;
- textos alternativos, marcadores, caminhos e hashes sincronizados.

## Arquivos principais

- capítulo: `Geometria/modelos/geometria-6ano-modelo-piloto-asymptote.md`;
- especificações e decisões do Orquestrador: `manifesto.json`;
- fontes: `src/fig-*.asy`;
- tipografia: `fonts/roboto/Roboto-VF.ttf`, distribuída sob a licença `fonts/roboto/OFL.txt`;
- saídas: `build/`;
- prévias para revisão: `preview/`;
- renderização reproduzível: `renderizar.sh`;
- validação do contrato genérico: `validar_piloto.py`.

## Executar

```bash
brew install asymptote
./_figuras/geometria/6ano/quadrilateros-e-circunferencia-piloto/renderizar.sh
./_figuras/geometria/6ano/quadrilateros-e-circunferencia-piloto/validar_piloto.py
```

O renderizador também usa a biblioteca do Ghostscript instalada pelo Homebrew em `/opt/homebrew/lib/libgs.dylib`.
Os rótulos usam a fonte variável oficial Roboto disponibilizada pelo Google Fonts; não é necessário instalar a fonte no sistema.

## Limite identificado

O validador oficial de Geometria ainda exige URL pública do repositório TikZ e PNG publicado. Por isso, o conteúdo e a estrutura do piloto passam nas verificações editoriais, mas a seção antiga `[7a] Figuras TikZ/PNG` rejeita corretamente os SVGs locais. A adoção definitiva exige generalizar essa seção para ler o manifesto por renderizador e formato, preservando as verificações de texto alternativo, hash e publicação.
