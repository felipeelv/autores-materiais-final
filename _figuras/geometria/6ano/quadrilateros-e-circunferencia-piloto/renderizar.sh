#!/usr/bin/env bash
set -euo pipefail

piloto_dir="$(cd "$(dirname "$0")" && pwd)"
origens_dir="$piloto_dir/src"
build_dir="$piloto_dir/build"
preview_dir="$piloto_dir/preview"
font_dir="$piloto_dir/fonts/roboto"
font_file="$font_dir/Roboto-VF.ttf"
font_license="$font_dir/OFL.txt"

case "$piloto_dir" in
  */_figuras/geometria/6ano/quadrilateros-e-circunferencia-piloto) ;;
  *)
    echo "Diretório inesperado para o piloto: $piloto_dir" >&2
    exit 1
    ;;
esac

command -v asy >/dev/null 2>&1 || {
  echo "Asymptote não encontrado. Instale com: brew install asymptote" >&2
  exit 1
}

command -v xelatex >/dev/null 2>&1 || {
  echo "XeLaTeX não encontrado. Instale uma distribuição TeX atual." >&2
  exit 1
}

[ -s "$font_file" ] || {
  echo "Fonte Roboto incorporada não encontrada em: $font_file" >&2
  exit 1
}

[ -s "$font_license" ] || {
  echo "Licença da fonte Roboto não encontrada em: $font_license" >&2
  exit 1
}

libgs="/opt/homebrew/lib/libgs.dylib"
[ -f "$libgs" ] || {
  echo "Biblioteca do Ghostscript não encontrada em: $libgs" >&2
  exit 1
}

mkdir -p "$build_dir" "$preview_dir"

for origem in "$origens_dir"/fig-*.asy; do
  [ -f "$origem" ] || continue
  id="$(basename "$origem" .asy)"
  temporario="render-$id"

  asy -libgs "$libgs" -cd "$origens_dir" -f svg -o "$temporario" "$(basename "$origem")"
  mv "$origens_dir/$temporario.svg" "$build_dir/$id.svg"

  asy -libgs "$libgs" -cd "$origens_dir" -f pdf -o "$temporario" "$(basename "$origem")"
  mv "$origens_dir/$temporario.pdf" "$build_dir/$id.pdf"

  asy -libgs "$libgs" -cd "$origens_dir" -f png -render=4 -o "$temporario" "$(basename "$origem")"
  mv "$origens_dir/$temporario.png" "$build_dir/$id.png"

  sips --resampleWidth 300 "$build_dir/$id.png" \
    --out "$preview_dir/$id-300.png" >/dev/null
  sips -s format jpeg "$preview_dir/$id-300.png" \
    --out "$preview_dir/$id-300-branco.jpg" >/dev/null
done

echo "Renderização concluída em: $build_dir"
echo "Prévias de 300 px em: $preview_dir"
