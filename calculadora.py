#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Meu Primeiro Programa em Python
Autor: [Seu Nome]
Data: [Data de Hoje]
Descrição: Programa básico para aprender GitHub
"""

# Importações
import datetime
import random


# Função de boas-vindas
def boas_vindas():
    """Exibe mensagem de boas-vindas personalizada"""
    print("=" * 50)
    print("🐍 MEU PRIMEIRO PROGRAMA PYTHON NO GITHUB! 🐍")
    print("=" * 50)
    print()

    # 1. Olá Mundo básico
    print("1️⃣ Olá, Mundo!")
    print("   Bem-vindo ao GitHub!\n")

    # 2. Informações pessoais
    nome = "[Seu Nome]"
    turma = "[Turma]"

    print("2️⃣ Sobre mim:")
    print(f"   Nome: {nome}")
    print(f"   Turma: {turma}")
    print()

    # 3. Data e hora atual
    agora = datetime.datetime.now()
    print("3️⃣ Data e hora atual:")
    print(f"   {agora.strftime('%d/%m/%Y às %H:%M:%S')}\n")


# Função principal
def main():
    # Exibe boas-vindas
    boas_vindas()

    # 4. Operações matemáticas simples
    print("4️⃣ Calculadora básica:")
    num1 = 10
    num2 = 3
    print(f"   {num1} + {num2} = {num1 + num2}")
    print(f"   {num1} - {num2} = {num1 - num2}")
    print(f"   {num1} × {num2} = {num1 * num2}")
    print(f"   {num1} ÷ {num2} = {num1 / num2:.2f}\n")

    # 5. Lista de tecnologias que estou aprendendo
    print("5️⃣ Tecnologias que estou aprendendo:")
    tecnologias = ["Python", "GitHub"]
    for i, tech in enumerate(tecnologias, 1):
        print(f"   {i}. {tech}")
    print()

    # 6. Número aleatório da sorte
    numero_sorte = random.randint(1, 100)
    print("6️⃣ Seu número da sorte hoje é:", numero_sorte)
    print()

    # 7. Mensagem motivacional
    mensagens = [
        "Continue aprendendo, você está indo muito bem! 💪",
        "Cada linha de código é um passo para o sucesso! 🚀",
        "Programar é como mágica, mas real! ✨",
        "O GitHub é seu portfólio digital! 📁",
        "Python é só o começo da sua jornada! 🐍"
    ]
    print("7️⃣ Mensagem do dia:")
    print(f"   {random.choice(mensagens)}")
    print()

    # Rodapé
    print("=" * 50)
    print("Obrigado por executar meu programa!")
    print("Visite meu GitHub: github.com/[seu-usuario]")
    print("=" * 50)


# Executa o programa
if __name__ == "__main__":
    main()