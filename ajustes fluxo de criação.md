# Ajustes no fluxo de criação

## 1. Mecanismos e instalação

| Ferramenta | Uso principal | Instalação resumida |
|---|---|---|
| **PGFPlots** | Gráficos matemáticos 2D e 3D em LaTeX | Incluído no TeX Live; se necessário, `tlmgr install pgfplots` |
| **ChemFig** | Estruturas químicas em LaTeX | `tlmgr install chemfig` |
| **mhchem** | Fórmulas e equações químicas em LaTeX | `tlmgr install mhchem` |
| **RDKit** | Geração e manipulação de estruturas moleculares em SVG, PNG ou PDF | `conda install -c conda-forge rdkit` |
| **Matplotlib** | Gráficos científicos e estatísticos estáticos | `pip install matplotlib` |
| **Plotly** | Gráficos interativos e exportação de imagens | `pip install plotly kaleido` |
| **Asymptote** | Geometria e ilustrações matemáticas vetoriais | macOS: `brew install asymptote` |
| **Mermaid CLI** | Fluxogramas e diagramas a partir de texto | `npm install -g @mermaid-js/mermaid-cli` |
| **Graphviz** | Grafos, árvores e organogramas | macOS: `brew install graphviz` |
| **PlantUML** | Diagramas UML e diagramas técnicos | macOS: `brew install plantuml` |
| **Inkscape** | Edição e conversão de arquivos SVG e PDF | macOS: `brew install --cask inkscape` |
| **Wolfram Engine** | Cálculo simbólico, numérico e científico avançado | Instalar pelo site oficial da Wolfram e configurar o acesso por MCP ou API |

## 2. Como inserir no fluxo

O Autor IA descreve a figura necessária sem escolher a tecnologia de renderização. O Orquestrador interpreta essa descrição e encaminha a tarefa ao renderizador especializado mais adequado.

```text
Autor IA
   │
   ▼
Descrição da figura
   │
   ▼
Orquestrador
   │
   ├── gráfico matemático ───────────► PGFPlots
   ├── estrutura molecular ──────────► RDKit
   ├── estrutura ou reação química ──► ChemFig
   ├── gráfico científico/estatístico ► Matplotlib
   ├── geometria ────────────────────► Asymptote
   ├── fluxograma ───────────────────► Mermaid
   ├── grafo ou organograma ─────────► Graphviz
   └── cálculo científico complexo ──► Wolfram
                                           │
                                           ▼
                                        SVG/PDF
                                           │
                                           ▼
                                      Google Drive
                                           │
                                           ▼
                                        Markdown
```

Assim, o conteúdo permanece separado da decisão técnica: o autor informa **o que deve ser representado**, enquanto o orquestrador decide **como produzir a figura**.
