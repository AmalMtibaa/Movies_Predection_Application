/**
 * Created by asus on 28/03/2019.
 */
import { Injectable } from  '@angular/core';
import { HttpClient} from  '@angular/common/http';
import {HttpHeaders} from "@angular/common/http";

@Injectable({
  providedIn:  'root'
})

export  class  APIService {

  constructor(private  httpClient:  HttpClient) {}

  API_URL  =  'http://127.0.0.1:5002/';

  sendFormulaire(formulaire){

    const headers = new HttpHeaders()
      .set('Authorization', 'my-auth-token')
      .set('Content-Type', 'application/json');

    return this.httpClient.post(this.API_URL, formulaire, {headers: headers});
  }

  getErrorRange(algo_id){
    return this.httpClient.get(`http://127.0.0.1:5002/evaluation/${algo_id}`)
  }

  getFirstFive(){
    return this.httpClient.get("http://127.0.0.1:5002/getFirstFiveLines")
  }

  predict(id){
    return this.httpClient.get(`http://127.0.0.1:5002/example/${id}`)
  }




}


