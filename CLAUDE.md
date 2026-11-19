# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Visão Geral

Portfolio pessoal de Ercílio Teixeira Júlio — site estático bilíngue (PT/EN) sem build tools, package manager, frameworks ou pipeline de CI/CD. Ficheiros servidos directamente como HTML estático.

## Estrutura de Pastas

- `/assets/` — CSS global e fontes (FontAwesome v6 local)
- `/Curriculum Vitae/` — Múltiplos templates de CV em HTML (versões PT/EN, print, dark theme)
- `/Biografia/` — Documentos de biografia profissional
- `/Candidaturas/` — Cartas de candidatura a emprego
- `/CERCTIFICACOES/` — Certificados concluídos e em progresso

## Quirk Crítico: Traduções PT/EN

As traduções estão hardcoded num único objeto JavaScript dentro de `index.html`:

```js
const translations = { pt: { ... }, en: { ... } };
```

**Qualquer alteração de texto visível ao utilizador requer actualização em AMBOS os idiomas** (`pt` e `en`) dentro deste objeto. Nunca alterar só uma língua.

## CVs HTML

Existem vários templates em `/Curriculum Vitae/`. Ao actualizar informação profissional (experiência, competências, certificações), verificar quais templates necessitam de actualização e manter consistência entre eles.

## Formulário de Contacto

O formulário no footer é **puramente visual** — não tem backend nem envia emails. Não sugerir que funciona.

## Deploy

O site ainda não está deployado. Quando chegar a altura, o GitHub Pages é a opção mais natural dado o repositório (`github.com:ErCiLio2/ercilio-portfolio.git`).

## Dependências Externas

Apenas CDN: Google Fonts (Inter) e FontAwesome v6 (local em `/assets/`). Não há `npm install` ou equivalente a correr.
