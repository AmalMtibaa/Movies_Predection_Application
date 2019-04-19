import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {FormulaireComponent} from "./formulaire/formulaire.component";
import {AccueikComponent} from "./accueik/accueik.component";
import {EvaluationComponent} from "./evaluation/evaluation.component";
import {ExempleComponent} from "./exemple/exemple.component";
import {PlotsComponent} from "./evaluation/plots/plots.component";

const routes: Routes = [
  { path: '', component: AccueikComponent },
  { path: 'formulaire', component: FormulaireComponent },
  { path: 'evaluation', component: EvaluationComponent},
  { path: 'evaluation/plots', component: PlotsComponent},
  { path: 'exemple', component: ExempleComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
