import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormulaireComponent } from './formulaire/formulaire.component';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";
import {APIService} from "./formulaire/APIService";
import { AccueikComponent } from './accueik/accueik.component';
import { EvaluationComponent } from './evaluation/evaluation.component';
import { ExempleComponent } from './exemple/exemple.component';
import { PlotsComponent } from './evaluation/plots/plots.component';

@NgModule({
  declarations: [
    AppComponent,
    FormulaireComponent,
    AccueikComponent,
    EvaluationComponent,
    ExempleComponent,
    PlotsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [APIService],
  bootstrap: [AppComponent]
})
export class AppModule { }
