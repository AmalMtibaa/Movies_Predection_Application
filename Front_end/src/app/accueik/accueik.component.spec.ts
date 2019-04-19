import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AccueikComponent } from './accueik.component';

describe('AccueikComponent', () => {
  let component: AccueikComponent;
  let fixture: ComponentFixture<AccueikComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AccueikComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AccueikComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
