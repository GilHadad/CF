import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';


import { HomeComponent } from './base/home/home.component';
import { ProductDetailsComponent } from './products/product-details/product-details.component';
import { SubscriberLoginComponent } from './subscriber/subscriber-login/subscriber-login.component';


import { PostTestComponent } from './tests/post-test/post-test.component';

const appRoutes: Routes = [
  {
    path: '',
    component: HomeComponent

  },

  {
    path: 'getting-started/:slug',
    component: ProductDetailsComponent

  },

  {
    path: 'subscriber-login',
    component: SubscriberLoginComponent

  },

  {
    path: 'tests',
    component: PostTestComponent

  }

]


@NgModule({
  imports: [
    RouterModule.forRoot(
      appRoutes
    )
  ],
  exports: [
    RouterModule
  ]

})


export class AppRoutingModule{}

