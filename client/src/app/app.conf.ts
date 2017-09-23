import {InjectionToken} from '@angular/core';

// ugly bug in angular-cli prevents us using just interface and const
// https://github.com/angular/angular-cli/issues/2034
export class AppConfig {
  public baseUrl: string;
  constructor(p: {baseUrl: string}) {
    Object.assign(this, p);
  }
}

export const appConfig = new AppConfig({
  baseUrl: 'http://localhost:4200/api'
});

export let APP_CONFIG = new InjectionToken<AppConfig>('app.config');
