import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { HttpModule } from '@angular/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AlertModule } from 'ngx-bootstrap';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app.routing';

import { ProductsListComponent } from './products/products-list/products-list.component';
import { ProductDetailsComponent } from './products/product-details/product-details.component';

import { HeaderNavbarComponent } from './base/header-navbar/header-navbar.component';
import { HomeComponent } from './base/home/home.component';
import { FooterComponent } from './base/footer/footer.component';

import { AngularFontAwesomeModule } from 'angular-font-awesome/angular-font-awesome';
import { SubscriberLoginComponent } from './subscriber/subscriber-login/subscriber-login.component';
import { SubscriberRegisterComponent } from './subscriber/subscriber-register/subscriber-register.component';

import { PostTestComponent } from './tests/post-test/post-test.component';



@NgModule({
  declarations: [
    AppComponent,
    HeaderNavbarComponent,
    HomeComponent,
    ProductsListComponent,
    ProductDetailsComponent,
    FooterComponent,
    SubscriberLoginComponent,
    PostTestComponent,
    SubscriberRegisterComponent,

  ],
  imports: [
    AppRoutingModule,
    HttpModule,
    FormsModule,
    ReactiveFormsModule,

    BrowserModule,
    AlertModule.forRoot(),

    AngularFontAwesomeModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
