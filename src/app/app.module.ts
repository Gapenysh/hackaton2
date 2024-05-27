import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {HttpClientModule} from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { WorkshopComponent } from './pages/workshop/workshop.component';
import { WorkshopIdeaComponent } from './pages/workshop-idea/workshop-idea.component';
import { ResumeFormComponent } from './pages/resume-form/resume-form.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    WorkshopComponent,
    WorkshopIdeaComponent,
    ResumeFormComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
