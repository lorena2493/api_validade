from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from flask import Flask, jsonify
# from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)


# Documentação OpenAPI
# spec = FlaskPydanticSpec('flask', title='API Validade de Produtos', version='1.0.0')
# spec.register(app)
#
#
@app.route("/")
def index():
    return "Hello World"

@app.route('/validade/<tipo>/<quantidade>')
def validade(tipo, quantidade):
    hoje = datetime.today()
    data_validade = hoje + relativedelta(quantidade)
    dia_da_semana = data_validade.weekday()
    dia = data_validade.day
    mes = data_validade.month
    ano = data_validade.year
    print(data_validade)
    if tipo == 'dia':
        quantidade = dia
    elif tipo == 'mes':
        quantidade = mes
    elif tipo == 'ano':
        quantidade = ano

    return jsonify({"hoje": datetime.today().strftime("%d/%m/%Y"),
                    "dia_semana": dia_da_semana,
                    "dia": dia,
                    "mes": mes,
                    "ano": ano,
                    "data_validade": data_validade, })






























    #
    # (f'"antes" - {datetime.today().strftime("%d-%m-%Y")}, '
    #     f'"dias" - {dias}, '
    #     f'semanas - {semanas}, '
    #     f'"meses" - {meses}, '
    #     f'"anos" - {anos}')


# @app.route('/validadeprodutos/<produto>/<data_fabricacao>', methods=['GET'])
# def validadeprodutos(produto, data_fabricacao):
#     # Converter string da data em um objeto datetime
#     '''
#     API para calcular a validade de produtos de acordo com a data da fabricacão.
#     ## Endpoint:
#     `GET/produto/data_fabricacao`
#
#     ## Parâmetros:
#     - `data_str` (str): Data no formato "DD/MM/YYYY"** (exemplo: "00-00-0000").
#     - **Qualquer outro formato resultará em erro.**
#
#     #Resposta (JSON):
#     ```json
#     {
#         "dias": 100,
#         "mes": 3,
#         "anos": 0,
#         "tempo": "passado"
#     }
#     ```
#     ## Erros possíveis:
#     - Se `data_str`não estiver no formato correto, retorna erro **400 Bad Request**:
#     ```json
#     '''
#     try:
#         # Converter a string da data para um objeto datetime
#         data_fabricacao = datetime.strptime(data_fabricacao, "%d-%m-%Y")
#
#         # Definir validade padrão (12 meses)
#         validade_prazo = 12
#         data_validade = data_fabricacao + relativedelta(months=validade_prazo)
#
#         # Calcular diferenças entre datas
#         hoje = datetime.today()
#         diferenca = relativedelta(data_validade, hoje)
#
#         # Calcular a diferença em dias, semanas, meses e anos
#         validade_dias = (data_validade - hoje).days
#         validade_dias = abs(validade_dias)  # Aqui, aplicamos o valor absoluto
#         validade_semanas = abs(validade_dias) // 7
#         validade_meses = abs(diferenca.months) + (abs(diferenca.years) * 12)
#         validade_anos = abs(diferenca.years)
#
#         # Retornar os dados em formato JSON
#         return {
#             "produto": produto,
#             "fabricacao": data_fabricacao.strftime("%d-%m-%Y"),
#             "validade": data_validade.strftime("%d-%m-%Y"),
#             "dias": validade_dias,
#             "semanas": validade_semanas,
#             "meses": validade_meses,
#             "anos": validade_anos
#         }
#
#     except ValueError:
#         return {"erro": "Formato de data inválido. Use DD-MM-YYYY."}, 400


if __name__ == '__main__':
    app.run(debug=True)
