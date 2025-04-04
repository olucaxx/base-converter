# Base Converter

Uma calculadora para transformar valores de uma base em outra.

Funciona muito bem com potências de 2, como 2, 4, 8 e 16, mas também suporta bases menos comuns, como base 5 e base 3.

Aceita valores inteiros e fracionários, porém a precisão dos números decimais após a vírgula pode não ser exata em certos casos, como nos valores 0,7 e 0,9 (em base 10).

## Como executar

### Pré-requisitos
- Python 3.12 ou superior instalado

### Instalação e execução

1. Clone o repositório:
   ```sh
   git clone https://github.com/olucaxx/base_converter
   cd base_converter
    ```
2. (Opcional) Crie um ambiente virtual:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    .venv\Scripts\activate     # Windows
    ```
3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```
4. Instale o pacote localmente:
    ```sh
    pip install .
    ```
5. Execute com:
    ```sh
    base-converter <number> <original_base> <target_base>
    ```
    Para uma descrição mais detalhada, use `base-converter -h` ou `base-converter --help`