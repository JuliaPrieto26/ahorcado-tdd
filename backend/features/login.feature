Feature: login
  Para poder jugar una partida de ahorcado,
  como usuario
  quiero ingresar mi nombre de usuario

  Scenario: logueo satisfactorio
    Given hemos inicializado una partida
    And "Juan" ha ingresado su nombre
    Then podre ver que su nombre es "Juan"
