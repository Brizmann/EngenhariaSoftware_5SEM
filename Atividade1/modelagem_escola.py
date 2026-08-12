import unittest

class Aluno:

    def __init__(self, nome):
        self.nome = nome
        self._notas = []  # Encapsulamento da lista de notas

    def adicionar_nota(self, nota):
        self._notas.append(nota)

    def media(self):
        # Blindagem contra ZeroDivisionError caso a lista esteja vazia
        if not self._notas:
            return 0.0
        return sum(self._notas) / len(self._notas)


# Testes Unitários para suportar o fluxo TDD (Red-Green-Refactor)
class TestAluno(unittest.TestCase):

    def test_media_sem_notas_deve_retornar_zero(self):
        aluno = Aluno("Carlos")
        self.assertEqual(aluno.media(), 0.0)

    def test_media_com_notas_deve_calcular_corretamente(self):
        aluno = Aluno("Ana")
        aluno.adicionar_nota(8.0)
        aluno.adicionar_nota(10.0)
        self.assertEqual(aluno.media(), 9.0)