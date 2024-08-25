# one_billion_row_etl

### DESCRIÇAO
Este projeto verifica e analisa diferentes formas de se processar um ETL de 1 bilhão de linhas.
A intenção é encontrar estratégias eficientes para lidar com tamanhos de dados massivos com recursos limitado, situação comum no ambiente empresarial em que os custos são uma variável determinante para o sucesso de um projeto de dados.
O arquivo a ser processado contém 1 bilhão de linhas com resultados de dados metereológicos gerados artificialmente para fins didáticos.

### ESTRATÉGIAS E RESULTADOS
1. `etl_python`: Executado em 12 minutos utilizando as funções nativas
2. `etl_pandas`: Executado em 5 minutos seguindo as recomendações da documentação: utilizar datatypes eficientes e particionar o dataset;
3. `etl_duckdb`: Executado em 49 segundos;
4. `etl_duckdb_parquet`: Executado em 100 segundos;


Outra alternativa é utilizar o Spark no Databricks para um processamento distribuído



