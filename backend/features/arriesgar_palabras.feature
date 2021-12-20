Feature: arriesgar palabras
  Como jugador,
  quiero arriesgar una palabra
  para poder ganar la partida directamente

  Scenario: la palabra arriesgada es la correcta
    Given hemos inicializado una partida
    And "Juan" ha ingresado su nombre
    And la palabra a adivinar es "agiles"
    When el usuario arriesga la palabra "agiles"
    Then el usuario habrá ganado la partida

  Scenario: la palabra arriesgada es incorrecta
    Given hemos inicializado una partida
    And "Juan" ha ingresado su nombre
    And la palabra a adivinar es "agiles"
    When el usuario arriesga la palabra "agilidad"
    Then el usuario habrá perdido la partida
