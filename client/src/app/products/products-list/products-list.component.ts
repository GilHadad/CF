import { Component, OnInit, OnDestroy } from '@angular/core';
import { ProducService } from '../products-service/products.service';

@Component({
  selector: 'app-products-list',
  templateUrl: './products-list.component.html',
  styleUrls: ['./products-list.component.css'],

  providers: [ProducService],
})
export class ProductsListComponent implements OnInit, OnDestroy {
  private req: any;
  ProductList: [any];
  titel = 'Getting started:';
  todayDate;

  constructor(private _products: ProducService) { }

  ngOnInit() {
    this.todayDate = new Date()

    this.req = this._products.list().subscribe(data => {
      this.ProductList = data
      console.log(data)
    })

  }


  ngOnDestroy() {
    this.req.unsubscribe()
  }

}
