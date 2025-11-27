from conexion.oracle_queries import OracleQueries

class SplashScreenLocadora:
    def __init__(self):
        self.nome_sistema = "SISTEMA DE LOCAÇÃO DE VEÍCULOS"

        self.created_by = (
           'Emanoel Vitor V. Atanazio'
           '\n\t\t\tFelipe R. Barzilai'
           '\n\t\t\tJoão Emanoel Justino'
           '\n\t\t\tLivia Favato B. Neves'
           '\n\t\t\tRogeres Jose P. da Silva\n'
        )

        self.professor = "Howard Roatti"
        self.disciplina = "Banco de Dados 2025/2"

    def get_total(self, tabela: str):
        oracle = OracleQueries()
        oracle.connect()
        df = oracle.sqlToDataFrame(
            f"SELECT COUNT(*) AS total_{tabela} FROM LABDATABASE.{tabela.upper()}"
        )
        return df[f"total_{tabela}"].values[0]

    def get_updated_screen(self):
        total_clientes = str(self.get_total('clientes'))
        total_carros = str(self.get_total('carros'))
        total_funcionarios = str(self.get_total('funcionarios'))
        total_locacoes = str(self.get_total('locacoes'))

        return f"""
##############################################################################
                           {self.nome_sistema.center(36)}                   
                                                                            
                    TOTAL DE REGISTROS EXISTENTES                           
                                                                            
    1 - CLIENTES:        {total_clientes.ljust(5)}                          
    2 - CARROS:          {total_carros.ljust(5)}                             
    3 - FUNCIONÁRIOS:    {total_funcionarios.ljust(5)}                       
    4 - LOCAÇÕES:        {total_locacoes.ljust(5)}                           
                                                                            
    CRIADO POR: {self.created_by.strip()}     
                                                                            
    DISCIPLINA: {self.disciplina}                                           
    PROFESSOR:  {self.professor}                                            
                                                                            
##############################################################################
"""
