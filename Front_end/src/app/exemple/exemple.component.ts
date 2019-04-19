import { Component, OnInit } from '@angular/core';
import {APIService} from "../formulaire/APIService";

@Component({
  selector: 'app-exemple',
  templateUrl: './exemple.component.html',
  styleUrls: ['./exemple.component.css']
})
export class ExempleComponent implements OnInit {

  constructor(private apiService: APIService) { }
  res;
  ngOnInit() {
    this.apiService.getFirstFive().subscribe(
      data=>{
        console.log(data);
        this.res=data["firstFive"];
      }
    )
  }
  predection="";
  isTrue="";
  predict(id){
    this.apiService.predict(id).subscribe(
      data=>{
        this.predection=data["predection"];
        this.isTrue=data["isTrue"];
      }
    )
  }

}
