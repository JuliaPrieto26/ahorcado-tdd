import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
// import 'rxjs/add/operator/catch';
import { catchError, retry } from 'rxjs/operators';
import { API_URL } from '../env';
import { Partida } from './models/Partida';

@Injectable({
  providedIn: 'root'
})

export class AhorcadoService {

  constructor(private http: HttpClient) { }

  login(name: String): Observable<any> {
    return this.http
      .post(`${API_URL}/login`, {name})
  }

  initialize(wordToGuess: String): Observable<any> {
    return this.http
      .post(`${API_URL}/initialize`, {wordToGuess})
  }

  getState(): Observable<Partida> {
    return this.http
      .get(`${API_URL}/get_state`)
  }

  arriesgar(userInput: String): Observable<Partida> {
    return this.http
      .post(`${API_URL}/arriesgar`, { userInput })
  }
}
