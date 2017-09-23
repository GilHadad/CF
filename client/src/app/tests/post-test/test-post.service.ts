import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Injectable} from '@angular/core';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

const endpoint_get = 'http://date.jsontest.com'
const endpoint_post = 'http://validate.jsontest.com'
const post_data_params = {
  var1: 'test',
  var2: 3,
  var3: 'gil hadad!!!!',
  gil: 4545
}

@Injectable()
export class TestPostService {

  constructor(private http: HttpClient) {}

  getCurrentTime() {
    return this.http.get(endpoint_get)
      .catch(this.handleError)
  }

  postJson() {
    const json = JSON.stringify(post_data_params)
    const params = 'json=' + json
    const headers = new HttpHeaders()

    headers.append('Content-Type', 'application/x-www-form-urlencoded')
    console.log(Headers)

    return this.http.post(endpoint_post, params, {headers: headers})
      .catch(this.handleError)
  }

  private handleError(error: any, caught: any): any {
    console.log(error, caught)
  }

}
