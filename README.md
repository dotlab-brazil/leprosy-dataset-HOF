# 📊 Clinical Evaluation Dataset – Leprosy

This repository provides a structured dataset for clinical evaluation of patients, including demographic, clinical, and functional information organized across multiple relational tables.

It also includes an example pipeline demonstrating how to read and integrate the data into a denormalized tabular format suitable for analysis, visualization, and machine learning.

---

## 📁 Repository Structure

```text
dataset/
    ├── dataset-hof-2026 - paciente.csv
    ├── dataset-hof-2026 - ficha.csv
    ├── dataset-hof-2026 - face.csv
    ├── dataset-hof-2026 - membro_superior.csv
    ├── dataset-hof-2026 - membro_inferior.csv
    ├── dataset-hof-2026 - avaliacao_sensitiva_mao.csv
    ├── dataset-hof-2026 - avaliacao_sensitiva_pe.csv
    ├── dataset-hof-2026 - queixas.csv
    ├── dataset-hof-2026 - pontuacao.csv

modelagem/
    ├── data_dictionary.pdf
    ├── data modeling.png

example_reading.ipynb
example_reading.py
README.md
```

---

## 🧠 Data Modeling

* The dataset follows a **normalized relational model**
* The central table is **Ficha (clinical record)**, linked to other entities
* Clinical evaluations are recorded over time via `data_avaliacao`
* Some tables include an additional dimension: **side (right/left)**

For more details:

* 📘 `modelagem/dicionario_dados.pdf`
* 🧩 `modelagem/modelo_ER.png`

---

## 🚀 How to Use the Dataset

This repository provides example scripts for reading and integrating the data:

* `example_reading.py`
* `example_reading.ipynb`

### ✔️ Goal of the example

Transform multiple relational tables into a single DataFrame where:

> **Each row represents one clinical follow-up (id_ficha + data_avaliacao)**

---

## ▶️ Quick Start

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-name>
```

---

### 2. Install dependencies

```bash
pip install pandas
```

---

### 3. Run the example

```bash
python example_reading.py
```

Or open the notebook:

```bash
jupyter notebook example_reading.ipynb
```

---

## 📌 What the Code Does

The example pipeline performs the following steps:

### 🔹 1. Load CSV files

Reads all tables from the `dataset/` directory.

---

### 🔹 2. Date normalization

* Converts `data_avaliacao` to datetime format
* Handles common formatting inconsistencies

---

### 🔹 3. Side-based feature transformation

Tables containing a `lado` (side) column are pivoted into features:

Example:

```text
face_nariz_ressecamento_direita
face_nariz_ressecamento_esquerda
```

---

### 🔹 4. Data integration

* Merges tables using:

```text
id_ficha + data_avaliacao
```

* Ensures correct temporal granularity per follow-up

---

### 🔹 5. Enrichment with patient data

Adds attributes from:

* `paciente`
* `ficha`

---

## 📦 Output

A final DataFrame with a structure similar to:

```text
id_ficha | data_avaliacao | sexo | ... | face_* | ms_* | mi_* | mao_* | pe_* | ...
```

Ready for:

* 📊 Exploratory Data Analysis
* 📈 Dashboards (Power BI, Looker, etc.)
* 🤖 Machine Learning

---

# 📊 Dataset de Avaliação Clínica – Hanseníase

Este repositório contém um conjunto de dados estruturados para avaliação clínica de pacientes, incluindo informações demográficas, clínicas e funcionais organizadas em múltiplas tabelas relacionais.

Além disso, é disponibilizado um exemplo de leitura e integração dos dados em formato tabular (denormalizado), adequado para análises, visualização e modelos de machine learning.

---

## 📁 Estrutura do Repositório

```
dataset/
    ├── dataset-hof-2026 - paciente.csv
    ├── dataset-hof-2026 - ficha.csv
    ├── dataset-hof-2026 - face.csv
    ├── dataset-hof-2026 - membro_superior.csv
    ├── dataset-hof-2026 - membro_inferior.csv
    ├── dataset-hof-2026 - avaliacao_sensitiva_mao.csv
    ├── dataset-hof-2026 - avaliacao_sensitiva_pe.csv
    ├── dataset-hof-2026 - queixas.csv
    ├── dataset-hof-2026 - pontuacao.csv

modelagem/
    ├── data_dictionary.pdf
    ├── data modeling.png

example_reading.ipynb
example_reading.py
README.md
```

---

## 🧠 Modelagem dos Dados

* O dataset segue um modelo relacional normalizado
* A tabela central é a **Ficha**, que se conecta às demais
* Avaliações clínicas são registradas ao longo do tempo (`data_avaliacao`)
* Algumas tabelas possuem granularidade adicional por **lado (direito/esquerdo)**

Para mais detalhes:

* 📘 `modelagem/dicionario_dados.pdf`
* 🧩 `modelagem/modelo_ER.png`

---

## 🚀 Como Ler o Dataset

Este repositório inclui um exemplo de leitura e integração dos dados:

* `example_reading.py`
* `example_reading.ipynb`

### ✔️ Objetivo do exemplo

Transformar os dados de múltiplas tabelas em um único DataFrame onde:

> **Cada linha representa um acompanhamento clínico (id_ficha + data_avaliacao)**

---

## ▶️ Execução rápida

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd <nome-do-repo>
```

---

### 2. Instale as dependências

```bash
pip install pandas
```

---

### 3. Execute o exemplo

```bash
python example_reading.py
```

Ou utilize o notebook:

```bash
jupyter notebook example_reading.ipynb
```

---

## 📌 O que o código faz

O pipeline implementado no exemplo realiza:

### 🔹 1. Leitura dos CSVs

Carrega todas as tabelas da pasta `dataset/`

---

### 🔹 2. Normalização de datas

* Converte `data_avaliacao` para formato datetime
* Trata inconsistências de formatação

---

### 🔹 3. Transformação de variáveis por lado

Tabelas com coluna `lado` são convertidas para colunas:

Exemplo:

```
face_nariz_ressecamento_direita
face_nariz_ressecamento_esquerda
```

---

### 🔹 4. Integração dos dados

* Merge baseado em:

```
id_ficha + data_avaliacao
```

* Garante granularidade correta por acompanhamento

---

### 🔹 5. Enriquecimento com dados do paciente

Inclui informações de:

* paciente
* ficha

---

## 📦 Resultado

Um DataFrame final com estrutura semelhante a:

```
id_ficha | data_avaliacao | sexo | ... | face_* | ms_* | mi_* | mao_* | pe_* | ...
```

Pronto para:

* 📊 Análise exploratória
* 📈 Dashboards (Power BI, Looker, etc.)
* 🤖 Machine Learning

---
