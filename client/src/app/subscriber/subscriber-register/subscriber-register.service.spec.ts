import { TestBed, inject } from '@angular/core/testing';

import { SubscriberRegisterService } from './subscriber-register.service';

describe('SubscriberRegisterService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SubscriberRegisterService]
    });
  });

  it('should be created', inject([SubscriberRegisterService], (service: SubscriberRegisterService) => {
    expect(service).toBeTruthy();
  }));
});
