export interface Loner {
	name: string
	role: string
	skills: string
}

export enum Role {
  Frontend = 'Frontend',
  Backend = 'Backend',
  Designer = 'Designer',
  Analyst = 'Analyst'
}

export interface TeamMember {
  role: Role;
}

export interface Team {
  name: string;
  members: TeamMember[];
}