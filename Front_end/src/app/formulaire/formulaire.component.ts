import { Component, OnInit } from '@angular/core';
import {FormGroup, FormControl, FormArray} from "@angular/forms";
import {APIService} from "./APIService";

@Component({
  selector: 'app-formulaire',
  templateUrl: './formulaire.component.html',
  styleUrls: ['./formulaire.component.css']
})
export class FormulaireComponent implements OnInit {

  constructor(private apiService:APIService) { }
  form:FormGroup;
  ngOnInit() {

    this.form=new FormGroup({
      'budget':new FormControl(''),
      'genres':new FormArray([]),
      'keywords':new FormControl(),
      'original_language':new FormControl('en'),
      'popularity':new FormControl(),
      'production_companies':new FormArray([]),
      'release_date':new FormControl(),
      'runtime':new FormControl(),
      'title':new FormControl(),
      'vote_average':new FormControl(),
      'vote_count':new FormControl(),
      'castgrade':new FormControl('Bad'),
      'directorGrade':new FormControl('Bad'),
      'writerGrade':new FormControl('Bad'),

    });
  }

    onCheckboxChange(option, event) {
      if (event.target.checked) {
        this.form.value["production_companies"].push(option)
      } else {
        for (let i = 0; i < this.productionCompanies.length; i++) {
          if ( this.form.value['production_companies'][i] == option) {
            this.form.value['production_companies'].splice(i,1);
          }
        }
      }
      console.log(this.form.value["production_companies"]);
    }

  onCheckboxChange1(option, event) {
    if (event.target.checked) {
      this.form.value["genres"].push(option)
    } else {
      for (let i = 0; i < this.productionCompanies.length; i++) {
        if ( this.form.value['genres'][i] == option) {
          this.form.value['genres'].splice(i,1);
        }
      }
    }
    console.log(this.form.value["genres"]);
  }
  genres_choices=['Action','Drama','Roamnce','Fantasy','Adventure','Action','Science Fiction','Thriller','Family','Animation','Comedy','History','Western','Crime','politics','Horror','Mystery','Music','Documentary']
  productionCompanies=['Walt Disney Pictures','Ingenious Film Partners','DC Comics','Marvel Studios','Columbia Pictures','Legendary Pictures','Amblin Entertainment','Paramount Pictures','Warner Bros.','Universal Pictures','Hollywood Pictures','Paramount Pictures','TriStar Pictures','Beacon Communications','Fox Searchlight Pictures','Bearing Fruit Entertainment','"New Line Cinema','Relativity Media','United Artists','Rai Cinema','Granada Film Production','Arts Council of England','Orion Pictures','Block 2 Pictures','Hollywood Pictures','Fox 2000 Pictures','American Zoetrope','Twentieth Century Fox Film Corporation','New Line Cinema','Orion Pictures','Dreamland Productions','Front Street Pictures']

  predection="";
  onSubmit(algorithme_id){
    let line=this.form.value;
    // let keywords=line["keywords"];
    // console.log(keywords);
    // let x=[];
    // x=keywords.split(" ");

    line["keywords"]=[];
    line["algorithme_id"]=algorithme_id;
    console.log(line);
    this.apiService.sendFormulaire(line).subscribe(data=>{
      console.log(data);
      this.predection=data["predection"]
    })
  }
}
