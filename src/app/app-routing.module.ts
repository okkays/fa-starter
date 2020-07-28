import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ClubComponent } from './club/club.component';

const routes: Routes = [
  { path: 'club/:id', component: ClubComponent },
  { path: '**', redirectTo: 'club/214176' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
