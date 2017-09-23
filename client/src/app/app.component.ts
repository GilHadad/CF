import {LoginGuard} from './services/login/login-guard';
import {LoginService} from './services/login/login-service.service';
import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  providers: [],
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Welcome to CONTROL FREAK!!!';
  subTitle = 'lets get started!';
}
