import { Component, OnInit } from '@angular/core';
import { BackendService } from './backend';
import { environment } from '../environments/environment';

@Component({
  selector: 'app-root',
  templateUrl: `./app.component.html`,
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  users: any[] = [];
  build_date = environment.buildTime;

  constructor(private backendService: BackendService) { }

  ngOnInit(): void {
    this.backendService.getUsers().subscribe(users => {
      this.users = users;
    });
  }
}