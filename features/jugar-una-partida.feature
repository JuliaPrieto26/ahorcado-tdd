Feature: jugar una partida

  Scenario: arriesgar una palabra
    Given se ha inicializado una partida con palabra a adivinar "agiles"
    When el jugador arriesga la palabra "agiles"
    Then habrá ganado la partida
