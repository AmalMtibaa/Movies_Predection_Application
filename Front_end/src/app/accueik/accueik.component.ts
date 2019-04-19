import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-accueik',
  templateUrl: './accueik.component.html',
  styleUrls: ['./accueik.component.css']
})
export class AccueikComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
  }

  onClick(choice){
    if(choice==0){
      this.router.navigate(['/formulaire']);
    }
    if(choice==1){
      this.router.navigate(['/evaluation']);
    }
    if(choice==2){
      this.router.navigate(['/exemple']);
    }
  }

}
