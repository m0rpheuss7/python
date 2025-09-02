from datetime import datetime

def obter_signo(dia: int, mes: int) -> str:
    signos = [
        ("Capricórnio", (22, 12), (20, 1)),
        ("Aquário", (21, 1), (19, 2)),
        ("Peixes", (20, 2), (20, 3)),
        ("Áries", (21, 3), (20, 4)),
        ("Touro", (21, 4), (20, 5)),
        ("Gêmeos", (21, 5), (20, 6)),
        ("Câncer", (21, 6), (22, 7)),
        ("Leão", (23, 7), (22, 8)),
        ("Virgem", (23, 8), (22, 9)),
        ("Libra", (23, 9), (22, 10)),
        ("Escorpião", (23, 10), (21, 11)),
        ("Sagitário", (22, 11), (21, 12))
    ]

    for signo, (dia_ini, mes_ini), (dia_fim, mes_fim) in signos:
        if (mes == mes_ini and dia >= dia_ini) or (mes == mes_fim and dia <= dia_fim):
            return signo
    return "Desconhecido"


def obter_cavaleiro(signo: str) -> str:
    cavaleiros = {
        "Áries": "Mu de Áries",
        "Touro": "Aldebaran de Touro",
        "Gêmeos": "Saga de Gêmeos",
        "Câncer": "Máscara da Morte de Câncer",
        "Leão": "Aiolia de Leão",
        "Virgem": "Shaka de Virgem",
        "Libra": "Dohko de Libra",
        "Escorpião": "Milo de Escorpião",
        "Sagitário": "Aiolos de Sagitário",
        "Capricórnio": "Shura de Capricórnio",
        "Aquário": "Camus de Aquário",
        "Peixes": "Afrodite de Peixes"
    }
    return cavaleiros.get(signo, "Desconhecido")


if __name__ == "__main__":
    data_str = input("Digite sua data de nascimento (ddmm ou dd/mm): ").strip()

    if "/" in data_str:
        dia, mes = map(int, data_str.split("/"))
    else:
        if len(data_str) != 4 or not data_str.isdigit():
            raise ValueError("Data inválida. Use o formato ddmm ou dd/mm.")
        dia = int(data_str[:2])
        mes = int(data_str[2:])

    signo = obter_signo(dia, mes)
    cavaleiro = obter_cavaleiro(signo)

    print(f"Seu signo é {signo} e seu Cavaleiro de Ouro correspondente é {cavaleiro}.")
