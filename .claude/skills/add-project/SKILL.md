---
name: add-project
description: Adiciona um novo projecto ao portfolio em index.html, garantindo que tanto a versão PT como EN são adicionadas ao objecto de traduções. Usa quando precisares de adicionar um projecto à secção "Projectos" do portfolio.
disable-model-invocation: true
---

O utilizador quer adicionar um novo projecto ao portfolio. Sigue estes passos:

1. Pede ao utilizador os detalhes do projecto (se não foram fornecidos em $ARGUMENTS):
   - Nome do projecto (PT e EN, se diferente)
   - Descrição curta (PT e EN)
   - Stack tecnológico / tecnologias usadas
   - Link (se existir)
   - Período (ex.: "2023 – presente")
   - Destaque ou resultado principal

2. Lê `index.html` para perceber a estrutura HTML actual dos cards de projectos e os campos existentes no objecto `translations` para projectos.

3. Adiciona o novo projecto:
   - Na secção HTML correcta (cards de projectos)
   - **Em ambas as línguas** no objecto `translations` — `pt` e `en` — sem excepção

4. Confirma que o projecto aparece correctamente em ambas as línguas ao rever o HTML e o objecto de traduções.

$ARGUMENTS
