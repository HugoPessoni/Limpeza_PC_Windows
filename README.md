# Automação para Limpeza de Arquivos Temporários no Windows

Sabe quando seu PC começa a dar uma travadas? Bom, técnicos quando não simplesmente formatam seu PC eles fazem esses processos que você encontrará nesse código. Este projeto automatiza a limpeza de arquivos temporários no Windows, melhorando o desempenho e liberando espaço em disco. A seguir, são detalhadas as operações realizadas pela automação, explicando cada etapa e a razão para a remoção segura dos arquivos. Precisa ter medo não! Sem contar que você pode escolher quais operações quer realizar e quais não. 

## Índice

1. [Limpeza da Pasta Prefetch](#limpeza-da-pasta-prefetch)
2. [Limpeza da Lista de Programas Recentes, pasta Recent](#limpeza-da-lista-de-programas-recentes-pasta-recent)
3. [Limpeza da Pasta Temp do Usuário](#limpeza-da-pasta-temp-do-usuário)
4. [Limpeza da Pasta %Temp% do Sistema](#limpeza-da-pasta-temp-do-sistema)
5. [Limpeza do Disco com o Cleanmgr](#limpeza-do-disco-com-o-cleanmgr)
6. [⚠️ Avisos e Considerações](#avisos-e-considerações)

---

### Limpeza da Pasta Prefetch

**Descrição:**
A pasta `Prefetch` contém dados que ajudam o Windows a iniciar programas mais rapidamente.

**Por que apagar:**
Eliminar esses arquivos libera espaço e resolve possíveis problemas, já que são recriados automaticamente assim que você abre os arquivos navamente. 

---

### Limpeza da Lista de Programas Recentes, pasta Recent

**Descrição:**
A pasta `Recent` guarda atalhos para arquivos e programas acessados recentemente.

**Por que apagar:**
Remover esses atalhos preserva a privacidade e libera um pouco de espaço, também serão ecriados automaticamente quando acessar os programas.

---

### Limpeza da Pasta Temp do Usuário

**Descrição:**
A pasta `Temp` do usuário armazena arquivos temporários criados por programas durante a execução.

**Por que apagar:**
Excluir esses arquivos libera espaço e previne conflitos ou erros em aplicativos, completamente inuteis.

---

### Limpeza da Pasta %Temp% do Sistema

**Descrição:**
A pasta de arquivos temporários do sistema é usada pelo Windows e aplicativos para dados temporários essenciais.

**Por que apagar:**
Limpar essa pasta libera espaço e pode resolver problemas de desempenho relacionados a arquivos temporários.

---

### Limpeza do Disco com o Cleanmgr

**Descrição:**
O Cleanmgr remove arquivos desnecessários do sistema, incluindo temporários e caches.

**Por que apagar:**
Libera espaço de forma segura e remove arquivos que não são mais necessários, melhorando o desempenho.

---

### ⚠️ Avisos e Considerações 

- **Permissões:** Algumas operações podem precisar de privilégios de administrador. Execute a automação com as permissões adequadas.
  
- **Impacto no Desempenho:** A exclusão de certos arquivos temporários pode causar um leve impacto no desempenho inicial dos programas, mas apenas no inicio.
  
- **Pontos de Restauração:** Apagar pontos de restauração anteriores reduz a capacidade de reverter o sistema para estados anteriores. Avalie a necessidade de manter alguns pontos.
  
- **Dados Importantes:** Verifique se não há arquivos importantes nas pastas de limpeza para evitar perda de dados.
  
---
