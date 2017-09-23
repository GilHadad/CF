import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
<<<<<<< HEAD
import { NgModule } from '@angular/core';


=======

>>>>>>> 2c52a218d0bfaf1596141840b9a543933027bff6
import { HomeComponent } from './base/home/home.component';
import { ProductDetailsComponent } from './products/product-details/product-details.component';
import { LoginGuard } from './services/login/login-guard';
import { SubscriberLoginComponent } from './subscriber/subscriber-login/subscriber-login.component';
import { PostTestComponent } from './tests/post-test/post-test.component';

const appRoutes: Routes = [
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full',
  },
  {
    path: 'home',
    component: HomeComponent,
    canActivate: [LoginGuard]
  },

  {
    path: 'getting-started/:slug',
    component: ProductDetailsComponent

  },

  {
    path: 'login',
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


export class AppRoutingModule {}

