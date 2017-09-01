import { TestBed, inject } from '@angular/core/testing';

import { SubscriberLoginService } from './subscriber-login.service';

describe('SubscriberLoginService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SubscriberLoginService]
    });
  });

  it('should be created', inject([SubscriberLoginService], (service: SubscriberLoginService) => {
    expect(service).toBeTruthy();
  }));
});
