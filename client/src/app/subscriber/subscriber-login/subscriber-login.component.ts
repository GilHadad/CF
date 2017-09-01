import { SubscriberLoginService } from './subscriber-login.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-subscriber-login',
  templateUrl: './subscriber-login.component.html',
  styleUrls: ['./subscriber-login.component.css'],
  providers: [SubscriberLoginService]
})
export class SubscriberLoginComponent implements OnInit {
  public userData: {username: string, password: string} = {username: '', password: ''};
  constructor(private loginService: SubscriberLoginService) { }

  ngOnInit() {
  }

  onSubmit(username: string, password: string) {
    this.loginService.login(this.userData.username, this.userData.password);
  }

}
