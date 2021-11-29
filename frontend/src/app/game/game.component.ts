import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AhorcadoService } from '../ahorcado.service';
import { Partida } from '../models/Partida';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss']
})
export class GameComponent implements OnInit {
  errorMessage = '';
  partida: Partida = {};

  constructor(
    private ahorcadoService: AhorcadoService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.ahorcadoService.getState().subscribe(
      res  => {
        this.partida = res;
        console.log(this.partida);
      },
      (err: any) => {
        console.log(err);
      }
    )
  }

  arriesgar(input: String): void {
    if(!input || input === '') {
      return;
    }
    this.ahorcadoService.arriesgar(input).subscribe(
      (res: any) => {
        this.partida = res;
      },
      (err: any) => {
        this.errorMessage = err.message;
      }
    );
 }
 playAgain(): void {
   this.router.navigate(['/newgame']);
 }
}
