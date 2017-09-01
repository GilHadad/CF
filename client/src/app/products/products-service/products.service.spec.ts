import { TestBed, inject } from '@angular/core/testing';

import { ProducService } from './products.service';

describe('ProducsService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ProducService]
    });
  });

  it('should be created', inject([ProducService], (service: ProducService) => {
    expect(service).toBeTruthy();
  }));
});
