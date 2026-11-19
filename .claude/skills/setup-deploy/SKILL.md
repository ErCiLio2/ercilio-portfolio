---
name: setup-deploy
description: Configura o deploy do portfolio para GitHub Pages (ou alternativa). Usa quando estiveres pronto para publicar o site online.
disable-model-invocation: true
---

O utilizador quer fazer o deploy do portfolio. O repositório está em `github.com:ErCiLio2/ercilio-portfolio.git`.

## Opção recomendada: GitHub Pages

1. Verificar se o `gh` CLI está disponível: `which gh`

2. Configurar GitHub Pages via CLI:
   ```bash
   gh api repos/ErCiLio2/ercilio-portfolio/pages \
     -X POST \
     -f source[branch]=main \
     -f source[path]=/
   ```

3. Verificar que `index.html` está na raiz do repositório (já está).

4. Confirmar o URL público gerado (normalmente `https://erciLio2.github.io/ercilio-portfolio/`).

5. Alertar para ajustar quaisquer caminhos de assets que assumam raiz absoluta (`/assets/`) para caminhos relativos (`./assets/`) se necessário.

## Alternativas

Se o utilizador preferir outra plataforma (Vercel, Netlify, Cloudflare Pages):
- **Vercel**: `npx vercel` na raiz do projeto (requer Node.js)
- **Netlify**: drag-and-drop de pasta ou CLI `netlify deploy`
- **Cloudflare Pages**: ligação directa ao repositório GitHub via dashboard

Perguntar ao utilizador qual prefere antes de prosseguir.

$ARGUMENTS
