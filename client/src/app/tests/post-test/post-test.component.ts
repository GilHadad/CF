import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';

import { TestPostService } from './test-post.service'




@Component({
  selector: 'app-post-test',
  templateUrl: './post-test.component.html',
  styleUrls: ['./post-test.component.css'],

  providers: [TestPostService],
})
export class PostTestComponent implements OnInit, OnDestroy {
  private req: any;
  getData: string;
  postData: string;
  myForm: FormGroup;

  constructor(private _TestPost: TestPostService, fb: FormBuilder) {
    this.myForm = fb.group({
      'sku': ['ABC123']
    });
  }

  ngOnInit() {
  }

  onTestGet() {
    this.req = this._TestPost.getCurrentTime().subscribe(
      data => this.getData = JSON.stringify(data),
      error => alert(error),
      () => console.log('get is done!!!')
    )

  }

  onTestPost() {
    this.req = this._TestPost.postJson().subscribe(
      data => this.postData = JSON.stringify(data),
      error => alert(error),
      () => console.log('post is done!!!')
    )
  }

  ngOnDestroy() {
    this.req.unsubscribe()
  }

// forms
  onSubmit(form: any): void {
    console.log('you submitted value:', form);
  }

}
