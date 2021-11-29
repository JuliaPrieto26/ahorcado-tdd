import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AhorcadoService } from '../ahorcado.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  errorMessage = '';

  constructor(
    private ahorcadoService: AhorcadoService,
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  login(name: String): void {
    if(!name || name === '') {
      return;
    }
    this.ahorcadoService.login(name).subscribe(
      res  => {
        this.errorMessage = '';
        localStorage.setItem('name', res);
        this.router.navigate(['/newgame']);
      },
      (err: any) => {
        this.errorMessage = err.error.message;
      }
    );
  }
}
