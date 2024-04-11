; vectorFill.nasm
; Escreva um programa em assembly que preenche um vetor (que está salvo na memória) com uma constante. O vetor começa sempre na RAM[5] e possui tamanho definido pela RAM[4]. O valor da constante (a ser usado) está salvo na RAM[3].
;
; Veja o exemplo a seguir (`-k vectorFill_example`):
;
; ```
;                 INICIAL          FINAL
;             -------------------------------------
;   valor   ---> RAM[3]: 7   |
;   tamanho ---> RAM[4]: 4   |
;           ---  RAM[5]: 0   |     RAM[5]: 7
;            |   RAM[6]: 0   |     RAM[6]: 7
;      vetor |   RAM[7]: 0  ===>   RAM[7]: 7
;           ---  RAM[8]: 0   |     RAM[8]: 7
;                RAM[9]: 0   |     RAM[9]: 0
; ```
;
; Testes:
;
; -  `vectorFill_example`: Testa o exemplo (valor 7 e tamanho 4)
; -  `vectorFill_generic`: Teste genérico.
