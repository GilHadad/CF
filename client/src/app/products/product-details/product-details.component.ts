import { Subscription } from 'rxjs/Rx';
import {Component, OnDestroy, OnInit} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {ProducService} from '../products-service/products.service';

@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html',
  styleUrls: ['./product-details.component.css'],

  providers: [ProducService],
})
export class ProductDetailsComponent implements OnInit, OnDestroy {
  private routeSub: Subscription;
  private req: any;
  product: any;
  slug: string;

  constructor(private route: ActivatedRoute, private _products: ProducService) {}

  ngOnInit() {
    this.routeSub = this.route.paramMap.subscribe(params => {
      this.slug = params.get('slug')
      this.req = this._products.get(this.slug).subscribe(data => {
        this.product = data
        console.log(data)
      })
    })

  }

  ngOnDestroy() {
    this.routeSub.unsubscribe()
    this.req.unsubscribe()

  }

}
