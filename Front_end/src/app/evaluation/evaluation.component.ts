import { Component, OnInit } from '@angular/core';
import {APIService} from "../formulaire/APIService";
import {Router} from "@angular/router";

@Component({
  selector: 'app-evaluation',
  templateUrl: './evaluation.component.html',
  styleUrls: ['./evaluation.component.css']
})
export class EvaluationComponent implements OnInit {

  constructor(private apiService:APIService,private router:Router) { }
  error_value="";
  x=true;
  id;


  ngOnInit() {
  }
  onClick(id){
    this.id=id;
    this.x=false;
    this.apiService.getErrorRange(id).subscribe(
      data=>{
        console.log(data);
        this.error_value=<string>data["error_value"];
      }
    )
  }

  onClickPlots(){
    this.router.navigate(['/evaluation/plots']);
  }
}
