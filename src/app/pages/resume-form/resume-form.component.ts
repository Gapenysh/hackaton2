import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-resume-form',
  templateUrl: './resume-form.component.html',
  styleUrls: ['./resume-form.component.scss']
})
export class ResumeFormComponent {
  name!: string;
  role!: string;
  skills!: string;

  constructor(private http: HttpClient, private router: Router) {}

  ngOnInit(): void {}

  onSubmit() {
    const resumeData = {
      name: this.name,
      role: this.role,
      skills: this.skills,
    };

    this.http.post('http://192.168.1.238:3000//construcktor/create_resume', resumeData).subscribe(
      (response) => {
        console.log('Резюме успешно отправлено!', response);
        this.router.navigate(['/constructor']);
      },
      (error) => {
        console.error('Ошибка при отправке резюме:', error);
      }
    );
  }
}
