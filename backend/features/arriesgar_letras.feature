Feature: arriesgar letras
  Como jugador,
  quiero arriesgar una letra
  para poder avanzar en el estado de la partida

  Scenario: la letra arriesgada es correcta
    Given hemos inicializado una partida
    And "Juan" ha ingresado su nombre
    And la palabra a adivinar es "agiles"
    When el usuario arriesga la letra "g"
    Then el usuario habrá acertado una letra y tendrá cero errores

  Scenario: la letra arriesgada es incorrecta
    Given hemos inicializado una partida
    And "Juan" ingresa su nombre
    And la palabra a adivinar es "agiles"
    When el usuario arriesga la letra "x"
    Then el usuario habrá errado una letra y tendrá un error

  Scenario: la letra arriesgada es correcta y está contenida tres veces en la palabra
    Given hemos inicializado una partida
    And "Juan" ha ingresado su nombre
    And la palabra a adivinar es "elefante"
    When el usuario arriesga la letra "e"
    Then el usuario habrá acertado tres veces y tendrá cero errores
