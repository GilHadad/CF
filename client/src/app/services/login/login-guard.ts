import {Injectable} from '@angular/core';
import {
  CanActivate, Router,
  ActivatedRouteSnapshot,
  RouterStateSnapshot
} from '@angular/router';
import {LoginService} from './login-service.service';

@Injectable()
export class LoginGuard implements CanActivate {
  constructor(private loginService: LoginService, private router: Router) {}

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Promise<boolean> {
    const url: string = state.url;

    return this.checkLogin(url);
  }

  checkLogin(url: string): Promise<boolean> {
    return this.loginService.isUserLoggedIn()
      .then(isLoggedIn => {
        if (!isLoggedIn) {
          this.loginService.registerUrl(url);
          this.router.navigate(['/login']);
        }
        return isLoggedIn;
      });
  }
}
