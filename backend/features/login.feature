Feature: login

  Scenario: loguearse en el ahorcado
    Given hemos inicializado una partida
    When "Juan" ingresa su nombre
    Then podre ver que su nombre es "Juan"
