---
name: update-cv
description: Actualiza os CVs HTML em /Curriculum Vitae/ mantendo consistência entre os múltiplos templates. Usa quando adicionares nova experiência, certificação ou competência.
disable-model-invocation: true
---

O utilizador quer actualizar os CVs. Sigue estes passos:

1. Se não especificado em $ARGUMENTS, perguntar o que mudou:
   - Nova experiência profissional?
   - Nova certificação ou formação?
   - Novas competências técnicas?
   - Outra informação?

2. Listar os ficheiros HTML em `/Curriculum Vitae/` para identificar todos os templates existentes.

3. Verificar quais templates contêm a secção relevante (nem todos os templates têm todas as secções).

4. Aplicar a actualização em **todos os templates afectados**, mantendo consistência de formato e estrutura entre eles.

5. Se os CVs têm versões PT e EN, actualizar ambas as línguas.

6. Resumir quais ficheiros foram alterados e o que mudou em cada um.

$ARGUMENTS
