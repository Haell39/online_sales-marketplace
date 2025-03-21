# 📊 **Análise de Vendas Online: Métodos de Pagamento e Comportamento Regional**

## **Introdução**

Este projeto analisa dados de vendas online com foco em métodos de pagamento e comportamento regional, utilizando um arquivo CSV com 240 transações para identificar padrões e extrair _insights_ estratégicos que possam orientar decisões de negócios.

## 🔍 **Principais Descobertas**

- **Descontos**: Não houve nenhum desconto aplicado nas 241 compras registradas.
- **Métodos de Pagamento**:
  - O **cartão de crédito** lidera, representando **50% das compras** e **mais de 63% da receita**.
  - Variações regionais:
    - **Ásia**: Cartão de crédito em 1/3 das operações; **cartão de débito** exclusivo nesta região.
    - **América do Norte**: Cartão de crédito em 2/3 das operações.
    - **Europa**: **PayPal** usado em 100% das operações.
- **Categorias de Produtos**: A categoria **Clothing (Vestuário)** foi comprada **exclusivamente com cartão de débito**.

## 🛠️ **Ferramentas Utilizadas**

- **Excel**: Para análise inicial, como tabelas dinâmicas e cálculos de receita por método de pagamento e região.
- **Jupyter Notebook**: Para exploração mais detalhada, utilizando bibliotecas Python como:
  - **Pandas**: Manipulação e limpeza dos dados.
  - **NumPy**: Cálculos numéricos.
  - **Matplotlib** e **Seaborn**: Visualizações gráficas (em andamento).

## 🔬 **Metodologia**

1. **Carregamento dos Dados**: Importação do arquivo CSV (`sales_dataset.csv`) com 240 entradas e 9 colunas (Transaction ID, Date, Product Category, Product Name, Units Sold, Unit Price, Total Revenue, Region, Payment Method).
2. **Limpeza de Dados**: Conversão da coluna `Date` para o formato `datetime64[ns]` e verificação de valores nulos/duplicados (nenhum encontrado até agora).
3. **Análise Exploratória**:
   - No Excel: Cálculo de percentuais de métodos de pagamento e análise regional.
   - No Jupyter: Início da análise com `.info()` e `.describe()` para entender a estrutura e estatísticas dos dados.

## 📈 **Próximos Passos**

- Avançar na exploração e análise no Jupyter Notebook, aproveitando ao máximo as capacidades do Python para desenvolver visualizações mais avançadas e identificar padrões adicionais.
- Investigar tendências sazonais e correlações entre unidades vendidas e receita total.

## 📝 **Conclusão**

Até agora, o projeto revelou preferências claras de pagamento por região e um padrão único na categoria de vestuário. A combinação de Excel e Jupyter Notebook está permitindo uma análise robusta, com potencial para _insights_ ainda mais profundos à medida que avançamos nas visualizações e explorações adicionais.

---

### **Repositório**

Confira o progresso no GitHub:  
<a href="https://github.com/Haell39/online_sales-marketplace">  
 <img src="https://github-readme-stats.vercel.app/api/pin/?username=Haell39&repo=online_sales-marketplace&theme=tokyonight" alt="Online Sales Marketplace">  
</a>
