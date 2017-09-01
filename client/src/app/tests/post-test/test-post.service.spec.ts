import { TestBed, inject } from '@angular/core/testing';

import { TestPostService } from './test-post.service';

describe('TestPostService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TestPostService]
    });
  });

  it('should be created', inject([TestPostService], (service: TestPostService) => {
    expect(service).toBeTruthy();
  }));
});
