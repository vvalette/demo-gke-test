import { Component, OnInit } from '@angular/core';
import { BackendService } from './backend';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: `./app.component.html`,
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  users: any[] = [];
  commitDate: string | null = null;

  constructor(private backendService: BackendService, private http: HttpClient) {}

  getCommitDate(): Observable<string> {
    return this.http.get('assets/commit-date.txt', { responseType: 'text' });
  }

  ngOnInit(): void {
    this.backendService.getUsers().subscribe(users => {
      this.users = users;
    });

    this.getCommitDate().subscribe(date => {
      this.commitDate = date;
    });
  }
}
