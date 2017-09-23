import {Router} from '@angular/router';
import {LoginService} from '../../services/login/login-service.service';
import {Component, OnInit} from '@angular/core';

@Component({
  selector: 'app-subscriber-login',
  templateUrl: './subscriber-login.component.html',
  styleUrls: ['./subscriber-login.component.css'],
  providers: []
})
export class SubscriberLoginComponent implements OnInit {
  public userData: {username: string, password: string} = {username: '', password: ''};
  constructor(private loginService: LoginService, private router: Router) {}

  ngOnInit() {
    /* if user is logged in, we don't want to allow him to enter login page
    /* doing it like this isn't great, we see a flash of the page
    /* needs to probably another guard in router */
    if (this.loginService.isUserLoggedIn()) {
      this.router.navigate(['/'])
    }
  }

  onSubmit() {
    this.loginService
      .login(this.userData.username, this.userData.password)
      .subscribe(result => {
        if (result.success) {
          console.log('success!');
        } else {
          console.log('fail', result.msg);
        }
      });
  }

}
