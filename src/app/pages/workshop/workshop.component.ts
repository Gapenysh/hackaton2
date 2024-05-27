import { Component } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Loner } from '../../types/user.interface'

@Component({
	selector: 'app-workshop',
	templateUrl: './workshop.component.html',
	styleUrls: ['./workshop.component.scss'],
})
export class WorkshopComponent {
	number: any
	Array(arg0: number) {
		throw new Error('Method not implemented.')
	}
	loners: Loner[] = [] // Переменная для хранения данных о участниках
	originalLoners: Loner[] = [] // Переменная для хранения оригинального списка участников
	showLoners: boolean = false // Переменная для управления отображением списка
	showTeam:boolean=false
	createTeamFormShown: boolean = false
	teamName: string = ''
	teamSize: number = 0
	selectedRoles: string[] = []
	roleImages: { [key: string]: string } = {
		backend: '../../../assets/images/backend.png',
		frontend: '../../../assets/images/frontend.png',
		designer: '../../../assets/images/designer.png',
		analyst: '../../../assets/images/analyst.png',
	}

	teams: any[] = [];

	buttonImageSrc: string[] = []
	isButtonPressed: boolean[] = []

	roles = ['backend', 'frontend', 'designer', 'analyst']

	constructor(private http: HttpClient) {
		this.preloadImages()
	}

	ngOnInit() {
		this.teamImages.forEach((_, index) => {
			this.buttonImageSrc[index] =
				'../../../assets/images/icons8-plus-button-16.png'
			this.isButtonPressed[index] = false
		})
	}

	isButtonActive = false

	teamImages: any[] = []
	showImages: boolean = false
	onButtonClick() {
		this.isButtonActive = !this.isButtonActive
	}
	showLonersList() {
		this.showLoners = !this.showLoners // Переключаем значение свойства showLoners

		if (this.showLoners) {
			// Если свойство showLoners равно true, то загружаем данные
			this.http
				.get<Loner[]>('http://192.168.1.238:3000/construcktor')
				.subscribe(
					(response) => {
						console.log('Список участников успешно получен!', response)
						this.loners = response // Сохраняем данные в локальной переменной
					},
					(error) => {
						console.error('Ошибка при получении списка участников:', error)
					}
				)
		}
	}

	filterLoners(event: any) {
		const selectedRole = event.target.value

		if (selectedRole === '') {
			this.loners = this.originalLoners // Возвращаем оригинальный список участников
			return
		}

		this.loners = this.originalLoners.filter(
			(loner: Loner) => loner.role === selectedRole
		) // Фильтруем оригинальный список участников
		this.showLoners = true
	}

	showCreateTeamForm() {
		this.createTeamFormShown = !this.createTeamFormShown
	}
	showTeams() {
		this.showTeam = !this.showTeam;
	}

	onTeamSizeChange() {
		this.selectedRoles.length = 0
	}
	getArray(size: number): Array<number> {
		return Array.from({ length: size }, (_, i) => i)
	}
	createTeam() {
		this.showImages = true
		this.teamImages = this.selectedRoles.map((role, index) => ({
			role,
			image: this.roleImages[role],
			order: index + 1,
		}))
	}
	preloadImages() {
		this.teamImages.forEach((item) => {
			const img = new Image()
			img.src = item.image
		})

		this.buttonImageSrc.forEach((src) => {
			const img = new Image()
			img.src = src
		})
	}
	handleMouseover(index: number) {
		// Change cursor style on mouseover
		// (no need to do anything here)
	}
	handleButtonClick(index: number) {
		// Change button image on click
		this.isButtonPressed[index] = !this.isButtonPressed[index]
		this.buttonImageSrc[index] = this.isButtonPressed[index]
			? '../../../assets/images/icons8-check-mark-16.png'
			: '../../../assets/images/icons8-plus-button-16.png'
	}
	sendTeamData() {
		const teamData = {
		  teamName: this.teamName,
		  teamSize: this.teamSize,
		  selectedRoles: this.selectedRoles,
		};
	
		this.http
		  .post<Loner[]>('http://192.168.1.238:3000/construcktor', teamData)
		  .subscribe(
			(response) => {
			  console.log('Данные команды успешно отправлены!', response);
			  // ... ваш код для обработки успешной отправки ...
			  this.getTeams();
			},
			(error) => {
			  console.error('Ошибка при отправке данных команды:', error);
			  // ... ваш код для обработки ошибки при отправке ...
			}
		  );
	  }
	
	  getTeams() {
		this.http
		  .get<any[]>('http://192.168.1.238:3000/construcktor')
		  .subscribe(
			(response) => {
			  console.log('Список команд успешно получен!', response);
			  this.teams = response; // Сохраняем данные о командах в локальной переменной
			},
			(error) => {
			  console.error('Ошибка при получении списка команд:', error);
			  // ... ваш код для обработки ошибки при получении ...
			}
		  );
	  }
}
