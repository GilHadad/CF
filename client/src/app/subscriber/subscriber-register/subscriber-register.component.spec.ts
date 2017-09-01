import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SubscriberRegisterComponent } from './subscriber-register.component';

describe('SubscriberRegisterComponent', () => {
  let component: SubscriberRegisterComponent;
  let fixture: ComponentFixture<SubscriberRegisterComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SubscriberRegisterComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SubscriberRegisterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
