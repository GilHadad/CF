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
<<<<<<< HEAD
    component: HomeComponent
=======
    redirectTo: 'home',
    pathMatch: 'full',
  },
>>>>>>> 2c52a218d0bfaf1596141840b9a543933027bff6

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
<<<<<<< HEAD
    path: 'subscriber-login',
    component: SubscriberLoginComponent

=======
    path: 'login',
    component: SubscriberLoginComponent
>>>>>>> 2c52a218d0bfaf1596141840b9a543933027bff6
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

