import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AhorcadoService } from '../ahorcado.service';

@Component({
  selector: 'app-new-game',
  templateUrl: './new-game.component.html',
  styleUrls: ['./new-game.component.scss']
})
export class NewGameComponent implements OnInit {
  name = localStorage.getItem("name")
  errorMessage = '';
  hide = true;

  constructor(
    private ahorcadoService: AhorcadoService,
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  initializeGame(wordToGuess: String): void {
    if(!wordToGuess || wordToGuess === '') {
      return;
    }
    this.ahorcadoService.initialize(wordToGuess).subscribe(
      res => {
        this.errorMessage = '';
        localStorage.setItem('wordToGuess', res);
        this.router.navigate(['/game'])
      },
      (err: any) => {
        this.errorMessage = err.error.message;
      }
    );
  }
}
