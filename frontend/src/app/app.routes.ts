import { Routes } from '@angular/router';
import { MapComponent } from './components/map/map.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { CollegeListComponent } from './components/college-list/college-list.component';
import { CollegeDetailComponent } from './components/college-detail/college-detail.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { authGuard } from './guards/auth-guard';

export const routes: Routes = [
    { path: 'dashboard', component: DashboardComponent },
    { path: 'map', component: MapComponent },
    { path: 'list', component: CollegeListComponent },
    { path: 'details/:id', component: CollegeDetailComponent },
    { path: 'login', component: LoginComponent },
    { path: 'register', component: RegisterComponent },
    { path: '', redirectTo: '/dashboard', pathMatch: 'full' }
];
