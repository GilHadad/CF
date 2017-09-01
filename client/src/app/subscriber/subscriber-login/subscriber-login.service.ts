import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class SubscriberLoginService {
  private _isLoggedIn = false;
  private username: string;
  constructor(private http: Http) {
  };

  public login(username: string, password: string) {
    this.http.post('/api/users/login/', { username, password })
      .toPromise()
      .then(response => {
        const data = response.json();
        this._isLoggedIn = true;
        this.username = data.username;
        console.log(data);
      })
      .catch(error => console.log(error));

  }
  isLoggedIn(): boolean {
    return this._isLoggedIn;
  }

  getUsername() {
    return this.username;
  }
}
