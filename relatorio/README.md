# Relatório em LaTeX (classe-ifg)

Versão LaTeX do `RELATORIO.md`, formatada com a classe `classe-ifg` (opção `relatorio`).

## Estrutura

- `relatorio.tex`: arquivo principal (dados da folha de rosto e ajustes de compactação);
- `tex/cap01.tex` a `tex/cap06.tex`: capítulos, na estrutura sugerida no enunciado;
- `pre/preResumo.tex`: resumo (opcional; está comentado);
- `bib/bibliografia.bib`: referências (estilo ABNT autor-data, `abnt-alf`);
- `prog/`: trecho de código exibido no texto;
- `figuras/`: figuras geradas pelo notebook;
- `formatacao/`: arquivos da classe (cópia de `../classe-ifg/formatacao`, não editar).

## Compilação

```bash
pdflatex relatorio
bibtex relatorio
pdflatex relatorio
pdflatex relatorio
```

ou `latexmk -pdf relatorio`. Também funciona no Overleaf: envie a pasta `relatorio/` inteira.
