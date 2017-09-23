import {APP_CONFIG, AppConfig} from '../../app.conf';
import {Observable} from 'rxjs/Rx';
import {Inject, Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

const endpoint = '/api-base/products'


@Injectable()
export class ProducService {
  private url: string;
  constructor(private http: HttpClient, @Inject(APP_CONFIG) private appConfig: AppConfig) {
    this.url = appConfig.baseUrl + endpoint;
  }

  list() {
    return this.http.get<any[]>(this.url)
      .catch(this.handleError);
  }

  get(slug) {
    return this.http.get<any[]>(this.url)
      .map(response => {
        const data = response.filter(item => {
          if (item.slug === slug) {
            return item
          }
        })
        if (data.length === 1) {
          return data[0]
        }
        return {}
      })
      .catch(this.handleError)

  }

  private handleError(error: any, caught: any) {
    console.log(error, caught)
    return Observable.of([]);
  }


}
