import { TestBed, inject } from '@angular/core/testing';

import { SubscriberGuardService } from './subscriber-guard.service';

describe('SubscriberGuardService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SubscriberGuardService]
    });
  });

  it('should be created', inject([SubscriberGuardService], (service: SubscriberGuardService) => {
    expect(service).toBeTruthy();
  }));
});
