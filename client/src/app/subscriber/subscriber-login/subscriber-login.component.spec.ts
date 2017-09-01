import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SubscriberLoginComponent } from './subscriber-login.component';

describe('SubscriberLoginComponent', () => {
  let component: SubscriberLoginComponent;
  let fixture: ComponentFixture<SubscriberLoginComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SubscriberLoginComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SubscriberLoginComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
