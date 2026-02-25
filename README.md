# 📊 Dashboard de Vendas em Excel

Um projeto educacional completo para desenvolver habilidades em **análise de dados, visualização e ferramentas de negócio**.

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido como parte da disciplina **Empregabilidade**, com o objetivo de:

✅ Demonstrar competências em **análise de dados**  
✅ Desenvolver habilidades em **Python** e **Excel**  
✅ Criar soluções **práticas e profissionais**  
✅ Preparar para o **mercado de trabalho**  
✅ Mostrar capacidade de **organização e documentação**  

---

## ✨ O Que Este Projeto Oferece

### 📈 Funcionalidades Principais

- **Geração Automática de Dashboard**: Script Python que cria um Excel profissional em segundos
- **Dados Fictícios Realistas**: 3 meses de dados de vendas com 8 produtos diferentes
- **Métricas de Negócio**: 
  - Total de Vendas (R$)
  - Ticket Médio
  - Quantidade de Transações
  - Produto Mais Vendido

- **Visualizações Profissionais**:
  - 📊 Gráfico de Barras: Comparação de vendas por produto
  - 🥧 Gráfico de Pizza: Distribuição de vendas

- **Estrutura Clara**:
  - Aba "Dados Brutos": Todos os registros de transações
  - Aba "Dashboard": Métricas e gráficos consolidados

---

## 💼 Competências Desenvolvidas

Este projeto demonstra domínio em:

| Competência | Descrição |
|-------------|-----------|
| **Python** | Automação, manipulação de dados, criação de arquivos |
| **Excel** | Formatação profissional, gráficos, estrutura de dados |
| **Análise de Dados** | Cálculos de KPIs, agregações, insights |
| **Documentação** | README completo, código comentado, estrutura clara |
| **Git & GitHub** | Versionamento, controle de código, publicação |
| **Comunicação** | Projeto bem organizado e fácil de entender |

---

## 🚀 Como Usar

### Instalação Rápida (3 passos)

**1️⃣ Clone o repositório:**
```bash
git clone https://github.com/letrasan12-droid/dashboard-vendas-excel.git
cd dashboard-vendas-excel
```

**2️⃣ Instale as dependências:**
```bash
pip install -r requirements.txt
```

**3️⃣ Execute o script:**
```bash
python gerar_dashboard.py
```

**✅ Pronto!** Um arquivo `Dashboard_Vendas.xlsx` será criado automaticamente.

---

## 📁 Estrutura do Projeto

```
dashboard-vendas-excel/
├── gerar_dashboard.py       # 🐍 Script principal (Python)
├── requirements.txt         # 📦 Dependências do projeto
├── README.md               # 📖 Documentação
├── .gitignore             # 🔒 Arquivos ignorados
└── Dashboard_Vendas.xlsx  # 📊 Arquivo gerado (não sincronizado)
```

---

## 📊 Exemplo de Saída

### Aba 1: Dados Brutos
| Data | Produto | Quantidade | Preço Unitário | Valor Total |
|------|---------|-----------|-----------------|-------------|
| 01/11/2026 | Notebook | 2 | 3.500,00 | 7.000,00 |
| 01/11/2026 | Monitor | 1 | 1.200,00 | 1.200,00 |
| 02/11/2026 | Teclado | 3 | 350,00 | 1.050,00 |
| ... | ... | ... | ... | ... |

### Aba 2: Dashboard - Métricas
- **Total de Vendas**: R$ 1.234.567,89
- **Ticket Médio**: R$ 4.321,22
- **Quantidade de Vendas**: 285
- **Produto Mais Vendido**: Notebook

---

## 🔧 Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|-----------|--------|-----|
| **Python** | 3.7+ | Linguagem principal |
| **Pandas** | 2.0.0 | Manipulação de dados |
| **OpenPyXL** | 3.10.0 | Criação de Excel |
| **Matplotlib** | 3.7.0 | Visualização de dados |
| **Git** | - | Controle de versão |

---

## 💡 Como Customizar

### Mudar o período de vendas
```python
data_inicio = datetime(2026, 11, 1)  # Altere para a data desejada
```

### Adicionar novos produtos
```python
produtos = ['Notebook', 'Monitor', 'Teclado', 'Seu Novo Produto']
```

### Ajustar preços
```python
preco = {
    'Notebook': 3500,
    'Seu Novo Produto': 1000,  # Adicione aqui
}
```

### Alterar cores dos gráficos
```python
chart1.fill = PatternFill(start_color="FF0000", ...)  # Código HEX da cor
```

---

## 📚 O Que Você Aprenderá

Usando este projeto, você vai aprender:

✅ Como automatizar tarefas em Excel com Python  
✅ Técnicas de manipulação de dados com Pandas  
✅ Criação de relatórios profissionais  
✅ Boas práticas de documentação  
✅ Como organizar projetos no GitHub  
✅ Conceitos de análise de dados  
✅ Comunicação clara de resultados  

---

## 🎓 Disciplina: Empregabilidade

Este projeto foi desenvolvido como aplicação prática para a disciplina **Empregabilidade**, demonstrando:

- **Iniciativa**: Projeto completo e bem estruturado
- **Criatividade**: Solução prática e profissional
- **Persistência**: Documentação detalhada e código comentado
- **Qualidade**: Código limpo e bem formatado
- **Comunicação**: README claro e fácil de entender
- **Tecnologia**: Uso adequado de ferramentas modernas

---

## 🌟 Próximas Melhorias

Ideias para expandir o projeto:

- [ ] Integração com banco de dados SQL
- [ ] Dashboard interativo com Streamlit
- [ ] Análise de tendências com Machine Learning
- [ ] Filtros por período e produto
- [ ] Exportação em múltiplos formatos (PDF, CSV, JSON)
- [ ] Interface web com Flask/Django
- [ ] Testes automatizados

---

## 📞 Suporte

Tem dúvidas? Aqui estão os passos:

1. **Verifique a documentação** no README.md
2. **Veja os erros comuns** na seção de troubleshooting
3. **Abra uma issue** no GitHub
4. **Entre em contato** com o desenvolvedor

---

## 📜 Licença

Este projeto está disponível para **fins educacionais e profissionais**.

---

## 👨‍💻 Desenvolvedor

**Nome**: Manoel Messias de Oliveira Gomes  
**GitHub**: [@letrasan12-droid](https://github.com/letrasan12-droid)  
**Email**: letras.an12@gmail.com  
**Disciplina**: Empregabilidade  
**Data**: 2026-02-25  

---

## 🤝 Contribuições

Sugestões de melhorias? Sinta-se à vontade para:
- 🍴 Fazer um fork do projeto
- 🔀 Criar um pull request
- 📝 Abrir uma issue com sugestões
- 💬 Compartilhar ideias

---

**⭐ Se este projeto foi útil, considere dar uma estrela no GitHub!**

[⭐ Star este repositório](https://github.com/letrasan12-droid/dashboard-vendas-excel)