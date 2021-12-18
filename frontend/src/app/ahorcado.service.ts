import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { environment } from '../environments/environment';
import { Partida } from './models/Partida';

@Injectable({
  providedIn: 'root'
})

export class AhorcadoService {
  // API_URL: String;

  constructor(private http: HttpClient) {
  }

  login(name: String): Observable<any> {
    return this.http
      .post(`${environment.API_URL}/login`, {name})
  }

  initialize(wordToGuess: String): Observable<any> {
    return this.http
      .post(`${environment.API_URL}/initialize`, {wordToGuess})
  }

  getState(): Observable<Partida> {
    return this.http
      .get(`${environment.API_URL}/get_state`)
  }

  arriesgar(userInput: String): Observable<Partida> {
    return this.http
      .post(`${environment.API_URL}/arriesgar`, { userInput })
  }
}
