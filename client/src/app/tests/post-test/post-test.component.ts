import { Component, OnInit, OnDestroy } from '@angular/core';
import { TestPostService } from "./test-post.service"

@Component({
  selector: 'app-post-test',
  templateUrl: './post-test.component.html',
  styleUrls: ['./post-test.component.css'],

  providers: [TestPostService],
})
export class PostTestComponent implements OnInit, OnDestroy {
  private req: any;
  getData:string;
  postData:string;

  constructor(private _TestPost: TestPostService) { }

  ngOnInit() {
  }

  onTestGet(){
    this.req = this._TestPost.getCurrentTime().subscribe(
      data => this.getData = JSON.stringify(data),
      error => alert(error),
      () => console.log('get is done!!!')
    )

  }

  onTestPost(){
    this.req = this._TestPost.postJson().subscribe(
      data => this.postData = JSON.stringify(data),
      error => alert(error),
      () => console.log('post is done!!!')
    )
  }

  ngOnDestroy() {
    this.req.unsubscribe()
  }

}
