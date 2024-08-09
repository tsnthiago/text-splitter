from langchain_openai import ChatOpenAI
from typing import List, Dict
import logging
import os
import pandas as pd

# 1. Configurações
csv_file_path = 'data.csv'
llm_model_name = "gpt-4o-mini"
openai_api_key = os.environ.get("OPENAI_API_KEY")

# 2. Configurar Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 3. Inicializar modelo LLM
llm = ChatOpenAI(temperature=0.5, model_name=llm_model_name)
llm_token_limit = 100000
total_tokens_used = 0  # Inicializar o contador de tokens

# 4. Carregar o CSV utilizando pandas
df = pd.read_csv(csv_file_path)

# 5. Função para agrupar por faixa etária e sexo
def group_posts(df):
    # Ensure the column names are accessed in a case-insensitive manner
    if 'sexo' not in df.columns.str.lower():
        raise KeyError("The column 'sexo' is missing from the dataframe.")

    male_keywords = ["MAS", "HOMEM"]
    female_keywords = ["FEM", "MULHER"]

    groups = {}
    for sexo in ["Masculino", "Feminino"]:
        for age_group, age_range in [
            ("0-24", (0, 24)),
            ("25-34", (25, 34)),
            ("35-44", (35, 44)),
            ("45plus", (45, float('inf'))),
        ]:
            keywords = male_keywords if sexo == "Masculino" else female_keywords
            filtered_df = df[
                (df["sexo"].str.upper().str.contains('|'.join(keywords))) &
                (df["age"] >= age_range[0]) &
                (df["age"] <= age_range[1])
            ]
            group_name = f"{sexo} {age_group}"
            if not filtered_df.empty:
                groups[group_name] = filtered_df["st_text"].tolist()
    return groups

# 6. Agrupar posts
grouped_posts = group_posts(df)

# 7. Analisar e combinar os chunks para cada grupo
final_analysis = {}
for group_name, posts in grouped_posts.items():

    if not posts:
        continue  # Pula grupos sem posts

    chunks: List[str] = []
    current_chunk = ""
    current_token_count = 0
    for post in posts:
        line_tokens = llm.get_num_tokens(post)
        if current_token_count + line_tokens < llm_token_limit - 500:
            current_chunk += post + "\n"
            current_token_count += line_tokens
        else:
            chunks.append(current_chunk.strip())
            current_chunk = post + "\n"
            current_token_count = line_tokens
    if current_chunk:
        chunks.append(current_chunk.strip())

    if not chunks:
        continue  # Pula grupos sem chunks

    # Processar cada chunk do grupo e combinar as análises
    group_chunk_analyses = []
    for i, chunk in enumerate(chunks):

        # Análise individual do chunk
        prompt = f"""
        Analise o seguinte conjunto de posts de forma concisa, identificando apenas os principais pontos. 
        Extraia as informações mais relevantes sobre contexto, menções a marcas e produtos, 
        e o sentimento geral, preferencialmente em frases curtas e objetivas.
        ```
        {chunk}
        ```
        """
        response = llm.invoke(prompt)
        analysis = response.content.strip()
        group_chunk_analyses.append(f"{analysis}")

        # Somar os tokens usados na resposta ao contador total
        total_tokens_used += response.response_metadata['token_usage']['total_tokens']

    # Combinar todas as análises dos chunks para o grupo específico
    all_chunks_text = "\n\n".join(group_chunk_analyses)
    final_prompt = f"""
    Combine as análises individuais dos chunks em um resumo único e conciso. 
    Foque em destacar os insights mais evidentes e os padrões recorrentes.
    
    Aqui estão as análises individuais:
    ```
    {all_chunks_text}
    ```

    Resumo conciso dos principais insights:
    """
    final_response = llm.invoke(final_prompt)
    final_insights = final_response.content.strip()

    # Somar os tokens usados na resposta ao contador total
    total_tokens_used += final_response.response_metadata['token_usage']['total_tokens']
    
    final_analysis[group_name] = final_insights

# 8. Formatar o relatório final como HTML
final_report = ""
for group_name, insights in final_analysis.items():
    final_report += f"<h2>Faixa Etária: {group_name}</h2>\n"
    final_report += f"<p>{insights}</p>\n"
    final_report += "<hr>\n"

# 9. Pedir ao LLM para estilizar o HTML
html_prompt = f"""
Formate o seguinte relatório em HTML estilizado. Use uma estrutura limpa com cabeçalhos, parágrafos e linhas de separação. 
Adicione CSS básico para melhorar a legibilidade, como margens, fontes, e cores suaves. Sua resposta deve ser APENAS o HTML, 
sem nenhum texto adicional, e nenhum caractér especial. Seu retorno será renderizado diretamente em uma página HTML.
Destaque pontos importantes em bullet points, e também use negrito em palavras-chave.

Relatório:
{final_report}

HTML:
"""
html_response = llm.invoke(html_prompt)
formatted_html = html_response.content.strip()
formatted_html = formatted_html.replace("```html", "").replace("```", "")

# Somar os tokens usados na resposta ao contador total
total_tokens_used += html_response.response_metadata['token_usage']['total_tokens']

# 10. Salvar o relatório formatado em um arquivo HTML
output_file = "relatorio_final.html"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(formatted_html)

logging.info(f"Relatório final salvo em {output_file}")
logging.info(f"Total de tokens usados: {total_tokens_used}")