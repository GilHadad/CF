import {Router} from '@angular/router';
import {Observable, Subject} from 'rxjs/Rx';
import {APP_CONFIG, AppConfig} from '../../app.conf';
import {HttpClient} from '@angular/common/http';
import {Inject, Injectable} from '@angular/core';

interface LoginResponse {
  success: boolean;
  msg: string;
}
interface UserDetails {
  username: string,
  email: string,
  first_name: string,
  last_name: string
};


const loginUrl = '/rest-auth/login/';
const logoutUrl = '/rest-auth/logout/';
const userDetaulsUrl = '/rest-auth/user/';
@Injectable()
export class LoginService {
  private userDetails: UserDetails = null;
  private nextUrl = '';

  constructor(
    private http: HttpClient,
    @Inject(APP_CONFIG) private config: AppConfig,
    private router: Router
  ) {}

  public login(username: string, password: string): Observable<LoginResponse> {
    const subject = new Subject<LoginResponse>();

    this.http.post(this.config.baseUrl + loginUrl, {username, password})
      .map(data => ({success: true, msg: ''}))
      .catch(e => Observable.of({success: false, msg: e}))
      .subscribe(subject);

    subject.subscribe(({success}) => {
      if (success) {
        this.router.navigate([this.nextUrl]);
      }
    });
    return subject;
  }

  public logout() {
    this.userDetails = null;
    /* don't really handle logout failure, might want to change later */
    this.http.post(this.config.baseUrl + logoutUrl, null)
      .catch(e => [])
      .subscribe(() => this.router.navigate(['/']));
  }

  public isUserLoggedIn() {
    return this.getUserDetails().then(userDetails => !!userDetails);
  }

  public registerUrl(url: string) {
    this.nextUrl = url;
  }

  /* TODO: maybe convert to observalbe */
  public getUserDetails(): Promise<UserDetails> {
    if (!!this.userDetails) {
      return Promise.resolve(this.userDetails);
    } else {
      return new Promise(resolve => {
        this.http.get<UserDetails>(this.config.baseUrl + userDetaulsUrl)
          .catch(e => {
            console.error('error getting user details', e);
            return Observable.of(null as UserDetails)
          })
          .subscribe(userDetails => {
            this.userDetails = userDetails;
            resolve(userDetails);
          })
      });
    }
  }
}
