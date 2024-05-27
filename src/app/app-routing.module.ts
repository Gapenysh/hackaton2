import { NgModule } from '@angular/core'
import { RouterModule, Routes } from '@angular/router'
import { HomeComponent } from './pages/home/home.component'
import { WorkshopComponent } from './pages/workshop/workshop.component'
import { WorkshopIdeaComponent } from './pages/workshop-idea/workshop-idea.component'
import { ResumeFormComponent } from './pages/resume-form/resume-form.component'

const routes: Routes = [
	{
		path: 'constructor',
		component: WorkshopComponent,
		title: 'Конструктор',
	},
	{
		path: 'fill-resume',
		component: ResumeFormComponent,
		title: 'резюме',
	},
	{
		path: '**',
		component: WorkshopComponent,
	},
]

@NgModule({
	imports: [RouterModule.forRoot(routes)],
	exports: [RouterModule],
})
export class AppRoutingModule {}
