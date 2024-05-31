import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environments/environment';



@Injectable({
  providedIn: 'root'
})
export class BackendService {

  constructor(private http: HttpClient) { }

  apiUrl = environment.apiUrl;

  getUsers(): Observable<any[]> {
    console.log(this.apiUrl)
    return this.http.get<any[]>(`${this.apiUrl}/users`);
  }
}
